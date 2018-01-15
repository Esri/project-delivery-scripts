# Professional Services - Project Delivery Automation Scripts

> POC scripts to help a Services Organization automate the deployment process of an ArcGIS Online Environment for Project Collaboration and Delivery

## Table of Contents

* [About](#about)
* [Prerequisites](#prerequisites-for-using-project-delivery)
* [Getting Started](#getting-started)
* [Contents](#contents)

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
3. Where specified, copy and paste [`/utils/clone_utils.py`](/utils/clone_utils.py)
4. Run `clone_groups.ipynb`!
5. Repeat with [`build_org.ipynb`](/build_org.ipynb) but, _where specified_, copy and paste [`/utils/user_utils.py`](/utils/user_utils.py)

### CLI -- Coming Soon

## Contents
* [`clone_groups.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to clone groups and their items
* [`build_org.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to customize org UI & add users
* [`utils`](/utils)
    * [`clone_utils.py`](/utils/clone_utils.py) - utility functions to assist with cloning groups & items
    * [`user_utils.py`](/utils/user_utils.py) - utility functions to assist with adding users


