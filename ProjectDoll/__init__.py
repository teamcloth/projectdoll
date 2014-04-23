#------------------------------------------------------
# Project Doll
#
# Team Cloth
# CSCI-4440
#-----------------------------------------------------

bl_info = {
	"name":	"Project Doll",
	"author" : "Team Cloth",
	"version": (0,0,2),
	"blender": (2,6,2),
	"description": "Test clothing on model types",
    "category": "Add Mesh"
}
   
import bpy
from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       IntProperty
                       )
                       
# Cloth and Model Classes:
from cloth import *
                     
#Import the Project Doll Mesh Utilities:                       
from mesh_accessor import *
from mesh_utilities import *

from bpy_extras.io_utils import ExportHelper, ImportHelper, path_reference_mode, axis_conversion
from io_scene_obj import import_obj, export_obj
import io_import_scene_mhx

############################################################# Global Vars############################################################ 

# Global MeshAccessor Object (from mesh_accessor.py):
meshAccessor = MeshAccessor(bpy.context.object)

# Global MeshUtilities Object (from mesh_utilties.py):
meshUtilities = MeshUtilities()

# Global lists containing all registered clothing and human models:
allClothes = []
allModels = []

# Function called when model height/width is changed
def changeMesh(self, context):
    
    print("human_stable_height is " + str(context.object.human_stable_height))
    print("human_stable_width is " + str(context.object.human_stable_width))
    
    ''' 
    Let's first get the current mesh to operate on (in case the user has selected
    another mesh beforehand):
    '''
    meshAccessor.setModelMesh(bpy.context.object)
    
    '''
    We want to change the height and width of the model.  To do so, we first
    need to get the list of vertex groups (from mesh_utilities.py).
    '''
    
    # Select all groups in the entire body:
    listOfModelVertexGroups = meshUtilities.entireBodyMesh
    
    '''
    We need to change the height of the currently selected model.  To do so,
    iterate through these vertex groups, get the points corresponding to each
    vertex group, and then modify them:
    '''
    for vertexGroup in listOfModelVertexGroups:
        #print("vertexGroup is: " + str(vertexGroup))
        nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
        print("human_stable_height is: " + str(context.object.human_stable_height))
        print("human_height_inches is: " + str(context.object.human_height_inches))
        meshUtilities.modifyMesh1D(nextVertexGroup, 0, 0, 0.007 * (context.object.human_height_inches - context.object.human_stable_height))
        
    '''
    Next, let's change the width of the model:
    '''
    listOfLeftTorsoSideVertexGroups = meshUtilities.leftTorsoSide
    listOfRightTorsoSideVertexGroups = meshUtilities.rightTorsoSide
    listOfFrontTorsoVertexGroups = meshUtilities.frontTorso
   
    for vertexGroup in listOfLeftTorsoSideVertexGroups:
        nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
        meshUtilities.modifyMesh1D(nextVertexGroup, -0.007 * (context.object.human_stable_width - context.object.human_width_inches), 0, 0)
        
    for vertexGroup in listOfRightTorsoSideVertexGroups:
        nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
        meshUtilities.modifyMesh1D(nextVertexGroup, 0.007 * (context.object.human_stable_width - context.object.human_width_inches), 0, 0)
    
    for vertexGroup in listOfFrontTorsoVertexGroups:
        nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
        meshUtilities.modifyMesh1D(nextVertexGroup, 0, -0.007 * (context.object.human_stable_width - context.object.human_width_inches), 0)

    context.object.human_stable_height = context.object.human_height_inches
    context.object.human_stable_width = context.object.human_width_inches
    
    # Blender requires us to return None 
    return None

