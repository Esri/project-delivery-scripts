"""util functions to copy items and groups"""
import tempfile
import csv

# script constants
GROUP_COPY_PROPERTIES = ['title', 'description', 'tags', 'snippet', 'phone',
                         'access', 'isInvitationOnly']
ITEM_COPY_PROPERTIES = ['title', 'type', 'typeKeywords', 'description', 'tags',
                        'snippet', 'extent', 'spatialReference', 'name',
                        'accessInformation', 'licenseInfo', 'culture', 'url']
TEXT_BASED_ITEM_TYPES = frozenset(['Web Map', 'Feature Service', 'Map Service', 'Web Scene',
                                   'Image Service', 'Feature Collection',
                                   'Feature Collection Template',
                                   'Web Mapping Application', 'Mobile Application',
                                   'Symbol Set', 'Color Set',
                                   'Windows Viewer Configuration'])

FILE_BASED_ITEM_TYPES = frozenset(['File Geodatabase', 'CSV', 'Image', 'KML', 'Locator Package',
                                   'Map Document', 'Shapefile', 'Microsoft Word', 'PDF',
                                   'Microsoft Powerpoint', 'Microsoft Excel', 'Layer Package',
                                   'Mobile Map Package', 'Geoprocessing Package', 'Scene Package',
                                   'Tile Package', 'Vector Tile Package'])

USER_FIELDS = ["username", "password", "firstname", "lastname", "email", "role", "groups",
               "groups", "description", "role", "provider", "idp_username", "level"]


def copy_item(item, target, owner, **kwargs):
    """Copy item to a target GIS
    * Has specific behavior:
    - If specify folder that doesn't exist, will create folder
    - If item exists, will change ownership and share to folder / groups

    args:
    item -- item to be copied
    target -- target GIS object
    owner -- user who owns item (default None)

    **kwargs:
    folder -- (optional) owner folder for the item (default None)
    target_groups -- (optional) group array where item will be shared (default None)
    modify_item -- (optional) callback function to update item before copy (default None)
    item_properties -- (optional) properties to be copied (default ITEM_COPY_PROPERTIES)
    """

    folder = kwargs.get("folder", None)
    target_groups = kwargs.get("target_groups", None)
    modify_item = kwargs.get("modify_item", None)
    item_properties = kwargs.get("item_properties", ITEM_COPY_PROPERTIES)

    print("INFO: Copying item {}".format(item['title']))

    try:

        # Create folder if doesn't exist
        if folder:
            target_folders = [f['title'] for f in owner.folders if f['title'] == folder]
            if not target_folders:
                target.content.create_folder(folder, owner)

        # Check if item already exists, if it does change owner and share to folder/groups
        s_items = target.content.search(query='title:{}'.format(item.title), item_type=item.type)
        for s_item in s_items:
            if s_item.title != item.title:
                continue
            print("WARN: Item {} already exists. Updating...".format(item['title']))
            share_groups = [g for g in target_groups if s_item not in g.content()]
            s_item.share(groups=[share_groups])
            s_item.move(folder, owner)
            return s_item

        with tempfile.TemporaryDirectory() as temp_dir:

            # Copy item properties
            new_item = {property_name: item[property_name] for property_name in item_properties}
            new_item = modify_item(new_item) if modify_item else new_item

            # Copy core item data
            data_file = None
            if item.type in TEXT_BASED_ITEM_TYPES:
                new_item['text'] = item.get_data(False)
            elif item.type in FILE_BASED_ITEM_TYPES:
                data_file = item.download(temp_dir)

            # Copy thumbnail and metadata
            thumbnail_file = item.download_thumbnail(temp_dir)
            metadata_file = item.download_metadata(temp_dir)

            # Create item
            target_item = target.content.add(new_item, data_file, thumbnail_file,
                                             metadata_file, owner, folder)

            # Share item
            share_everyone = item.access == 'public'
            share_org = item.access in ['org', 'public']
            share_groups = target_groups if target_groups else []
            target_item.share(share_everyone, share_org, share_groups)

            return target_item

    except Exception as e:
        print('ERR: Could not create item {}'.format(item.title))
        print(e)

