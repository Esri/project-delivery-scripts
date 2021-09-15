# project-delivery-scripts

Project Delivery allows a Services company (the project or source organization) to purchase and manage ArcGIS Online on behalf of their end users (the delivery or target organizations). These scripts are meant to be a starting point for Services users to automate the deployment of their industry-specific maps and apps to end users. The notebooks allow you to automatically customize, populate with content, and add users to a new ArcGIS Online or ArcGIS Enterprise Organization for project delivery

There are four sets of notebooks. Each set of notebooks correspond to the target and source organization type:

1. ArcGIS Online to ArcGIS Online Notebooks: use the notebooks in this folder if the source and target are both ArcGIS Online organizations. 
2. ArcGIS Online to Enterprise Notebooks: use the notebooks in this folder if the source organization is ArcGIS Online and the target is an ArcGIS Enterprise organization. 
3. Enterprise to ArcGIS Online Notebooks: use the notebooks in this folder if the source organization is ArcGIS Enterprise and the target is an ArcGIS Online organization. 
4. Enterprise to Enterprise Notebooks: use the notebooks in this folder if the source and target are ArcGIS Enterprise organizations. 


## Features
* [`agol-to-agol-notebooks`](/agol-to-agol-notebooks) - Directory with notebooks to use if the source and target are both ArcGIS Online organizations
    * [`Clone_Template_Group.ipynb`](/agol-to-agol-notebooks/Clone_Template_Group.ipynb) - Jupyter Notebook to clone template content within an organization providing a new copy ready for customization
    * [`Clone_Group_Source_to_Target.ipynb`](/agol-to-agol-notebooks/Clone_Group_Source_to_Target.ipynb) - In this notebook, a group will be cloned from the source organization to a target organization. 
    * [`Configure_Target_Users.ipynb`](/agol-to-agol-notebooks/Configure_Target_Users.ipynb) - Jupyter Notebook to add users to an organization from an Excel spreadsheet. 
    * [`SampleConfig`](/agol-to-agol-notebooks/SampleConfig) - Example configuration directory
* [`agol-to-enterprise-notebooks`](/agol-to-enterprise-notebooks) - Directory with notebooks to use if the source organization is ArcGIS Online and the target is an ArcGIS Enterprise organization. 
    * [`Clone_Template_Group.ipynb`](/agol-to-agol-notebooks/Clone_Template_Group.ipynb) - Jupyter Notebook to clone template content within an organization providing a new copy ready for customization
    * [`Configure_Target_Org.ipynb`](/agol-to-agol-notebooks/Configure_Target_Org.ipynb) - In this notebook, the target organization's User Interface will be customized with banner, boackground, thumbnail images, a description, a footer, and a featured group shown on the homepage. 
    * [`Clone_Group_Source_to_Target.ipynb`](/agol-to-agol-notebooks/Clone_Group_Source_to_Target.ipynb) - In this notebook, a group will be cloned from the source organization to a target organization. 
    * [`Configure_Target_Users.ipynb`](/agol-to-agol-notebooks/Configure_Target_Users.ipynb) - Jupyter Notebook to automate adding users to an organization from an Excel spreadsheet. 
    * [`Setup_Collaboration.ipynb`](/agol-to-agol-notebooks/Setup_Collaboration.ipynb) - Jupyter Notebook to automate the creation of a collaboration between an ArcGIS Online and ArcGIS Enterprise organization. 
    * [`SampleConfig`](/agol-to-enterprise-notebooks/SampleConfig) - Example configuration directory
* [`enterprise-to-agol-notebooks`](/enterprise-to-agol-notebooks) - Directory with notebooks to use if the source and target are both ArcGIS Online organizations
    * [`Clone_Template_Group.ipynb`](/agol-to-agol-notebooks/Clone_Template_Group.ipynb) - Jupyter Notebook to clone template content within an organization providing a new copy ready for customization
    * [`Clone_Group_Source_to_Target.ipynb`](/agol-to-agol-notebooks/Clone_Group_Source_to_Target.ipynb) - In this notebook, a group will be cloned from the source organization to a target organization. 
    * [`Configure_Target_Users.ipynb`](/agol-to-agol-notebooks/Configure_Target_Users.ipynb) - Jupyter Notebook to add users to an organization from an Excel spreadsheet. 
    * [`SampleConfig`](/enterprise-to-agol-notebooks/SampleConfig) - Example configuration directory
* [`enterprise-to-enterprise-notebooks`](/enterprise-to-enterprise-notebooks) - Directory with notebooks to use if the source organization is ArcGIS Online and the target is an ArcGIS Enterprise organization. 
    * [`Clone_Template_Group.ipynb`](/agol-to-agol-notebooks/Clone_Template_Group.ipynb) - Jupyter Notebook to clone template content within an organization providing a new copy ready for customization
    * [`Configure_Target_Org.ipynb`](/agol-to-agol-notebooks/Configure_Target_Org.ipynb) - In this notebook, the target organization's User Interface will be customized with banner, boackground, thumbnail images, a description, a footer, and a featured group shown on the homepage. 
    * [`Clone_Group_Source_to_Target.ipynb`](/agol-to-agol-notebooks/Clone_Group_Source_to_Target.ipynb) - In this notebook, a group will be cloned from the source organization to a target organization. 
    * [`Configure_Target_Users.ipynb`](/agol-to-agol-notebooks/Configure_Target_Users.ipynb) - Jupyter Notebook to automate adding users to an organization from an Excel spreadsheet. 
    * [`SampleConfig`](/enterprise-to-enterprise-notebooks/SampleConfig) - Example configuration directory
* [`Resource`](/Resource) - contains diagrams of system set-ups


## Instructions

1. Download the zip or clone the repo (`$ git clone https://github.com/ArcGIS/pdo-scripts.git`)
2. Pick which version of the scripts will work for your set-up based on your source and target organization type and navigate to the correct directory using the `cd` command.
4. Open a Jupyter Notebook that has access to the arcgis (api) library (`$ jupyter notebook`)
5. Read the Readme located in the sub directory for your workflow and follow the rest of the instructions there.


## Requirements

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/) (included with [ArcGIS Python API](https://developers.arcgis.com/python/guide/install-and-set-up/#Test-your-install-with-jupyter-notebook))
* ArcGIS Online Organization for the company (project org), and at least one Organization for an end user (delivery org)
    - You must have access to both of these orgs with administrator privileges
* Before automating, we recommend deploying a few delivery organizations manually
* A template group (with materials for the delivery orgs) that lives in the company's Online Organization or Enterprise System (or both)


## Resources

* [Collaboration FAQs](https://enterprise.arcgis.com/en/portal/latest/administer/windows/common-questions-for-distributed-collaboration.htm)
* [Python Collaboration Documentation](https://developers.arcgis.com/python/guide/building-distributed-gis-through-collaborations/#Shortcut-to-establish-collaborations-in-a-single-step)
* [ArcGIS Enterprise and ArcGIS Online Collaboration Manual Steps](https://enterprise.arcgis.com/en/portal/latest/administer/windows/set-up-an-arcgis-enterprise-and-arcgis-online-collaboration.htm)
* [Key Collaboration Concepts](https://enterprise.arcgis.com/en/portal/latest/administer/windows/key-concepts.htm)
* [ArcGIS for Python API Resource Center](https://community.esri.com/groups/arcgis-python-api/)


## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.


## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).


## Licensing
Copyright 2021 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [license.txt](./license.txt) file.

