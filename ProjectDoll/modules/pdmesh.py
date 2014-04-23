'''
pdmesh.py - Class to represent a piece of clothing or a human model.

Team Cloth
4/23/14

Last Updated: Bryant Pong: 4/23/14 - 1:54 PM
'''

# Import the Blender Libraries:
import bpy

class PDMesh:
    
    '''
    Constructor for a PDMesh object.  We need the following data fields:
    mesh_groups_: a list of STRINGS that stores the names of each of the vertex groups 
                 in this model.
    name_: a STRING representing the name of this mesh.
    width_: a FLOAT representing the width of this mesh.
    height_: a FLOAT representing the height of this mesh.
    mesh_: the associated mesh with this mesh.
    type_: a STRING representing the type of this mesh.
    '''
    def __init__(self, name, width, height, type):
        self.mesh_groups_ = []
        self.name_ = name
        self.width_ = width
        self.height_ = height
        self.mesh_ = bpy.context.object
        self.type_ = type
        
        # Populate the mesh_groups:
        for i in range(len(self.getMesh().vertex_groups)):
            self.mesh_groups_.append(self.getMesh().vertex_groups[i].name)
             
    # Accessor Functions:
    def getMeshGroups(self):
        return self.mesh_groups_
    
    def getMesh(self):
        return self.mesh_
    
    def getName(self):
        return self.name_
    
    def getWidth(self):
        return self.width_
    
    def getHeight(self):
        return self.height_
    
    def getType(self):
        return self.type_
    
    # Modifier Functions:
    def setName(self, newName):
        self.name_ = newName
        
    def setWidth(self, newWidth):
        self.width_ = newWidth
        
    def setHeight(self, newHeight):
        self.height_ = newHeight
        
    def setMesh(self, newMesh):
        self.mesh_ = newMesh
        
    def setType(self, newType):
        self.type_ = newType
        
    