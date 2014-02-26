'''
main.py - The entry point to running Project Doll

Written By:
Bryant Pong
2/26/14

Last Updated - Bryant Pong, 2/16/14 - 12:46 PM
'''

# Blender's Python API:
import bpy   

# Main function.  This calls all the other ProjectDoll classes:
def main(context):
    for ob in context.scene.objects:
        print(ob)

# ProjectDollOperator class to start up all the ProjectDoll utilities:
class ProjectDollOperator(bpy.types.Operator):
    # Provide Descriptions of what does Blender Add-on does:
    bl_idname = "object.project_doll_operator"
    bl_label = "Project Doll Tools"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
# register() registers the Project Doll Add-on in the Blender's add-on catalog:
def register():
    bpy.utils.register_class(ProjectDollOperator)
    
# unregister() removes the Project Doll Add-on from Blender's add-on catalog:
def unregister():
    bpy.utils.unregister_class(ProjectDollOperator)

# When this script is loaded, load all the Project Doll features:
if __name__ == '__main__':
    register()
    bpy.ops.object.project_doll_operator()



