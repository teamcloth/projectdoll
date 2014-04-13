'''
mesh_utilities.py - This library contains utilities for modifying meshes.

Team Cloth
CSCI-4440
3/30/14

Last Updated: Bryant Pong: 4/13/14 - 2:55 PM
'''


# Blender and STL Libraries:
import bpy
import bmesh
import unittest


# Mesh_Utilities class definition:
class MeshUtilities:
    
    '''
    Constructor for Mesh_Utilities.  Because there are certain mesh groups
    that are often accessed, a Mesh_Utilities object will also contain a list
    of strings naming these mesh groups.
    
    The mesh lists are:
    entireBodyMesh: This mesh contains all points that allow you to manipulate
                    the entire body.
    '''
    def __init__(self):
        self.entireBodyMesh = ["DEF-stomach",
                               "DEF-head",
                               "DEF-jaw",
                               "DEF-hips",
                               "DEF-neck",
                               "DEF-spine",
                               "DEF-spine-1",
                               "DEF-chest",
                               "DEF-chest-1",
    
                                # Right muscle groups
                               "DEF-trapezius1.R",
                               "DEF-trapezius2.R",
                               "DEF-shin.01.R",
                               "DEF-shin.02.R",
                               "DEF-shin.03.R",
                               "DEF-soleus.R",
                               "DEF-scapula.R",
                               "DEF-quadriceps.R",
                               "DEF-deltoid.R",
                               "DEF-clavicle.R",
                               "DEF-eye.R",
                               "breast.R",
                               "DEF-thigh.R",
                               "DEF-femoris.R",
                               "DEF-gluteus.R",
                               "DEF-knee_fan.R",
                               "DEF-lat_dorsi.R",
                               "DEF-pectoralis.R",
    
                                # Left muscle groups
                               "DEF-shin.01.L",
                               "DEF-shin.02.L",
                               "DEF-shin.03.L",
                               "DEF-trapezius1.L",
                               "DEF-trapezius2.L",
                               "DEF-soleus.L",
                               "DEF-scapula.L",
                               "DEF-quadriceps.L",
                               "DEF-clavicle.L",
                               "DEF-deltoid.L",
                               "DEF-eye.L",
                               "breast.L",
                               "DEF-thigh.L",
                               "DEF-femoris.L",
                               "DEF-gluteus.L",
                               "DEF-knee_fan.L",
                               "DEF-lat_dorsi.L",
                               "DEF-pectoralis.L"]
                               
        self.leftTorsoSide = ["DEF-lat_dorsi.L",
                              "DEF-gluteus.L"]
                              
        self.rightTorsoSide = ["DEF-lat_dorsi.R",
                               "DEF-gluteus.R"]
                               
        self.frontTorso = ["DEF-stomach"]

    '''
    modifyMesh1D() allows a user to modify a mesh group in 1 Dimension.
    
    The arguments are:
    meshGroup: A LIST of points that designate the vertex groups to modify.
    modX, modY, modZ: FLOAT values that modify the mesh in the X, Y, Z directions
    '''
    def modifyMesh1D(self, meshGroup, modX, modY, modZ):
        
        '''
        Iterate through each vertex in the meshGroup list, modifying the
        X, Y, Z directions by the given arguments:
        '''
        for vertex in meshGroup:
            vertex.co.x += modX
            vertex.co.y += modY
            vertex.co.z += modZ
            
    '''
    modifyMesh3D() allows a user to modify a multiple mesh groups in their own
    dimensions.  For instance, when making a mesh fatter/skinnier, the left side
    needs to move in the negative X direction, the right side needs to move in 
    the positive X direction, and the front and back needs to move in the Y 
    direction.
    
    The arguments are:
    leftMeshGroup: A LIST of points that designate all vertex groups on the
                   model's LEFT-HAND side.
    rightMeshGroup: A LIST of points that designate all vertex groups on the
                    model's RIGHT-HAND side.
    frontMeshGroup: A LIST of points that designate all vertex groups on the
                    model's FRONT.
    backMeshGroup: A LIST of points that designate all vertex groups on the 
                   model's BACK.
    lMGX, lMGY, lMGZ: values to modify the leftMeshGroup in X - Y - Z
    rMGX, rMGY, rMGZ: values to modify the rightMeshGroup in X - Y - Z
    fMGX, fMGY, fMGZ: values to modify the frontMeshGroup in X - Y - Z
    bMGX, bMGY, bMGZ: values to modify the backMeshGroup in X - Y - Z
    '''
    def modifyMesh3D(leftMeshGroup, rightMeshGroup, frontMeshGroup, 
                     backMeshGroup, lMGX,           lMGY,
                     lMGZ,          rMGX,           rMGY,
                     rMGZ,          fMGX,           fMGY,
                     fMGZ,          bMGX,           bMGY,
                     bMGZ):
        for vertex in leftMeshGroup:
            vertex.co.x += lMGX
            vertex.co.y += lMGY
            vertex.co.z += lMGZ
        for vertex in rightMeshGroup:
            vertex.co.x += rMGX
            vertex.co.y += rMGY
            vertex.co.z += rMGZ    
        for vertex in frontMeshGroup:
            vertex.co.x += fMGX
            vertex.co.y += fMGY
            vertex.co.z += fMGZ
        for vertex in backMeshGroup:
            vertex.co.x += bMGX
            vertex.co.y += bMGY
            vertex.co.z += bMGZ
       
    '''
    modifyMeshSide() allows a user to modify 
    '''