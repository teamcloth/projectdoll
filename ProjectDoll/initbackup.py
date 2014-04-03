#------------------------------------------------------
# Project Doll
#-----------------------------------------------------

bl_info = {
	"name":	"Project Doll",
	"author" : "Team Cloth",
	"version": (0,0,1),
	"blender": (2,6,2),
	"description": "Test clothing on model types",
    "category": "Add Mesh"
}

# Supporting reloading the add-on

#if "bpy" in locals():
  #import imp
  #imp.reload(ProjectDolltest)
  #imp.reload()
#else:
    #from . import ProjectDolltest
    
import bpy
from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       IntProperty
                       )
 Import the Project Doll Mesh Utilities:                       
from mesh_accessor import *
from mesh_utilities import *

from bpy_extras.io_utils import ExportHelper, ImportHelper, path_reference_mode, axis_conversion
from io_scene_obj import import_obj , export_obj
import io_import_scene_mhx

############################################################# Global Vars############################################################ 

# Global MeshAccessor Object (from mesh_accessor.py):
meshAccessor = MeshAccessor(bpy.context.object)

# Global MeshUtilities Object (from mesh_utilties.py):
meshUtilities = MeshUtilities()

# Function called when model height/width is changed
def changeMesh(self, context):
    # Call the mesh alter function passing Human_height_cm
    #mesh_utilities.modifyMesh1D(context, context.object.human_height_inches, context.object.human_width_inches)
    # Change human_height_cm afterwards to Human_height_inch 
    
    
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
    
    for vertexGroup in listOfFrontTorsoSideVertexGroups:
        nextVertexGroup = meshAccessor.getVertexGroupPoints(vertexGroup)
        meshUtilities.modifyMesh1D(nextVertexGroup, 0, -0.007 * (context.object.human_stable_width - context.object.human_width_inches), 0)
            

    context.object.human_stable_height = context.object.human_height_inches
    context.object.human_stable_width = context.object.human_width_inches
    
    # Blender requires us to return None 
    return None
    ''' # For use when unit conversion is finished being implemented
    if context.scene.Units == "Inches":
        #print("Changing inches")
        # Call the mesh alter function passing Human_height_cm
        #mesh_utilities.modifyMesh1D(context, context.object.human_height_inches, context.object.human_width_inches)
        # Change human_height_cm afterwards to Human_height_inch 
        context.object.human_stable_height = context.object.human_height_inches
        context.object.human_stable_width = context.object.human_width_inches
        return 0
    
    elif context.scene.Units == 'Centimeter': # Cm
        print("Changing cm")
        #mesh_utilities.modifyMesh1D(context, context.object.human_height_cm / 2.5, context.object.human_width_cm / 2.5)
        context.object.human_stable_height = context.object.human_height_cm / 2.5
        context.object.human_stable_width = context.object.human_width_cm / 2.5
        return 0
    '''
#Custom properties
bpy.types.Object.human_height_inches = bpy.props.FloatProperty( name = "Height", min = 52, max = 82,update=changeMesh)
bpy.types.Object.human_height_cm = bpy.props.FloatProperty( name = "Height", min = 52*2.5, max = 82*2.5,update=changeMesh)
bpy.types.Object.human_width_inches = bpy.props.FloatProperty( name = "Width", min =1 , max = 24,update=changeMesh)
bpy.types.Object.human_width_cm = bpy.props.FloatProperty( name = "Width", min = 2.5, max= 24*2.5,update=changeMesh)
bpy.types.Object.human_stable_height = bpy.props.FloatProperty( name= "Stable_height",default=67,options={'HIDDEN'}) 
bpy.types.Object.human_stable_width = bpy.props.FloatProperty( name= "Stable_width",default=12.5,options={'HIDDEN'}) 

############################################################## END OF GLOBALS ############################################################

