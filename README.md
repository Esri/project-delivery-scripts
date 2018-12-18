# Project-Delivery Organization Scripts

Project Delivery allows a Services company (the project organization) to purchase and manage ArcGIS Online on behalf of their end users (the delivery organizations). These scripts are meant to be a starting point for Services users to automate the deployment of their industry-specific maps and apps to end users. They do two things:
1. Automatically customize and populate a new ArcGIS Online Organization for project delivery
2. Clone Apps, Maps, and Data into the respective organizations for Services users to do work and end users to access project updates.


There are two versions:
1. Enterprise Scripts: use the scripts in this folder if the company has ArcGIS Enterprise and an ArcGIS Online Organization and they want to use both to share content with the end users. The Online Org and the Portal will both have a group that can be empty or contain template items that they want to deploy to end users.
2. ArcGIS Online Only Scripts: use the scripts in this folder if the company just has an ArcGIS Online Organziation that they want to use to share content with their end users. The company's ArcGIS Online Organization will have a template group or groups containing items that they want to deploy to end users.


## Features
* [`enterprise-scripts`](/enterprise-scipts) - scripts to use if you have enterprise
    * [`setup_collaboration.ipynb`](/enterprise-scripts/setup_collaboration.ipynb) - Jupyter Notebook to create enterprise and Online collaboration
    * [`clone_groups.ipynb`](/enterprise-scripts/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
    * [`configure_org.ipynb`](/enterprise-scripts/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`agol-only-scripts`](/agol-only-scripts) - scripts to use if you have ArcGIS Online only
    * [`clone_groups.ipynb`](/agol-only-scripts/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
    * [`configure_org.ipynb`](/agol-only-scripts/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`Sample Config`](/Sample_Config) - contains samples of files used in configure_org.ipynb

## Instructions

1. Download the zip or clone the repo (`$ git clone https://github.com/ArcGIS/pdo-scripts.git`)
2. Pick which version of the scripts will work for your set-up (Enterprise or Online)
3. Nativate to the correct folder `$ cd pdo-scripts/enterprise-scripts` or `$ cd pdo-scripts/agol-online-only`
4. Open a Jupyter Notebook that has access to the arcgis (api) library (`$ jupyter notebook`)
5. Read the Readme located in the enterprise or arcigs online only folder and follow the rest of the instructions there.


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
Copyright 2018 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [license.txt]( https://raw.github.com/Esri/aec-scripts/master/license.txt) file.

[](Esri Tags: ArcGIS Project Delivery Automation Scripts)
[](Esri Language: Python)​
