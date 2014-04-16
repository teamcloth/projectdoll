'''
cloth.py - Class to represent a piece of clothing.

Team Cloth
4/16/14

Last Updated: Bryant Pong: 4/16/14 - 3:37 PM
'''

# Import the Blender Libraries:
import bpy

class Cloth:
    
    '''
    Constructor for a Cloth object.  We need the following data fields:
    mesh_groups: a list of STRINGS that stores the names of each of the vertex groups 
                 in this model.
    name: a STRING representing the name of this clothing.
    width: a FLOAT representing the width of this clothe.
    height: a FLOAT representing the height of this clothe.
    mesh: the associated mesh with this clothe.
    '''
    def __init__(self, name_):
        self.mesh_groups = []
        self.name = name_
        self.width = 15.5
        self.height = 36.5
        self.mesh = bpy.context.object
        
    # Accessor Functions:
    def getMeshGroups(self):
        return self.mesh_groups
    
    def getMesh(self):
        return self.mesh
    
    def getName(self):
        return self.name
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    # Modifier Functions:
    def setName(self, newName):
        self.name = newName
        
    def setWidth(self, newWidth):
        self.width = newWidth
        
    def setHeight(self, newHeight):
        self.height = newHeight
        
    def setMesh(self, newMesh):
        self.mesh = newMesh
        
    