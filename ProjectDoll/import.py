'''
import.py - Blender Operator to allow a user to import Make Human models for the
Project Doll addon.

Team Cloth
3/19/14

Last Updated: Bryant Pong 3/19/14 - 3:18 PM
'''

# Import the Blender API Library:
import bpy

# Import the Blender 
from bpy_extras.io_utils import ExportHelper

# ImportOperator is the actual class that imports in the model:
class ImportOperator(bpy.types.Operator, ExportHelper):
    
    # Set the ID and label for the Import Operator:
    bl_idname = "object.import_operator"
    bl_label = "Import Meshes"
    
    filename_ext = ".fmt"
    
    # execute() is called when ImportOperator triggers:
    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}
    
# This function formally registers the Import operator with Blender:
def register():
    bpy.utils.register_class(ImportOperator)
    
# Remove the ImportOperator from Blender:
def unregister():
    bpy.utils.unregister_class(ImportOperator)
    
if __name__ == "__main__":
    register()
    bpy.ops.object.import_operator()
    