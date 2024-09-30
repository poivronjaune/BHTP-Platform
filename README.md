# BHTP - Brothers Hobby Trading Platform
Command line interface (CLI) for Brothers Hobby Trading Platform.  

## Introduction  
Main Python project to build a fully functional command line interface (CLI) tool for Algorithmic Trading using BHTP packages as they get published.

## Standards  
Each published package will use the naming convention BHTP-package to organise algorithmic functions into autonomous packages that can be run independently from one another or used in other tools you might build.  

## How to use  
This Platform package should be installed in a python virtual environment.  
To run commands, use a terminal window (bash, powershell, etc...)  

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
The install process should have created a script command called bhtp that can be run directly from your commande line without using the python launcher.  

run bhtp to check if the default message is displayed.
```  
bhtp
```  
Expected response
```  
BHTP-CLI: Brothers Hobby Trading Platform, 'bhtp --help' for commands
```  
## Launching actions  
From the command line use the bhtp program to launch actiosn directly from your terminal  

#### Switch:  
bhtp --help  : use the -- option to activate a switch 

#### Command
bhtp config  : use the command name to execute actions

## Detailed documentation  
Read the Docs site commig in 2025...