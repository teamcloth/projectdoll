'''
model.py - Class definition of a Human Model.

Team Cloth
CSCI-4440
4/13/14

Last Updated: Bryant Pong: 4/23/14 - 11:49 AM
'''

# Blender API Libraries:
import bpy

# Model definition:
class Model:
    
    def __init__(self, name):
        self.height_ = 67.0
        self.width_ = 
        self.name_ = name
        
        self.mesh_groups = []
        self.name = name_
        self.width = 15.5
        self.height = 36.5
        self.mesh = bpy.context.object
        
        # Populate the mesh_groups:
        for i in range(len(self.getMesh().vertex_groups)):
            self.mesh_groups.append(self.getMesh().vertex_groups[i].name)
             
            
    # Accessor functions:
    def getHeight(self):
        return self.height_
    
    def getWidth(self):
        return self.width_
    
    def getName(self):
        return self.name_
    
    # Modifier functions:
    def setHeight(self, newHeight):
        self.height_ = newHeight
        
    def setWidth(self, newWidth):
        self.width_ = newWidth
        
    def setName(self, newName):
        self.name_ = newName