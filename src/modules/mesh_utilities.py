'''
mesh_utilities.py - This library contains utilities for modifying meshes.

Team Cloth
CSCI-4440
3/30/14

Last Updated: Bryant Pong: 4/1/14 - 6:05 PM
'''

'''
Blender and STL Libraries:
'''
import bpy
import bmesh
import unittest

'''
Mesh_Utilities class definition:
'''
class Mesh_Utilities:
    
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

    '''
    modifyMesh() allows a user to modify a mesh group.
    
    The arguments are:
    meshGroup: A LIST of points that designate the vertex groups to modify.
    modX, modY, modZ: FLOAT values that modify the mesh in the X, Y, Z directions
    '''
    def modifyMesh(self, meshGroup, modX, modY, modZ):
        
        '''
        Iterate through each vertex in the meshGroup list, modifying the
        X, Y, Z directions by the given arguments:
        '''
        for vertex in meshGroup:
            vertex.co.x += modX
            vertex.co.y += modY
            vertex.co.z += modZ
   
''' 
runUnitTests() runs unit tests for this module.
'''
def runUnitTests():
    print("Now running Unit Tests for Mesh_Utilities:")
            
'''
To run unit for this module, just click "Run Script".
'''
if __name__ == '__main__':
    runUnitTests()