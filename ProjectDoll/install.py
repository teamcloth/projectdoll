#!/usr/bin/python

'''
install.py - Python script to install Project doll into a new user's directory.

Team Cloth
4/30/13

Last Updated: 4/30/13 - 2:15 PM
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
	
	blenderAddons: Directory that holds the __init__.py file.
	blenderModules: Directory that holds the files in "Modules".
	'''

	blenderAddons = blenderPath + "addons/"
	blenderModules = blenderPath + "modules/"

	print("DEBUG ONLY - blenderAddons: " + blenderAddons)
	print("DEBUG ONLY - blenderModules: " + blenderModules)

	# Does the ProjectDoll directory exist in blenderAddons?     	
	if not os.path.exists(blenderAddons + "ProjectDoll"):
		print("DEBUG ONLY - ProjectDoll does not exist in blenderAddons")
		os.makedirs(blenderAddons + "ProjectDoll")
	else:
		print("DEBUG ONLY - ProjectDoll exists in blenderAddons")

# Run the installation script:
if __name__ == "__main__":
	main()   