# Function to change a piece of clothing:
def changeClothingMesh(self, context):
    
    # Select the current mesh to be the clothe to modify:
    meshAccessor.setModelMesh(bpy.context.object)

    # Does the user wish to mirror the changes made to the clothe on both sides?
    if bpy.context.scene.mirror_prop == True:
        print("DEBUG ONLY - The user wishes to mirror changes!")
        
        # List of the names of vertex groups for this piece of clothing:
        listOfVertexGroups = []
        
        # Find the Cloth object in allClothes:
        for clothing in allClothes:
            if clothing.getMesh() == bpy.context.object:
                print("DEBUG ONLY - found the specified clothing object!")
                listOfVertexGroups = clothing.getMeshGroups()
                break
            
        # Tests passed
        print(listOfVertexGroups)
     
        '''
        We need to change the height of the currently selected model.  To do so,
        iterate through these vertex groups, get the points corresponding to each
        vertex group, and then modify them:
        '''
        for vertexGroup in listOfVertexGroups:
            #print("vertexGroup is: " + str(vertexGroup))
            nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
            
            print("human_stable_height is: " + str(context.object.clothing_stable_height))
            print("human_height_inches is: " + str(context.object.clothing_height_inches))
            meshUtilities.modifyMesh1D(nextVertexGroup, 0, 0, 0.007 * (context.object.clothing_height_inches - context.object.clothing_stable_height))
        
        # Next, let's change the width of the model:
        
        listOfFrontTorsoVertexGroups = ["Leg.F"]
        listOfBackTorsoVertexGroups = ["Leg.B"]
   
        for vertexGroup in listOfFrontTorsoVertexGroups:
            nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
            meshUtilities.modifyMesh1D(nextVertexGroup, 0, 0.01 * (context.object.clothing_stable_width - context.object.clothing_width_inches), 0)
        
        for vertexGroup in listOfBackTorsoVertexGroups:
            nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
            meshUtilities.modifyMesh1D(nextVertexGroup, 0, -0.01 * (context.object.clothing_stable_width - context.object.clothing_width_inches), 0)
        
        context.object.clothing_stable_height = context.object.clothing_height_inches
        context.object.clothing_stable_width = context.object.clothing_width_inches
    else:
        print("DEBUG ONLY - The user does NOT wish to mirror changes!")
        
    # Blender requires us to return None after an operator is called:
    return None
    
# Custom Properties
bpy.types.Object.human_height_inches = bpy.props.FloatProperty(name="Height", min=52, max=82)#,update=changeMesh)
bpy.types.Object.human_height_cm = bpy.props.FloatProperty(name="Height", min=52*2.5, max=82*2.5)#,update=changeMesh)
bpy.types.Object.human_width_inches = bpy.props.FloatProperty(name="Width", min=1 ,max=24)#,update=changeMesh)
bpy.types.Object.human_width_cm = bpy.props.FloatProperty(name="Width", min=2.5, max=24*2.5)#,update=changeMesh)
bpy.types.Object.human_stable_height = bpy.props.FloatProperty(name="Stable_height", default=67)#,options={'HIDDEN'}) 
bpy.types.Object.human_stable_width = bpy.props.FloatProperty(name="Stable_width", default=12.5)#,options={'HIDDEN'}) 
bpy.types.Object.clothing_height_inches = bpy.props.FloatProperty(name="Clothing Height", min=52/2.0+3, max=82/2.0+3) 
bpy.types.Object.clothing_width_inches = bpy.props.FloatProperty(name="Clothing Width", min=1+3, max=24+3)
bpy.types.Object.clothing_stable_height = bpy.props.FloatProperty(name="Clothing_stable_height", default=36.5)
bpy.types.Object.clothing_stable_width = bpy.props.FloatProperty(name="Clothing_stable_width", default=15.5)

# Scene Properties
bpy.types.Scene.mirror_prop = BoolProperty(name="Mirror Changes", description="Mirror the changes made to one side of a model", default=True)
bpy.types.Scene.is_mesh_cloth = BoolProperty(name="Clothe Mesh", description="This mesh is a clothe object", default=False)
bpy.types.Scene.is_mesh_model = BoolProperty(name="Model Mesh", description="This mesh is a model object", default=False)
bpy.types.Scene.mesh_name = StringProperty(name="Mesh Name", description="This string holds the name of the specified mesh")
############################################################## END OF GLOBALS ############################################################

