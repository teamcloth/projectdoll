#!/usr/bin/python

'''
install.py - Python script to install Project doll into a new user's directory.

Team Cloth
4/30/14

Last Updated: 5/4/14 - 1:48 PM
'''
import os
import shutil

# Main function:
def main():

	# Get the path to Blender:
	blenderPath = str(input("Please enter the path to Blender: "))
	blenderPath += "/2.69/scripts/"
	
	'''
	We need the following path variables to move the Project Doll files:
	
	currentDirectory: Current directory. 
	blenderAddons: Directory that holds the __init__.py file.
	blenderModules: Directory that holds the files in "Modules".
	'''

	currentDirectory = os.getcwd()
	blenderAddons = blenderPath + "addons/"
	blenderModules = blenderPath + "modules/"

	# Does the ProjectDoll directory exist in blenderAddons?     	
	if not os.path.exists(blenderAddons + "ProjectDoll"):
		os.makedirs(blenderAddons + "ProjectDoll")

	# Copy __init__.py into the "ProjectDoll" directory in addons:
	initFilePath = currentDirectory + "/__init__.py"
	shutil.copy(initFilePath, blenderAddons + "ProjectDoll")

	# Copy all files in the modules directory:
	modulesDirectory = currentDirectory + "/modules"
	
	# Get all files in the modulesDirectory:
	modulesFiles = os.listdir(modulesDirectory)

	for nextFile in modulesFiles:
		fullFileName = currentDirectory + "/modules/" + nextFile
		shutil.copy(fullFileName, blenderModules)	 
	  	
	print("Done installing Project Doll!")

# Run the installation script:
if __name__ == "__main__":
	main()   
