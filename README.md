# BHTP - Brothers Hobby Trading Platform
Command line interface (CLI) for Brothers Hobby Trading Platform.  

## Introduction  
Main Python project to build a fully functional command line interface (CLI) tool for Algorithmic Trading using BHTP packages as they get published.

## Standards  
Each published package will use the naming convention BHTP-package to organise algorithmic functions into autonomous packages that can be run independently from one another or used in other tools you might build.  

## How to use  
This Platform package must be installed in a python virtual environment. To run command, use a terminal window (bash, powershell, etc...)

## Installation
Clone this repo on your local machine.
Then 
1) create a virtual environment
2) activate the virtual environment
3) pip install packages (from pyproject.toml)

#### Windows installation (using py launcher)
```
py -m venv env

.\env\Scripts\activate

pip install -e .  
```  
You may wnat to upgrade the default pip in your virtual environment.  
```  
py -m pip install -U pip
```  
## Running the app  
The install process shoule have create a script command calle bhtp that can be run directly from your commande line.  

run bhtp to see the default message and syntax for help.

Run an action from the command line.  
bhtp --help
bhtp --config


