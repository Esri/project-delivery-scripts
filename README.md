# Professional Services - Project Delivery Automation Scripts

> POC scripts to help a Services Organization automate the deployment process of an ArcGIS Online Environment for Project Collaboration and Delivery

## Table of Contents

* [About](#about)
* [Prerequisites](#prerequisites-for-using-project-delivery)
* [Getting Started](#getting-started)
* [Contents](#contents)

## About
Project Delivery is a new product. It allows a Services company to purchase and manage ArcGIS Online on behalf of their endusers. [Minimum requirements for Product Delivery](/images/Project Delivery Org.PNG)

These scripts are meant to be a starting point for Services users to automate the deployment of their industry specific maps and apps to end users. They do two things:
1. Automatically customize and populate a new ArcGIS Online Organization for project delivery
2. Clone Apps, Maps, and Data into the respective organizations for Services users to do work and end users to access project updates.

Before a customer starts automating the deployment of a Project Delivery Organziation a there are some prerequisites

## Prerequisites for Using Project Delivery

### Education Prerequisites

Services Firm needs to have a firm grasp on the WebGIS Paradigm. The Services firm should be actively using WebGIS internally to deliver GIS Services to different parts of the orgnaization. Once the organization is successful internally they can begin working on finding strategies to delvivering content to their end users throughout the project lifecycle. 

### Infrastructure Prerequisites

Services Firm must have an ArcGIS Online Environment.

  If the Services Firm is using ArcGIS Enterprise they must deploy a Hybrid Environment (ArcGIS Enterprise & ArcGIS Online) to leverage the Project Delivery Organizations.

### Automation Prerequisites

__[TBD]__

### Script Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))
* Access to [Jupyter Notebooks](http://jupyter.org/) (included with ArcGIS Python API __?__ )

## Getting Started

### Jupyter Notebooks _(local)_:

1. `$ git clone https://github.com/ArcGIS/aec-scripts.git`
2. `$ cd aec-scripts`
3. `$ jupyter notebook`
4. Open `clone_groups`
5. Update GIS information and user-defined constants

### Jupyter Notebooks _(hosted)_:
1. Copy and paste [`clone_groups.ipynb`](/clone_groups.ipynb)
2. Update GIS information and user-defined constants
3. Where specified, copy and paste [`clone_utils.py`](/clone_utils.py)

### CLI -- Coming Soon

## Contents
* [`clone_groups.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to clone group contents.
* [`clone_utils.py`](/clone_utils.py) - Functions to clone groups and items


