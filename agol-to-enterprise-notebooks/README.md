# agol-to-enterprise-notebooks

## Notebook 1: Clone_Template_Group.ipynb
In this notebook, the template group will be copied within the source organization and renamed so it can be identified as the group to be shared with the target organization. A new folder will be created and all the items shared with each group will be copied, renamed, and stored in this new folder. 

## Notebook 2: Clone_Group_Source_to_Target.ipynb
In this notebook, a group will be cloned from the source organization to a target organization. 

## Notebook 3: Configure_Target_Org.ipynb
In this notebook, the target organization's User Interface will be customized with banner, boackground, thumbnail images, a description, a footer, and a featured group shown on the homepage. 

## Notebook 4: Configure_Target_Users.ipynb
In this notebook, we add users to the delivery org and invite them to groups. Users will be able to find the invites to the new groups on the 'Groups' tab or in their notifications. 

## Notebook 5: Setup_Collaboration.ipynb
In this notebook, we establish a collaboration between an ArcGIS Online Organization and an ArcGIS Enterprise system, with the Online Organization as the host. There will be a group added to the collaboration in Enterprise, and another in AGOL. After the notebook has run, these groups will share data and items by copy (if possible) and by reference (if copy is not possible). Server Service items are the only things know that cannot be synced by copy and will have to be synced by reference. After the notebook has run, there will be a folder in each org's content that will have the same title as the collaboration title and will contain all the content from the other participant in the collaboration.