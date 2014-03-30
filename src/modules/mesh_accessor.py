'''
mesh_accessor.py - This class provides functions to access a mesh from the model.

Team Cloth
3/29/14

Last Updated: Bryant Pong: 3/30/14 - 1:02 AM
'''

# Blender API Libraries:
import bpy
import bmesh

# Unittest Unit Tests:
import unittest

# Class definition for Mesh_Accessor:
class Mesh_Accessor:
    
    ''' 
    Mesh_Accessor constructor.  We need to pass in the actual model that will be
    modified.  The model is of type "MESH" (bpy.data.object).
    '''
    def __init__(self, modelMeshIn):
        '''
        Instance variables:
        modelMesh: This is the model mesh to modify.
        currentVertexGroup: This is the current vertex group to modify.
        '''
        self.modelMesh = modelMeshIn
        self.currentVertexGroup = None
        
    ''' 
    Accessor and Modifying Functions.
    '''
    def getModelMesh(self):
        return self.modelMesh
    
    def getCurrentVertexGroup(self):
        return self.currentVertexGroup
    
    def setModelMesh(self, newModelMesh):
        self.modelMesh = newModelMesh
        
    def setCurrentVertexGroup(self, newVertexGroup):
        self.currentVertexGroup = newVertexGroup
        
    '''
    This is the main function for the Mesh_Accessor class: 
    getVertexGroupPoints().  This function takes in a STRING argument that specifies
    the name of the vertex group to examine.  The return value will be a LIST that 
    contains all the points in the vertex group.
    '''
    def getVertexGroupPoints(self, vertexGroupName):
        
        '''
        First, let's loop through all the vertex groups to find the index of the
        vertex group we're interested in:
        '''
        for i in range(len(self.getModelMesh().vertex_groups)):
            if self.getModelMesh().vertex_groups[i].name == vertexGroupName:
                # We have a match!
                groupIndex = i
                break
            
        print("groupIndex is " + str(groupIndex))
        
        '''
        This is the list that will hold the collection of points in the specified
        vertex group:
        '''
        vertexGroupPoints = []
        
        '''
        Let's now get all the points in the specified vertex group!
        '''
        for vertex in self.getModelMesh().data.vertices:
            for group in vertex.groups:
                if group.group == groupIndex:
                    vertexGroupPoints.append(vertex)
        
        for vertex in vertexGroupPoints:
            vertex.co.z += 0.01
            
        return vertexGroupPoints
            
def main():
    x = Mesh_Accessor(bpy.context.object)
    x.getVertexGroupPoints("DEF-stomach")
    x.getVertexGroupPoints("DEF-head")
    x.getVertexGroupPoints("DEF-jaw")
    x.getVertexGroupPoints("DEF-hips")
    x.getVertexGroupPoints("DEF-neck")
    x.getVertexGroupPoints("DEF-spine")
    x.getVertexGroupPoints("DEF-spine-1")
    x.getVertexGroupPoints("DEF-chest")
    x.getVertexGroupPoints("DEF-chest-1")
    
    # Right muscle groups
    x.getVertexGroupPoints("DEF-trapezius1.R")
    x.getVertexGroupPoints("DEF-trapezius2.R")
    x.getVertexGroupPoints("DEF-shin.01.R")
    x.getVertexGroupPoints("DEF-shin.02.R")
    x.getVertexGroupPoints("DEF-shin.03.R")
    x.getVertexGroupPoints("DEF-soleus.R")
    x.getVertexGroupPoints("DEF-scapula.R")
    x.getVertexGroupPoints("DEF-quadriceps.R")
    x.getVertexGroupPoints("DEF-deltoid.R")
    x.getVertexGroupPoints("DEF-clavicle.R")
    x.getVertexGroupPoints("DEF-eye.R")
    x.getVertexGroupPoints("breast.R")
    x.getVertexGroupPoints("DEF-thigh.R")
    x.getVertexGroupPoints("DEF-femoris.R")
    x.getVertexGroupPoints("DEF-gluteus.R")
    x.getVertexGroupPoints("DEF-knee_fan.R")
    x.getVertexGroupPoints("DEF-lat_dorsi.R")
    x.getVertexGroupPoints("DEF-pectoralis.R")
    
    # Left muscle groups
    x.getVertexGroupPoints("DEF-shin.01.L")
    x.getVertexGroupPoints("DEF-shin.02.L")
    x.getVertexGroupPoints("DEF-shin.03.L")
    x.getVertexGroupPoints("DEF-trapezius1.L")
    x.getVertexGroupPoints("DEF-trapezius2.L")
    x.getVertexGroupPoints("DEF-soleus.L")
    x.getVertexGroupPoints("DEF-scapula.L")
    x.getVertexGroupPoints("DEF-quadriceps.L")
    x.getVertexGroupPoints("DEF-clavicle.L")
    x.getVertexGroupPoints("DEF-deltoid.L")
    x.getVertexGroupPoints("DEF-eye.L")
    x.getVertexGroupPoints("breast.L")
    x.getVertexGroupPoints("DEF-thigh.L")
    x.getVertexGroupPoints("DEF-femoris.L")
    x.getVertexGroupPoints("DEF-gluteus.L")
    x.getVertexGroupPoints("DEF-knee_fan.L")
    x.getVertexGroupPoints("DEF-lat_dorsi.L")
    x.getVertexGroupPoints("DEF-pectoralis.L")
    
    
if __name__ == '__main__':
    main()