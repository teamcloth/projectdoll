'''
ProjectDoll.py - Main Entry code for Project Doll.

Team Cloth
CSCI-4440
3/27/14

Last Edited: Bryant Pong - 3/30/14 - 3:00 PM
'''

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import *
from mesh_accessor import *
import bmesh
import unittest


# Global Mesh Accessor Object (from mesh_accessor.py):
x = Mesh_Accessor(bpy.context.object)

# Placeholder properties
bpy.types.Object.cProp = bpy.props.IntProperty( name = "Number", min = 0, max = 10, default = 5)
bpy.types.Object.human_height_inches = bpy.props.IntProperty( name = "Height", min = 12, max = 96, default=67)
bpy.types.Object.human_height_cm = bpy.props.IntProperty( name = "Height", min = 30, max = 250, default=150)
bpy.types.Object.human_width_inches = bpy.props.IntProperty( name = "Width", min = 30, max = 250, default=150)
bpy.types.Object.human_width_cm = bpy.props.IntProperty( name = "Width", min = 30, max = 250, default=150)
       
class AlterHumanModel(bpy.types.Operator):
    bl_idname = "mesh.make_changes_to_human"
    bl_label = "Change Human"
    
    #Implementation here
    def execute(self, context):
        
        print("human_height_inches: " + str(bpy.context.object.human_height_inches))
        print("human_width_inches: " + str(bpy.context.object.human_width_inches))
        
        
        
        return {'FINISHED'}
            
#Button to import exported model             
class ImportCustomModel(bpy.types.Operator):
    bl_idname = "mesh.import_custom_model"
    bl_label = "Import Custom Model"
    
    #Implement here
    
#Button to bring in default model
class ImportDefaultModel(bpy.types.Operator):
    bl_idname = "mesh.import_default_model"
    bl_label = "Import Default Model"
    

#Button to export selected model
class ExportSelectedModel(bpy.types.Operator, ExportHelper):
    bl_idname = "mesh.export_selected_model"
    bl_label = "Exports Selected Mesh"
    
    filename_ext = ".obj"
    #Code based off MakeHuman ml_plugins/exportobj.py
    def execute(self, context):
        #Get active mesh
        bpy.ops.object.mode_set(mode = 'EDIT')
        obj = bpy.context.active_object
        dat = obj.data
        
        #Get bmesh
        bm = bmesh.from_edit_mesh(dat)
        #me = bm.data
        return {"FINISHED"}

def register():
    bpy.utils.register_class(ImportDefaultModel)
    bpy.utils.register_class(ExportSelectedModel)
    bpy.utils.register_class(ImportCustomModel)
    bpy.utils.register_class(AlterHumanModel)    

def unregister():
    bpy.unregister_class(ImportDefaultModel)
    bpy.unregister_class(ExportSelectedModel)
    bpy.unregister_class(ImportCustomModel)
    bpy.unregister_class(AlterHumanModel)

if __name__ == "__main__":
	register()	
