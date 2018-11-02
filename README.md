# Professional Services - Project Delivery Automation Scripts

> Python scripts to help a Services Organization automate the deployment process of an ArcGIS Online Environment for Project Collaboration and Delivery

## Table of Contents

* [About](#about)
* [Prerequisites](#prerequisites-for-using-project-delivery)
* [Contents](#contents)
* [Getting Started](#getting-started)

## About
Project Delivery is a new product. It allows a Services company to purchase and manage ArcGIS Online on behalf of their endusers. [Minimum Requirements for Product Delivery Organization](Resource/Project_Delivery_Org.PNG)

These scripts are meant to be a starting point for Services users to automate the deployment of their industry specific maps and apps to end users. They do two things:
1. Automatically customize and populate a new ArcGIS Online Organization for project delivery
2. Clone Apps, Maps, and Data into the respective organizations for Services users to do work and end users to access project updates.

Before a customer starts automating the deployment of a Project Delivery Organziation a there are some prerequisites

## Prerequisites for Using Project Delivery
Is the customer Ready for this? [Product Readiness Checklist](Resource/ProjectDeliveryReadiness.pdf)

### Education Prerequisites

Services Firm needs to have a firm grasp on the WebGIS Paradigm. The Services firm should be actively using WebGIS internally to deliver GIS Services to different parts of the orgnaization. Once the organization is successful internally they can begin working on finding strategies to delvivering content to their end users throughout the project lifecycle. 

### Infrastructure Prerequisites

Services firm **Must** have **an Internal ArcGIS Online** to use Project Delivery.

#### Manual Project Delivery 
* Project Delivery Infrastucture with on **[ArcGIS Online](/Resource/ArcGISOnline_NOAutomation.PNG)**
* Project Delivery Infrastucture with on **[ArcGIS Enterprise](/Resource/ArcGISEnterprise_NOAutomation.PNG)**
  - If the Services Firm is using ArcGIS Enterprise they must deploy a Hybrid Environment (ArcGIS Enterprise & ArcGIS Online) to leverage the Project Delivery Organizations.
#### Automation Prerequisites
Before automating we always recommend a services firm to deploy a few Delivery organizations manuall

To automate the Project Delivery the services firm must have a template environment with materials (IE: Banner, Images, Thumbnails... etc) for the organizations. Services firm needs to have predefined governace and content strategies for each organziation.

* Project Delivery Automation Infrastucture with on **[ArcGIS Online](/Resource/ArcGISOnline_Automation.PNG)**
* Project Delivery Automation Infrastucture with on **[ArcGIS Enterprise](/Resource/ArcGISEnterprise_Automation.PNG)**


### Script Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/) (included with ArcGIS Python API __?__ )

## Contents
* [`clone_groups.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
* [`configure_org.ipynb`](/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`utils/`](/utils)
    * [`clone_utils.py`](/utils/clone_utils.py) - utility functions to assist with cloning groups & items
    * [`user_utils.py`](/utils/user_utils.py) - utility functions to assist with adding users

## Getting Started

### Jupyter Notebooks _(local)_:

1. `$ git clone https://github.com/ArcGIS/aec-scripts.git`
2. `$ cd aec-scripts`
3. `$ jupyter notebook`
4. Open `clone_groups.ipynb` & `build_org.ipynb`
5. Update GIS information and user-defined constants
6. Run!

### Jupyter Notebooks _(hosted)_:
1. Copy and paste [`clone_groups.ipynb`](/clone_groups.ipynb)
2. Update GIS information and user-defined constants
3. Where specified, copy and paste [`clone_utils.py`](/utils/clone_utils.py)
4. Run `clone_groups.ipynb`!
5. Repeat with [`configure_org.ipynb`](/configure_org.ipynb) but, _where specified_, copy and paste [`user_utils.py`](/utils/user_utils.py)

# aec-scripts

Project Delivery is a new product that allows a Services company to purchas and manage ArcGIS Online on behalf of their end users. ([Minimum Requirements for Product Delivery Organization](Resource/Project_Delivery_Org.PNG)) These scripts are meant to be a starting point for Services users to automate the deployment of their industry-specific maps and apps to end users. They do two things:
1. Automatically customize and populate a new ArcGIS Online Organization for project delivery
2. Clone Apps, Maps, and Data into the respective organizations for Services users to do work and end users to access project updates.

## Features
* [`clone_groups.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
* [`configure_org.ipynb`](/configure_org.ipynb) - Jupyter Notebook to customize org UI & add users
* [`utils/`](/utils)
    * [`clone_utils.py`](/utils/clone_utils.py) - utility functions to assist with cloning groups & items
    * [`user_utils.py`](/utils/user_utils.py) - utility functions to assist with adding users

## Instructions

### Jupyter Notebooks _(local)_:
1. Fork and then clone the repo (`$ git clone https://github.com/ArcGIS/aec-scripts.git`)
2. `$ cd aec-scripts`
3. Open a Jupyter Notebook (`$ jupyter notebook`)
4. Open `clone_groups.ipynb` and `build_org.ipynb`
5. Update GIS information and user-defined constants
6. Run the Notebook.

### Jupyter Notebooks _(hosted)_:
1. Copy and paste [`clone_groups.ipynb`](/clone_groups.ipynb)
2. Update GIS information and user-defined constants
3. Where specified, copy and paste [`clone_utils.py`](/utils/clone_utils.py)
4. Run `clone_groups.ipynb`.
5. Repeat with [`configure_org.ipynb`](/configure_org.ipynb) but, _where specified_, copy and paste [`user_utils.py`](/utils/user_utils.py)

## Requirements

* Meet the requirements in the [Product Readiness Checklist](Resource/ProjectDeliveryReadiness.pdf)
* The services firm needs to have a firm grasp on the WebGIS Paradigm. The Services firm should be actively using WebGIS internally to deliver GIS services to different parts of the organization. Once the organization is successful internally, they can begin working on finding strategies to deliver content to their end users throughout the project lifecycle.
* Services firms **must** have an **internal ArcGIS Online** to use Project Delivery
* Project Delivery Infrastucture with **[ArcGIS Online](/Resource/ArcGISOnline_NOAutomation.PNG)**
* Project Delivery Infrastucture with **[ArcGIS Enterprise](/Resource/ArcGISEnterprise_NOAutomation.PNG)**
    - If the Services Firm is using ArcGIS Enterprise they must deploy a Hybrid Environment (ArcGIS Enterprise & ArcGIS Online) to leverage the Project Delivery Organizations.
* Before automating, we recommend a services firm to deploy a few delivery organizations manually.
* The services firm must have a template environment with materials (i.e. banner, images, thumbnails, etc.) for the organizations. The services firm needs to have predefined governance and content strategies for each organization.
* Project Delivery Automation Infrastucture with **[ArcGIS Online](/Resource/ArcGISOnline_Automation.PNG)**
* Project Delivery Automation Infrastucture with **[ArcGIS Enterprise](/Resource/ArcGISEnterprise_Automation.PNG)**
* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/)([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/)(included with ArcGIS Python API __?__)

## Resources

* [ArcGIS for Python API Resource Center](https://community.esri.com/groups/arcgis-python-api/)
* [ArcGIS Blog](http://blogs.esri.com/esri/arcgis/)
* [twitter@esri](http://twitter.com/esri)

## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing
Copyright 2016 Esri

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
