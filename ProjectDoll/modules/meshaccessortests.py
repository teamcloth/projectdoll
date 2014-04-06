'''
meshaccessortests.py - Unit Tests for the Mesh Accessor class (found in
mesh_accessor.py).

Team Cloth
4/6/14

Last Written: Bryant Pong: 4/6/14 - 2:12 PM
'''

# Import the Blender Library:
import bpy

# Import the mesh_accessor class:
from mesh_accessor import *

# Import the Unittest Library:
import unittest

'''
The Python Unit Test library requires that a class be made containing
all the test implementations:
'''
class MeshAccessorTests(unittest.TestCase):
    
    '''
    The setUp() function is always run before EACH tests.  This ensures that
    a fresh set of instance variables will be used for each test.
    
    For the MeshAccessor tests, we only require 1 instance variable:
    the Mesh_Accessor object itself.  Before running this test, you will need
    to spawn a Make Human male model and select it.
    '''
    def setUp(self):
       self.meshAccessor = MeshAccessor(bpy.context.object) 
       
    ''' 
    Test to verify that the currently seelected model's name is
    'male_modelBody':
    '''
    def testSelectedMeshName(self):
        selectedMeshName = self.meshAccessor.getModelMesh().name
        self.assertEqual(selectedMeshName, 'male_modelBody')
        
    
    # Test to verify that the currently selected vertex group is None:
    def testSelectedVertexGroup(self):
        selectedVertexGroup = self.meshAccessor.getCurrentVertexGroup()
        self.assertEqual(selectedVertexGroup, None)
        
    # Test to verify that a non-existant vertex group returns not None:
    def testVertexGroup(self):
        pointCloud = self.meshAccessor.getVertexGroupPoints("DEF-hand.L")
        self.assertEqual(len(pointCloud), 190)
        
    
    
# Run the Unit Tests, preventing the unittest library from closing Blender:
if __name__ == '__main__':
    unittest.main(exit=False)