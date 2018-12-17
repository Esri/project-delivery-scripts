# Case 1: ArcGIS Online Only

## This folder contains scripts to run if the user has an ArcGIS Online Organization
## that they want to use to share content with their customers (the delivery organizations).
## The user's ArcGIS Online Organization will contain a template group or groups containing
## items (services, feature layers, maps, scenes, apps, etc.) that they want to clone
## for each delivery organization that they work with.

### Script 1: Clone_Groups.ipynb
In this script, the template groups will be copied within the Project organization and renamed so they can be identified
as the groups shared with the specific delivery organization. A new folder will be created, and all the items shared with
each group will be copied, renamed, and stored in this new folder.

Example case of script 1: The groups to be cloned and shared with delivery organization ACME are named "test-group" and "test-group-2". The items in "test-group" are "Sample Layer" and "Sample Map". The items in "test-group-2" are "Sample WebApp". The argument COPY_PREFIX is set to "ACME", and the FOLDER_SUFFIX is set to "Content". After the script is run, the project organization contains a group named "ACME-test-group" with items "ACME Sample Layer" and "ACME Sample Map", and a group named "ACME-test-group-2" with item "ACME Sample WebApp". The ACME copies of the layer, map, and webapp are all stored in a folder called "ACME Content". The original template groups and items still exist and can be copied over again for another delivery organization at any time.

Before you run this script, collect all the information needed for the global variables in the first cell of the jupyter notebook. Group IDs can be found by opening the group in portal (Groups > click on the group) and looking at the url. Within the URL there will be a section that says id=12345... and everything following "id=" before a # is the group ID.
- PROJECT_PORTAL: the url for the project portal that contains the template content (ex. "https://envisioning.maps.arcgis.com")
- PROJECT_USERNAME: an admin username for project portal log-on (ex. "admin")
- PROJECT_GROUP_IDS: ids for the template project groups that will be shared with the delivery org (ex. ["4d7ff4f81d6340428ef290b7de801204"])
- COPY_PREFIX: the word that will be appended to the front of template groups, items, and folder to distinguish these copies of the templates (ex. "ACME")
- FOLDER_SUFFIX: the base name for the folder containing these copies of the templates which will be combined with the copy_prefix (ex. "Content")

After the global variables have been set, run the notebook cell by cell. In cell 3, you will need to enter the password for the project username when prompted. In cell 5, the script will print the existing template groups and items that will be copied over for use with the delivery org, and in cell 6, the script will print out the groups and items that were copied and renamed.

### Script 2: Configure_Org.ipynb
In this script, the delivery organization's User Interface will be customized with banner, background, and thumbnail images, description and footer text files, and a featured group shown on the homepage. The script will also add users to the delivery org and invite them to the groups in the project org that they should have access to. 

Before you run this script, collect all the information needed for the global variables in the first cell of the jupyter notebook.
- PROJECT_URL: the url for the project portal
- PROJECT_USERNAME: an admin username for the project portal
- DELIVERY_URL: the url for the delivery portal that will be customized and have users added (ex. "https://esrienergy.maps.arcgis.com")
- DELIVERY_USERNAME: an admin username for the delivery portal (ex. "portaladmin")
- FOLDER: a local full path to the folder where the org customization files are located, using forward slashes (ex. "/Users/joesmith/Documents/Sample_Config")
- THUMBNAIL_FILENAME: the filename of the thumbnail image located in FOLDER (ex. "thumbnail.png")
- FOOTER_FILENAME: the filename of the footer text file located in FOLDER (ex. "footer.txt")
- BACKGROUND_FILENAME: the filename of the background image located in FOLDER (ex. "background.png")
- BANNER_FILENAME: the filename of the banner image located in FOLDER (ex. "banner.jpg")
- DESCRIPTION_FILENAME: the filename of the description text file located in FOLDER (ex. "description.txt")
- USERS_FILENAME: the filename of the csv file containing the new user info. This file will be formatted the same way as a csv file that would be used to upload users in portal, but it will have an extra column called "groups" that contains the ids of groups that each user should be added to. If a user should be added to multiple groups, they should be separated by commas and one pair of double quotes should enclose all the groups. If there are any groups that all users should be added to, place them in the GROUP_IDS variable. Documentation can be found at https://learn.arcgis.com/en/projects/set-up-an-arcgis-enterprise-portal/lessons/add-members-to-the-organization.htm, step 4 details the columns that should be included, and step 5 has an example csv file you can view or download. (ex. "users.csv")
- GROUP_IDS: a list of group ids for any groups in the project org that will be shared with *all* the users being added (ex. ["4d7ff4f81d6340428ef290b7de801204"])
- FEATURED_GROUP_ID: the id of a group to be displayed on the delivery org home page (ex. "4f4fcac023dc430294cea226231ab448")
- MESSAGE: a message that will be sent in the email to users when they are invited to join the project groups (ex. "You are invited to join a group!")
- EXPIRATION: how long the email invitations will be valid for (options are '1 Day', '3 Days', '1 Week', or '2 Weeks') (ex. '1 Day')

After the global variables have been set, run the notebook cell by cell. In cell 4, you will need to enter the passwords for the project organization and delivery organization when prompted. In cell 6 the script will print out the users that were added and which groups they were added to. 