# Panel on side, import export buttons
class FilePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Files"
    
    def draw(self, context):
        layout = self.layout
        
        #Export the selected model button
        col = layout.column(align = True)
        #Import a custom model/mesh
        col = layout.column(align = True)
        col.label(text="Import other model")
        row = col.row(align = True)
        row.operator("mesh.import_custom_model", text = "Clothing")
        row.operator(io_import_scene_mhx.ImportMhx.bl_idname, text = "Human")
	#end draw

# Panel on the side, allowing the user to register/deregister human models and
# Clothing models:
class RegisterPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Register/Deregister"
    
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        
        # Export the register/deregister buttons:
        col = layout.column(align=True)
        col.label(text="Register Selected Object")
        checkboxRow = col.row(align=True)
        textboxRow = col.row(align=True)
        checkboxRow.prop(scn, "is_mesh_cloth", text="Cloth Mesh")
        checkboxRow.prop(scn, "is_mesh_model", text="Model Mesh")
        textboxRow.prop(scn, "mesh_name", text="Mesh Name")
        
        col.operator("mesh.register_mesh", text = "Register Selected Object")
        
        col2 = layout.column(align = True)
        col2.label(text="Deregister Selected Object")
        col2.operator("mesh.deregister_mesh", text = "Deregister Selected Object")

#Another Panel for Human properties
class MeshPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Mesh Properties"
    
    # Properties
    bpy.types.Scene.Units = EnumProperty(
        name="Units", description="Choose One", 
        items=(('Inches', 'Inch', 'Descript1'), ('Centimeter','Cm', 'Descript2')), 
        default='Inches',
        )
               
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        #layout.prop(scn,"Units", expand=True)
        ob = context.object
        # Get the material of the object
        mat = bpy.context.object.active_material
        # Allow changing of object color
        layout.prop(mat, "diffuse_color", text="Color")
        col1 = layout.column(align=True)
        # Allow changing of human properties
        col1.label(text="Human properties")
        col1.prop(ob, "human_height_inches", slider=True)
        col1.prop(ob, "human_width_inches", slider=True)
        col1.operator("mesh.make_changes_to_human",text="Make Changes")
        # Allow changes of clothes properties
        col2 = layout.column(align=True)
        layout.prop(scn, "mirror_prop", text="Mirror Changes?")
        col2.label(text="Clothing properties")
        col2.prop(ob, "clothing_height_inches", slider=True)
        col2.prop(ob, "clothing_width_inches", slider=True)
        col2.operator("mesh.make_changes_to_clothing",text="Make Changes")

# Operator to change human model
class AlterHumanModel(bpy.types.Operator):
    bl_idname = "mesh.make_changes_to_human"
    bl_label = "Change Human"
    
    def execute(self, context):
        changeMesh(self, context)
        return {"FINISHED"}
    
# Operator to change clothing model
class AlterClothingModel(bpy.types.Operator):
    bl_idname = "mesh.make_changes_to_clothing"
    bl_label = "Change Model"
    
    def execute(self, context):
        # Tests passed!
        print("Mirror Changes is: " + str(bpy.context.scene.mirror_prop))
        changeClothingMesh(self, context)
        return {"FINISHED"}
    
