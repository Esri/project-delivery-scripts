# ArcGIS Online Only Scripts


## Script 1: Clone_Groups.ipynb
In this script, the template groups will be copied within the Project organization and renamed so they can be identified as the groups shared with the specific delivery organization. A new folder will be created, and all the items shared with each group will be copied, renamed, and stored in this new folder.

### Getting Started:
1. Find the group IDs for the template groups. These can be found by navigating to the group page and looking in the URL (for example, if the URL is http://envisioning.maps.arcgis.com/home/group.html?id=a7903db4086641b98570bce5856a6364#overview, the group ID is "a7903db4086641b98570bce5856a6364". Example set-up in the project organization:
    - test-group (ID "a7903db4086641b98570bce5856a6364") contains:
        - Sample Layer
        - Sample Map
    - test-group-2 (ID "4d7ff4f81d6340428ef290b7de801204") contains:
        - Sample WebApp
2. Change the variables in cell 1. Example variables:
    - SOURCE_URL = "https://envisioning.maps.arcgis.com"
    - SOURCE_USERNAME = "admin"
    - SOURCE_GROUP_IDS = ["a7903db4086641b98570bce5856a6364", "4d7ff4f81d6340428ef290b7de801204"]
    - COPY_PREFIX = "ACME"
3. Run the notebook cell by cell. 
    - In cell 3, you will need to enter the password for the project username when prompted
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


## Script 2: Configure_Org.ipynb
In this script, the delivery organization's User Interface will be customized with banner, background, and thumbnail images, description and footer text files, and a featured group shown on the homepage. The script will also add users to the delivery org and invite them to the groups in the project org that they should have access to. Users will be able to find to the invites to the new groups on the 'Groups' tab or in their Notifications.

### Getting Started:
1. Find the group IDs for the featured group and for any groups in the project org you will be adding delivery org users to.
2. Set up the csv file of users. This csv should have columns for email, firstname, lastname, username, password, role, level, and groups. The groups column should contain group IDs that are separated by commas. There is a sample user csv in the Sample Config folder, and there is more information about formatting [`here`](https://learn.arcgis.com/en/projects/set-up-an-arcgis-enterprise-portal/lessons/add-members-to-the-organization.htm) in steps 4 & 5. Make sure that the User Roles you choose are able to be added to groups in other organizations! The default 'Viewer' role is not able to be added to groups outside of the organization.
4. Change the variables in cell 1. Example variables:
    - SOURCE_URL = "https://envisioning.maps.arcgis.com"
    - SOURCE_USERNAME = "admin"
    - TARGET_URL = "https://esrienergy.maps.arcgis.com"
    - TARGET_USERNAME = "portaladmin"
    - GROUP_IDS = ["a7903db4086641b98570bce5856a6364", "4d7ff4f81d6340428ef290b7de801204"]
    - FEATURED_GROUP_ID = "4f4fcac023dc430294cea226231ab448"
5. Run the notebook cell by cell.
    - In cell 4, you will need to enter the passwords for the project and delivery organizations when prompted
    - In cell 6, the script will print out the users that were added to the delivery org and the project groups they were added to
6. At the end, your delivery org should have all the users in the csv file added and each should get an invitation in their Organization Account for each group listed for them. Once they accept it, they will be shown in the group members in the Project Organization as well. The delivery org will also be customized.
