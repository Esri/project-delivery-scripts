# Case 2: Enterprise Scripts

## This folder contains scripts that the user will run if they have ArcGIS Enterprise and an ArcGIS Online Organization and want to use both to share content with their customers (the delivery organizations). The user's ArcGIS Online Organization and/or their Portal will contain a template group containing items (services, feature layers, maps, scenes, apps, etc.) that they want to clone for each delivery organization that they work with.

### Script 1: Setup_Collaboration.ipynb
This script will establish the collaboration between the ArcGIS Online Organization and the ArcGIS Enterprise systems, with the Online Organization as the host. There will be a group for collaboration in Enterprise, and another in AGOL. After the script has run, these groups will share data and items by copy (if possible) and by reference (if copy is not possible). Server Service items are the only things known that cannot be synced by copy and will have to be synced by reference. All the items in the Enterprise and AGOL groups that will be synced need to have "Enable Sync" checked in their settings page in order to sync by copy. After the script has run there will also be a folder in each org's content that will have the same title as the collaboration title and will contain all the shared content for the collaboration. 

Before running this script, you need to:
- find the group IDs for the collaboration/ template groups in ArcGIS Online and Enterprise
- ensure that enable sync is checked on the items in these groups

In order to make it sync sooner than 24 hours, you need to open up the Enterprise Portal, go to Organization > Collaborations > click on the collaboration name > click on the gear icon under Action, and then click Edit Workspace. Click sync at scheduled intervals and set it to repeat every 1 hour, so it will do the first sync one hour from now. Make sure it says Feature layers are sent as copies, not references!