# Operator to register a class:
class RegisterMesh(bpy.types.Operator):
    bl_idname = "mesh.register_mesh"
    bl_label = "Register Mesh"
    
    def execute(self, context):
        
        print("DEBUG ONLY: Now inside operator RegisterMesh")
        
        # Is this a Cloth or Model Mesh?
        if bpy.context.scene.is_mesh_cloth == True and bpy.context.scene.is_mesh_model == False:
            print("DEBUG ONLY: This is a cloth object")
            
            # Create an instance of a Cloth object and insert it into the allClothes list:
            cloth = Cloth(bpy.context.scene.mesh_name)
            allClothes.append(cloth)
        elif bpy.context.scene.is_mesh_cloth == False and bpy.context.scene.is_mesh_model == True:
            print("DEBUG ONLY: This is a model object")
            
            # Create an instance of a Model object and insert it into the allModels list:
            model = Model(bpy.context.scene.mesh_name)
            allModels.append(model)
        else:
            print("DEBUG ONLY: This is neither a cloth or a model")
            pass
        
        print("DEBUG ONLY: Now leaving operator RegisterMesh")
        return {"FINISHED"}
    
# Operator to deregister a class:
class DeregisterMesh(bpy.types.Operator):
    bl_idname = "mesh.deregister_mesh"
    bl_label = "Deregister Mesh"
    
    def execute(self, context):
        
        print("DEBUG ONLY - now deregistering mesh")
        
        # Search for the selected mesh in allClothes or allModels:
        selected_mesh = bpy.context.object
        
        
        print("DEBUG ONLY - Done deregistering mesh")
        
        return {"FINISHED"}
        
# Button to export selected model to .mhx
class ExportSelectedModel(bpy.types.Operator, ExportHelper):
    bl_idname = "mesh.export_selected_model"
    bl_label = "Exports Selected Mesh"
    
    
    filename_ext = ".obj"
    filter_glob = StringProperty(
            default="*.obj;*.mtl",
            options={'HIDDEN'},
            )

    # context group
    use_selection = BoolProperty(
            name="Selection Only",
            description="Export selected objects only",
            default=False,
            )
    use_animation = BoolProperty(
            name="Animation",
            description="Write out an OBJ for each frame",
            default=False,
            )

    # object group
    use_mesh_modifiers = BoolProperty(
            name="Apply Modifiers",
            description="Apply modifiers (preview resolution)",
            default=True,
            )

    # extra data group
    use_edges = BoolProperty(
            name="Include Edges",
            description="",
            default=True,
            )
    use_smooth_groups = BoolProperty(
            name="Smooth Groups",
            description="Write sharp edges as smooth groups",
            default=False,
            )
    use_smooth_groups_bitflags = BoolProperty(
            name="Bitflag Smooth Groups",
            description="Same as 'Smooth Groups', but generate smooth groups IDs as bitflags "
                        "(produces at most 32 different smooth groups, usually much less)",
            default=False,
            )
    use_normals = BoolProperty(
            name="Include Normals",
            description="",
            default=False,
            )
    use_uvs = BoolProperty(
            name="Include UVs",
            description="Write out the active UV coordinates",
            default=True,
            )
    use_materials = BoolProperty(
            name="Write Materials",
            description="Write out the MTL file",
            default=True,
            )
    use_triangles = BoolProperty(
            name="Triangulate Faces",
            description="Convert all faces to triangles",
            default=False,
            )
    use_nurbs = BoolProperty(
            name="Write Nurbs",
            description="Write nurbs curves as OBJ nurbs rather than "
                        "converting to geometry",
            default=False,
            )
    use_vertex_groups = BoolProperty(
            name="Polygroups",
            description="",
            default=False,
            )

    # grouping group
    use_blen_objects = BoolProperty(
            name="Objects as OBJ Objects",
            description="",
            default=True,
            )
    group_by_object = BoolProperty(
            name="Objects as OBJ Groups ",
            description="",
            default=False,
            )
    group_by_material = BoolProperty(
            name="Material Groups",
            description="",
            default=False,
            )
    keep_vertex_order = BoolProperty(
            name="Keep Vertex Order",
            description="",
            default=False,
            )

    axis_forward = EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )
    axis_up = EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )
    global_scale = FloatProperty(
            name="Scale",
            min=0.01, max=1000.0,
            default=1.0,
            )

    path_mode = path_reference_mode

    check_extension = True

    def execute(self, context):
        #from . import export_obj

        from mathutils import Matrix
        keywords = self.as_keywords(ignore=("axis_forward",
                                            "axis_up",
                                            "global_scale",
                                            "check_existing",
                                            "filter_glob",
                                            ))

        global_matrix = (Matrix.Scale(self.global_scale, 4) *
                         axis_conversion(to_forward=self.axis_forward,
                                         to_up=self.axis_up,
                                         ).to_4x4())

        keywords["global_matrix"] = global_matrix
        return export_obj.save(self, context, **keywords)


