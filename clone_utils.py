"""util functions to copy items and groups"""
import tempfile

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


def copy_item(item, target, owner=None, folder=None, target_groups=None,\
             modify_item=None, item_properties=ITEM_COPY_PROPERTIES):
    """Copy item to a target GIS
    * Assumes item does not yet exist

    Keyword arguments:
    item -- item to be copied
    target -- target GIS object
    owner -- user who owns item (default None)
    folder -- owner folder for the item (default None)
    target_groups -- group array where item will be shared (default None)
    modify_item -- callback function to update item before copy (default None)
    item_properties -- properties to be copied
    """

    try:
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

            # Create folder if doesn't exist
            if folder:
                target_folders = [f['title'] for f in owner.folders if f['title'] == folder]
                if not target_folders:
                    target.content.create_folder(folder, owner)

            # Create item
            target_item = target.content.add(new_item, data_file, thumbnail_file,\
                                             metadata_file, owner, folder)

            # Share item
            share_everyone = item.access == 'public'
            share_org = item.access in ['org', 'public']
            share_groups = target_groups if target_groups else []
            target_item.share(share_everyone, share_org, share_groups)

            return target_item

    except Exception as e:
        print('Item {} could not be created in the target portal'.format(item.title))
        print(e)

def copy_group(source, source_group, target,\
               modify_group=None, group_properties=GROUP_COPY_PROPERTIES):
    """Copy group to a target GIS

    Keyword arguments:
    source -- source GIS object
    source_group -- group to be copied
    target -- target GIS object
    modify_group -- callback function to update group before copy (default None)
    group_properties -- properties to be copied
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Copy group properties
            new_group = {property_name: source_group[property_name]\
              for property_name in group_properties}
            new_group = modify_group(new_group) if modify_group else new_group

            # ArcGIS Online to Enterprise
            if source_group['access'] == 'org'\
                and target.properties['portalMode'] == 'singletenant':
                new_group['access'] = 'public'
            # Enterprise to ArcGIS Online
            elif source_group['access'] == 'public'\
                and source.properties['portalMode'] == 'singletenant'\
                and target.properties['portalMode'] == 'multitenant'\
                and 'id' in target.properties:
                new_group['access'] = 'org'

            # Download thumbnail (if one exists)
            new_group['thumbnail'] = source_group.download_thumbnail(temp_dir)\
            if 'thumbnail' in source_group else None

            return target.groups.create_from_dict(new_group)

        except Exception as e:
            print("Error creating " + source_group['title'])
            print(e)


def copy_group_and_items(source, source_group, target, group_args={}, item_args={}):
    """Copy group and items to a target GIS

    See arguments for copy_group and copy_items
    """
    target_group = copy_group(source, source_group, target, **group_args)

    for item in source_group.content():
        copy_item(item, target, target_groups=[target_group], **item_args)

    return target_group

