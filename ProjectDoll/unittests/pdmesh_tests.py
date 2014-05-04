'''
pdmesh_tests.py - Unittests for the PDMesh class.

Team Cloth
4/23/14

Last Updated: Bryant Pong: 4/23/14 - 1:56 PM
'''

# Python Libraries:
import bpy
import unittest
from pdmesh import *

'''
The Python Unittest Library requires that a class be made to contain all the unit tests:
'''
class PDMeshTests(unittest.TestCase):
    
    '''
    The setUp() function is always run once before EACH unit test.  For the PDMesh
    tests, we'll need one instance of a PDMesh object.  Before running this test,
    please select a mesh on the User Perspective Window to the right:
        
    For these tests, the selected model has the following properties:
    Name: Test Mesh
    Width: 67.0
    Height: 12.0
    Type: Human
    '''
    def setUp(self):
        self.mesh = PDMesh("Test Mesh", 67.0, 12.0, "Human")
        
    # Tests to verify that all accessor functions work:
    def testGetName(self):
        self.assertEqual(self.mesh.getName(), "Test Mesh")
        
    def testGetWidth(self):
        self.assertEqual(self.mesh.getWidth(), 67.0)
        
    def testGetHeight(self):
        self.assertEqual(self.mesh.getHeight(), 12.0)
        
    def testGetType(self):
        self.assertEqual(self.mesh.getType(), "Human")
        
    def testGetMesh(self):
        self.assertEqual(self.mesh.getMesh(), bpy.context.object)
        
    # Tests to verify that all modifier functions work:
    def testSetName(self):
        self.mesh.setName("New Name")
        
        # The mesh's name should now be "New Name":
        self.assertEqual(self.mesh.getName(), "New Name")
        
    def testSetWidth(self):
        self.mesh.setWidth(100)
        
        # The mesh's width should now be 100:
        self.assertEqual(self.mesh.getWidth(), 100)

# Run the unittests:
if __name__ == "__main__":
    unittest.main(exit=False)