#Button to import exported model             
class ImportCustomModel(bpy.types.Operator, ImportHelper):
    
    bl_idname = "mesh.import_custom_model"
    bl_label = "Import Custom Model"
    bl_options = {'PRESET', 'UNDO'}
    
    filename_ext = ".obj"
    filter_glob = StringProperty(
            default="*.obj;*.mtl",
            options={'HIDDEN'},
            )

    use_ngons = BoolProperty(
            name="NGons",
            description="Import faces with more than 4 verts as ngons",
            default=True,
            )
    use_edges = BoolProperty(
            name="Lines",
            description="Import lines and faces with 2 verts as edge",
            default=True,
            )
    use_smooth_groups = BoolProperty(
            name="Smooth Groups",
            description="Surround smooth groups by sharp edges",
            default=True,
            )

    use_split_objects = BoolProperty(
            name="Object",
            description="Import OBJ Objects into Blender Objects",
            default=True,
            )
    use_split_groups = BoolProperty(
            name="Group",
            description="Import OBJ Groups into Blender Objects",
            default=True,
            )

    use_groups_as_vgroups = BoolProperty(
            name="Poly Groups",
            description="Import OBJ groups as vertex groups",
            default=False,
            )

    use_image_search = BoolProperty(
            name="Image Search",
            description="Search subdirs for any associated images "
                        "(Warning, may be slow)",
            default=True,
            )

    split_mode = EnumProperty(
            name="Split",
            items=(('ON', "Split", "Split geometry, omits unused verts"),
                   ('OFF', "Keep Vert Order", "Keep vertex order from file"),
                   ),
            )

    global_clamp_size = FloatProperty(
            name="Clamp Size",
            description="Clamp bounds under this value (zero to disable)",
            min=0.0, max=1000.0,
            soft_min=0.0, soft_max=1000.0,
            default=0.0,
            )
    axis_forward = EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )

    axis_up = EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )
    
    def execute(self, context):
        # print("Selected: " + context.active_object.name)    
        if self.split_mode == 'OFF':
            self.use_split_objects = False
            self.use_split_groups = False
        else:
            self.use_groups_as_vgroups = False

        keywords = self.as_keywords(ignore=("axis_forward",
                                            "axis_up",
                                            "filter_glob",
                                            "split_mode",
                                            ))

        global_matrix = axis_conversion(from_forward=self.axis_forward,
                                        from_up=self.axis_up,
                                        ).to_4x4()
        keywords["global_matrix"] = global_matrix

        if bpy.data.is_saved and context.user_preferences.filepaths.use_relative_paths:
            import os
            keywords["relpath"] = os.path.dirname((bpy.data.path_resolve("filepath", False).as_bytes()))

        return import_obj.load(self, context, **keywords)

# register our classes into blender
def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(FilePanel)
    bpy.types.INFO_MT_file_import.append(RegisterPanel)
    bpy.types.INFO_MT_file_import.append(MeshPanel)
    

def unregister():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(FilePanel)
    bpy.types.INFO_MT_file_import.append(RegisterPanel)
    bpy.types.INFO_MT_file_import.append(MeshPanel)
    
    
if __name__ == "__main__":
    register()

