#!/usr/bin/python

'''
install.py - Python script to install Project doll into a new user's directory.

Team Cloth
4/30/13

Last Updated: 4/30/13 - 2:48 PM
'''
import os
import shutil

# Main function:
def main():

	# Get the path to Blender:
	blenderPath = str(raw_input("Please enter the path to Blender: "))
	blenderPath += "/2.69/scripts/"
	print("DEBUG ONLY - blenderPath is: " + blenderPath) 
	
	'''
	We need the following path variables to move the Project Doll files:
	
	currentDirectory: Current directory. 
	blenderAddons: Directory that holds the __init__.py file.
	blenderModules: Directory that holds the files in "Modules".
	'''

	currentDirectory = os.getcwd()
	blenderAddons = blenderPath + "addons/"
	blenderModules = blenderPath + "modules/"

	print("DEBUG ONLY - currentDirectory: " + currentDirectory)
	print("DEBUG ONLY - blenderAddons: " + blenderAddons)
	print("DEBUG ONLY - blenderModules: " + blenderModules)

	# Does the ProjectDoll directory exist in blenderAddons?     	
	if not os.path.exists(blenderAddons + "ProjectDoll"):
		print("DEBUG ONLY - ProjectDoll does not exist in blenderAddons")
		os.makedirs(blenderAddons + "ProjectDoll")
	else:
		print("DEBUG ONLY - ProjectDoll exists in blenderAddons")

	# Copy __init__.py into the "ProjectDoll" directory in addons:
	initFilePath = currentDirectory + "/__init__.py"
	print("DEBUG ONLY - initFilePath is: " + initFilePath)
	shutil.copy(initFilePath, blenderAddons + "ProjectDoll")

	# Copy all files in the modules directory:
	modulesDirectory = currentDirectory + "/modules"
	print("DEBUG ONLY - modulesDirectory is: " + modulesDirectory)	 
	
	# Get all files in the modulesDirectory:
	modulesFiles = os.listdir(modulesDirectory)
	print(modulesFiles)

	for nextFile in modulesFiles:
		fullFileName = currentDirectory + "/modules/" + nextFile
		shutil.copy(fullFileName, blenderModules)	 
	  	

# Run the installation script:
if __name__ == "__main__":
	main()   