# Panel on side, inport export buttons
class FilePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Files"
    
    def draw(self, context):
        layout = self.layout
        
        #Import default model buttons (m/f are the same for now)
        #col = layout.column(align = True)
        #col.label(text="Import Default models")
        #row = col.row(align = True)
        #row.operator("mesh.import_default_model", text = "Male")
        #row.operator("mesh.import_default_model", text = "Female")
        
        #Export the selected model button
        col = layout.column(align = True)
        #col.label(text="Export selected mesh")
        #row = col.row(align = True)
        #row.operator(export_obj.ExportOBJ.bl_idname, text="Export Selected Model")
        
        #Import a custom model/mesh
        col = layout.column(align = True)
        col.label(text="Import other model")
        row = col.row(align = True)
        #row.operator(import_obj.ImportOBJ.bl_name, text = "Import Clothing obj")
        row.operator("mesh.import_custom_model", text = "Clothing")
        row.operator(io_import_scene_mhx.ImportMhx.bl_idname, text = "Human")
	#end draw


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
        #Customization of model height and width, updates automatically in changeMesh()
        ''' DEBUGGING INCH -> CM CONVERSION
        if bpy.context.scene.Units == 'Inches':
            context.object.human_height_inches = context.object.human_stable_height 
            context.object.human_width_inches = context.object.human_stable_width
            layout.prop(ob, "human_height_inches", slider=True)
            layout.prop(ob, "human_width_inches", slider=True)
        elif bpy.context.scene.Units == 'Centimeter':
            context.object.human_height_inches = context.object.human_stable_height 
            context.object.human_width_inches = context.object.human_stable_width
            layout.prop(ob, "human_height_cm", slider=True)
            layout.prop(ob, "human_width_cm", slider=True)
        '''
        # Inch measurement
        #context.object.human_height_inches = context.object.human_stable_height 
        #context.object.human_width_inches = context.object.human_stable_width
        layout.prop(ob, "human_height_inches", slider=True)
        layout.prop(ob, "human_width_inches", slider=True)
        # Get the material of the object
        mat = bpy.context.object.active_material
        # Allow changing of object color
        layout.prop(mat, "diffuse_color", text="Color")
'''        
#Another Panel for Human properties
class ClothingPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Clothing Properties"
       
    def draw(self, context):
        layout = self.layout
        
        mat = bpy.context.object.active_material
        
        col = layout.column()
        # Allow changing of object color
        col.prop(mat, "diffuse_color", text="Color")
'''        
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
    '''
# Operator to change human model
class AlterHumanModel(bpy.types.Operator):
    bl_idname = "mesh.make_changes_to_human"
    bl_label = "Change Human"
    
    Units = EnumProperty(
            name="Units", description="Choose One", 
            items=(('Inches', 'Inch Option', 'Descript1'), 
            ('Centimeter','CM Option', 'Descript2')), 
            default='Inches',
    )
    
    # Wanted measurements
    
    # Height
    
    height_in_inches = IntProperty(
        name="Height (inches)",
        default=bpy.types.Object.human_height_inches,
        min= 36,
        max= 120
        )
    
    height_in_cm = IntProperty(
        name="Height (cm)",
        default=bpy.types.Object.human_height_cm,
        min= 90,
        max= 300
        )
    
    #Width
    width_in_inches = IntProperty(
        name="Width (inches)",
        default=bpy.types.Object.human_width_inches,
        min= 15,
        max= 30
        )
    
    width_in_cm = IntProperty(
        name="Width (cm)",
        default=bpy.types.Object.human_width_inches,
        min= 37,
        max= 75
        )
    
    #Implementation here
    def execute(self, context):
        return {"FINISHED"}
'''    

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
       
# Button to bring in default model
class ImportDefaultModel(bpy.types.Operator):
    bl_idname = "mesh.import_default_model"
    bl_label = "Import Default Model"

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(FilePanel)
    bpy.types.INFO_MT_file_import.append(MeshPanel)
    #bpy.types.INFO_MT_file_import.append(ClothingPanel)

def unregister():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(FilePanel)
    bpy.types.INFO_MT_file_import.append(MeshPanel)
    #bpy.types.INFO_MT_file_import.append(ClothingPanel)
    
if __name__ == "__main__":
    register()