def copy_group(source, source_group, target, **kwargs):
    """Copy group to a target GIS

    args:
    source -- source GIS object
    source_group -- group to be copied
    target -- target GIS object

    **kwargs:
    modify_group -- (optional) callback function to update group before copy (default None)
    group_properties -- (optional) properties to be copied (default GROUP_COPY_PROPERTIES)
    """

    modify_group = kwargs.get("modify_group", None)
    group_properties = kwargs.get("group_properties", GROUP_COPY_PROPERTIES)

    print("INFO: Copying group {}".format(source_group['title']))

    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Copy group properties
            new_group = ({property_name: source_group[property_name]
                          for property_name in group_properties})
            new_group = modify_group(new_group) if modify_group else new_group

            # ArcGIS Online to Enterprise
            if (source_group['access'] == 'org'
                    and target.properties['portalMode'] == 'singletenant'):
                new_group['access'] = 'public'
            # Enterprise to ArcGIS Online
            elif (source_group['access'] == 'public'
                  and source.properties['portalMode'] == 'singletenant'
                  and target.properties['portalMode'] == 'multitenant'
                  and 'id' in target.properties):
                new_group['access'] = 'org'

            # Download thumbnail (if one exists)
            new_group['thumbnail'] = (source_group.download_thumbnail(temp_dir)
                                      if 'thumbnail' in source_group
                                      else None)

            return target.groups.create_from_dict(new_group)

        except Exception as e:
            print("ERR: Could not create group {}".format(source_group['title']))
            print(e)


def copy_group_and_items(source, source_group, target, group_args={}, item_args={}):
    """Copy group and items to a target GIS

    args:
    source -- source GIS object
    source_group -- group to be copied
    target -- target GIS object
    group_args -- (optional) see copy_group **kwargs (default {})
    item_args -- (optional) see copy_items **kwargs (default {})
    """
    target_group = copy_group(source, source_group, target, **group_args)

    for item in source_group.content():
        copy_item(item, target, target_groups=[target_group], **item_args)

    return target_group

def add_user(user, gis, **kwargs):
    """Add user to the gis
    * Abstraction for creating from dict such as with csv
    * Handles moving to groups

    args:
    user -- a dictionary containing user fields, see fields:
    http://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#arcgis.gis.UserManager.create
    gis -- gis object where users are added

    **kwargs:
    groups -- (optional) destination groups, compliments those in dict (default [])
    field_map -- (optional) change keys from defaults in USER_FIELDS
    """

    groups = kwargs.get("groups", [])
    field_map = kwargs.get("field_map", {})

    try:

        # Define new user fields
        new_user = {}
        for field in USER_FIELDS:
            new_user[field] = (user.get(field_map[field], None)
                               if field in field_map
                               else user.get(field, None))

        print("INFO: Creating user {}".format(new_user["username"]))

        # Create/augment array of destination groups for user
        # Pop group from user because separate logic
        group_field = "groups" if "groups" not in field_map else field_map["groups"]
        group_str = new_user.pop(group_field, None)
        if group_str:
            group_list = group_str.split(",")
            for g in group_list:
                group_search = gis.groups.search(g)
                if group_search:
                    groups.append(group_search[0])

        # Create new user
        result = gis.users.create(**new_user)

        # Sometimes there's an error that doesn't throw
        if not result:
            return

        # Add user to groups
        for g in groups:
            try:
                g.add_users([new_user['username']])
            except Exception as e:
                print("ERR: Could not add user to group {}".format(g))
                print(e)

        return result

    except Exception as e:
        print("ERR: Could not create user {}".format(user['username']))
        print(e)

def add_users_csv(csv_file, gis, **kwargs):
    """Add users from csv to gis
    * Convenient abstraction for csvs

    args:
    csv_file -- path to csv with users to create
    gis -- gis object where users are added

    **kwargs:
    groups -- (optional) destination groups, compliments those in csv (default [])
    field_map -- (optional) change keys from defaults in USER_FIELDS, see fields:
    http://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#arcgis.gis.UserManager.create
    """
    results = []
    with open(csv_file, 'r') as users_csv:
        users = csv.DictReader(users_csv)
        for user in users:
            result = add_user(user, gis, **kwargs)
            results.append(result)
    
    return results
