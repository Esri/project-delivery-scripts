# AEC Project Delivery Automation Scripts

> These scripts provide a starting point for an AEC a customer to automate the deployment of their industry specific maps and apps to end users. 
> These scripts do 2 things:
> 1. The scripts automate the creation of a new ArcGIS Online Organization for Project Delivery.
> 2. Once the Project Delivery Organization exists the 2nd script will clone Apps, Maps, and Data into the respective place for the AEC firm to do work and the end user to access the status updates.

## Prerequisites

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


