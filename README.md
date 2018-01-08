# AEC Project Delivery Automation Scripts

> POC scripts to automatically deploy the AEC project structure 

## About

These scripts are meant to be a starting point for AEC users to automate the deployment of their industry specific maps and apps to end users. They do two things:
1. Automatically customize and populate a new ArcGIS Online Organization for project delivery
2. Clone Apps, Maps, and Data into the respective organizations for AEC users to do work and end users to access project updates.

## Script Prerequisites

* Install the [ArcGIS API for Python](https://developers.arcgis.com/python/) ([instructions](https://developers.arcgis.com/python/guide/install-and-set-up/))

* Access to [Jupyter Notebooks](http://jupyter.org/) (included with ArcGIS Python API __?__ )

## Getting Started

#### Jupyter Notebooks _(local)_:

1. `$ git clone https://github.com/ArcGIS/aec-scripts.git`
2. `$ cd aec-scripts`
3. `$ jupyter notebook`
4. Open `clone_groups`
5. Update GIS information and user-defined constants

#### Jupyter Notebooks _(hosted)_:
1. Copy and paste [`clone_groups.ipynb`](/clone_groups.ipynb)
2. Update GIS information and user-defined constants
3. Where specified, copy and paste [`clone_utils.py`](/clone_utils.py)

#### CLI -- Coming Soon

## Contents
* [`clone_groups.ipynb`](/clone_groups.ipynb) - Jupyter Notebook to clone group contents.
* [`clone_utils.py`](/clone_utils.py) - Functions to clone groups and items


