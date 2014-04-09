'''
mesh_accessor.py - This class provides functions to access a mesh from the model.

Team Cloth
3/29/14

Last Updated: Bryant Pong: 4/6/14 - 2:01 PM
'''

# Blender API Libraries:
import bpy
import bmesh

# Unittest Unit Tests:
import unittest

# Class definition for Mesh_Accessor:
class MeshAccessor:
    
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
        
        groupIndex = -1
        print("groupIndex: " + groupIndex)
        
        '''
        First, let's loop through all the vertex groups to find the index of the
        vertex group we're interested in:
        '''
        for i in range(len(self.getModelMesh().vertex_groups)):
            if self.getModelMesh().vertex_groups[i].name == vertexGroupName:
                # We have a match!
                groupIndex = i
                break
            
        '''
        If the groupIndex is -1, then the vertexGroupName does not exist in
        this mesh; return None:
        '''
        print("groupIndex: " + str(groupIndex))
        if groupIndex == -1:
            return None
                        
        '''
        This is the list that will hold the collection of points in the specified
        vertex group:
        '''
        
        vertexGroupPoints = []
        
        # Let's now get all the points in the specified vertex group!
        for vertex in self.getModelMesh().data.vertices:
            for group in vertex.groups:
                if group.group == groupIndex:
                    vertexGroupPoints.append(vertex)
        
            
        return vertexGroupPoints