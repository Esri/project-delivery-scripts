# Enterprise Scripts


## Script 1: Setup_Collaboration.ipynb
This script will establish the collaboration between the ArcGIS Online Organization and the ArcGIS Enterprise systems, with the Online Organization as the host. There will be a group for collaboration in Enterprise, and another in AGOL. After the script has run, these groups will share data and items by copy (if possible) and by reference (if copy is not possible). Server Service items are the only things known that cannot be synced by copy and will have to be synced by reference. After the script has run, the Online Organization will be set up as the project org for the next two scripts. there will also be a folder in each org's content that will have the same title as the collaboration title and will contain all the  content from the other participant in the collaboration. 

### Getting Started:
1. Ensure that there is a group set up that you will use for collaboration in both Online and Enterprise. These can be empty or have items in them and can be named different things.
2. Find the group IDs for the collaboration groups in ArcGIS Online and Enterprise. These can be found by navigating to the group page and looking in the URL (for example, if the URL is http://envisioning.maps.arcgis.com/home/group.html?id=a7903db4086641b98570bce5856a6364#overview, the group ID is "a7903db4086641b98570bce5856a6364".
3. Ensure that "Enable Sync" is checked on each item's setting page in each group.
4. Change the variables in cell 1. Example variables:
5. Run the notebook cell by cell.
6. After running...

#### Troubleshooting: 
After the first scheduled sync, you can view the logs on the portal machine (if the portal url is "https://pdoscriptdev.esri.com/portal", go to "https://pdoscriptdev.esri.com/portal/portaladmin/logs/") to see if there were any errors with the sync (ex. layers that were not able to sync by copy). If any layers failed to sync by copy and are synced by reference instead, they will need to be unshared and reshared, after the issue is fixed. You can find more information about this in the [`Collaboration FAQs`](https://enterprise.arcgis.com/en/portal/latest/administer/windows/common-questions-for-distributed-collaboration.htm). If a feature layer syncs by copy, the feature layer will show as feature layer (hosted) for the guest, but if it syncs by reference, it will just show as a feature layer.

In order to make it sync sooner than 24 hours, you need to open up the Enterprise Portal, go to Organization > Collaborations > click on the collaboration name > click on the gear icon under Action, and then click Edit Workspace. Click sync at scheduled intervals and set it to repeat every 1 hour, so it will do the first sync one hour from now. Make sure it says Feature layers are sent as copies, not references!


## Script 2: Clone_Groups.ipynb
In this script, the template groups will be copied within the Project organization and renamed so they can be identified
as the groups shared with the specific delivery organization. A new folder will be created, and all the items shared with
each group will be copied, renamed, and stored in this new folder.

### Getting Started:
1. Find the group IDs for the template groups. Example set-up in the project organization:
    - test-group (ID "a7903db4086641b98570bce5856a6364") contains:
        - Sample Layer
        - Sample Map
    - test-group-2 (ID "4d7ff4f81d6340428ef290b7de801204") contains:
        - Sample WebApp
2. Change the variables in cell 1. Example variables:
    - PROJECT_PORTAL = "https://envisioning.maps.arcgis.com"
    - PROJECT_USERNAME = "admin"
    - PROJECT_GROUP_IDS = ["a7903db4086641b98570bce5856a6364", "4d7ff4f81d6340428ef290b7de801204"]
    - COPY_PREFIX = "ACME"
3. Run the notebook cell by cell. 
    - In cell 3, you will need to enter thet password for the project username when prompted
    - In cell 5, the script will print out the existing template groups and items that will be copied over
    - In cell 6, the script will print out the groups and items that were copied and renamed
4. Continuing this example, after running this script, the following should now also exist in the project organization:
    - ACME-test-group contains:
        - ACME Sample Layer
        - ACME Sample Map
    - ACME-test-group-2 contains:
        - ACME WebApp
    - ACME Content, which is a folder in content, contains:
        - ACME Sample Layer
        - ACME Sample Map
        - ACME WebApp


## Script 3: Configure_Org.ipynb
In this script, the delivery organization's User Interface will be customized with banner, background, and thumbnail images, description and footer text files, and a featured group shown on the homepage. The script will also add users to the delivery org and invite them to the groups in the project org that they should have access to. 

### Getting Started:
1. Find the group IDs for the featured group and for any groups in the project org you will be adding delivery org users to.
2. Set up the csv file of users. This csv should have columns for email, firstname, lastname, username, password, role, level, and groups. The groups column should contain group IDs that are separated by commas. There is a sample user csv in the Sample Config folder, and there is more information about formatting here (https://learn.arcgis.com/en/projects/set-up-an-arcgis-enterprise-portal/lessons/add-members-to-the-organization.htm) in steps 4 & 5.
3. Collect all other customization components. You should have a local folder containing items such as banner, background, and thumbnail images and description and footer text files.
4. Change the variables in cell 1. Example variables:
    - DELIVERY_URL = "https://esrienergy.maps.arcgis.com"
    - DELIVERY_USERNAME = "portaladmin"
    - FOLDER = "/Users/joesmith/Documents/Sample_Config" or FOLDER = "C:/Users/joesmith/Documents/Sample_Config"
    - GROUP_IDS = ["a7903db4086641b98570bce5856a6364", "4d7ff4f81d6340428ef290b7de801204"]
    - FEATURED_GROUP_ID = "4f4fcac023dc430294cea226231ab448"
    - MESSAGE = "You are invited to join a group!"
    - EXPIRATION = "3 Days"
5. Run the notebook cell by cell.
    - In cell 4, you will need to enter the passwords for the project and delivery organizations when prompted
    - In cell 6, the script will print out the users that were added to the delivery org and the project groups they were added to
6. At the end, your delivery org should have all the users in the csv file added and each should get one email invitation for each group listed for them. The delivery org will also be customized.