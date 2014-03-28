import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import *
import bmesh

bl_info = {
	"name":	"Project Doll",
	"author" : "Team Cloth",
	"version": (0,0,1),
	"blender": (2,6,2),
	"description": "Test clothing on model types"
}

#Placeholder properties
bpy.types.Object.cProp = bpy.props.IntProperty( name = "Number", min = 0, max = 10, default = 5)
bpy.types.Object.human_height_inches = bpy.props.IntProperty( name = "Height", min = 12, max = 96, default=65)
bpy.types.Object.human_height_cm = bpy.props.IntProperty( name = "Height", min = 30, max = 250, default=150)
bpy.types.Object.human_width_inches = bpy.props.IntProperty( name = "Width", min = 30, max = 250, default=150)
bpy.types.Object.human_width_cm = bpy.props.IntProperty( name = "Width", min = 30, max = 250, default=150)

#Panel on side, inport export buttons
class PDPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Project Doll"
    
    def draw(self, context):
        layout = self.layout
        
        #Import default model buttons (m/f are the same for now)
        col = layout.column(align = True)
        col.label(text="Import Default models")
        row = col.row(align = True)
        row.operator("mesh.import_default_model", text = "Male")
        row.operator("mesh.import_default_model", text = "Female")
        
        #Export the selected model button
        col = layout.column(align = True)
        col.label(text="Export selected mesh")
        row = col.row(align = True)
        row.operator("mesh.export_selected_model", text = "Export Selected Model")
        
        #Import a custom model/mesh
        col = layout.column(align = True)
        col.label(text="Import your own clothing/model")
        row = col.row(align = True)
        row.operator("mesh.import_custom_model", text = "Import Custom Model")
	#end draw


#Another Panel for properties
class PDPanel2(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Project Doll Properties"
    
    #Unit Measuring
    bpy.types.Scene.Units = bpy.props.EnumProperty(
            name="Units", description="Choose One", 
            items=(('Inches', 'Inch option', 'Descript1'), 
            ('Centimeter','Cm option', 'Descript2')), 
            default='Inches',
    )
    
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.prop(scn,"Units", expand=True)
        ob = context.object
        #if not ob:
            #return
        #Customization of human model
        layout.prop(ob, "cProp", slider=True)
        layout.prop(ob, "human_height_inches", slider=True)
        layout.prop(ob, "human_width_inches", slider=True)
        #Button to make changes
        layout.operator("mesh.make_changes_to_human", text = "Apply changes to human")

# Button to change human model        
class AlterHumanModel(bpy.types.Operator):
    bl_idname = "mesh.make_changes_to_human"
    bl_label = "Change Human"
    
    #Implementation here
    def execute(self, context):
        return {'Finished'}
            
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
        '''
        fp = open(self.filepath,'w');
        for v in bm.verts:
            x = v.co
            fp.write("v %.5f %.5f %.5f\n" % (x[0], x[1], x[2]))
        
        if len(bm.uv_textures) > 0:
            uvtex = bm.uv_textures[0]
            for f in bm.faces:
                data = uvtex.data[f.index]
                fp.write("vt %.5f %.5f\n" % (data.uv1[0], data.uv1[1]))
                fp.write("vt %.5f %.5f\n" % (data.uv2[0], data.uv2[1]))
                fp.write("vt %.5f %.5f\n" % (data.uv3[0], data.uv3[1]))
                if len(f.vertices) == 4:
                    fp.write("vt %.5f %.5f\n" % (data.uv4[0], data.uv4[1]))
 
            vt = 1
            for f in bm.faces:
                vs = f.vertices
                fp.write("f %d/%d %d/%d %d/%d" % (vs[0]+1, vt, vs[1]+1, vt+1, vs[2]+1, vt+2))
                vt += 3
                if len(f.vertices) == 4:
                    fp.write(" %d/%d\n" % (vs[3]+1, vt))
                    vt += 1        
                else:
                    fp.write("\n")
        else:
         
        for f in bm.faces:
            vs = f.verts
            #print(vs[0].)
            fp.write("f %d %d %d" % (vs[0].co.x, vs[1].co, vs[2].co+1))
            if len(f.verts) == 4:
                fp.write(" %d\n" % (vs[3].co+1))
            else:
                fp.write("\n")
 
        #print('%s successfully exported' % realpath)
        fp.close()
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return
        '''
        # Write obj file 
        f = open(self.filepath, 'w')
        #Get filename
        x = (self.filepath.rfind("/",0,-4))
        if x > -1:
            filename = self.filepath[x+1:-4]
        else:
            print("Linux, mac stuff here")
            #Linux/mac stuff here
                 
        #filename = self.filepath[:-4]
        print(filename) 
        f.write("# ProjectDoll exported OBJ\n") 
        f.write("# www.makehuman.org\n") 
        f.write("mtllib " + filename + ".mtl\n") 
        #Traverse vertices in mesh
        for v in bm.verts: 
            f.write("v %f %f %f\n" %(v.co[0], v.co[1], v.co[2])) 
        for uv in bm.loops.layers.uv
            f.write("vt %f %f\n" %(uv.data[length].uv[0], uv.data[length].uv[1]))  
        for v in bm.verts: 
            f.write("vn %f %f %f\n" %(v.normal[0], v.normal[1], v.normal[2])) 
        f.write("usemtl basic\n") 
        f.write("s off\n") 
         
        #faces = files3d.loadFacesIndices("data/3dobjs/base.obj") 
        for fc in bm.faces: 
            f.write("f") 
            for v in fc: 
                f.write(" %i/%i/%i " %(v[0] + 1, v[1] + 1, v[0] + 1)) 
            f.write("\n") 
        f.close() 
         
        # Write material file 
        f = open(filename + ".mtl", 'w') 
        f.write("# MakeHuman exported MTL\n") 
        f.write("# www.makehuman.org\n") 
        f.write("newmtl basic\n") 
        f.write("Ka 1.0 1.0 1.0\n") 
        f.write("Kd 1.0 1.0 1.0\n") 
        f.write("Ks 0.33 0.33 0.52\n") 
        f.write("illum 5\n") 
        f.write("Ns 50.0\n") 
        f.write("map_Kd -clamp on " + obj.texture + "\n") 
        f.close()
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
		
def register():
    bpy.utils.register_class(PDPanel)
    bpy.utils.register_class(ImportDefaultModel)
    bpy.utils.register_class(ExportSelectedModel)
    bpy.utils.register_class(ImportCustomModel)
    bpy.utils.register_class(PDPanel2)
    bpy.utils.register_class(AlterHumanModel)    

def unregister():
    bpy.unregister_class(PDPanel)
    bpy.unregister_class(ImportDefaultModel)
    bpy.unregister_class(ExportSelectedModel)
    bpy.unregister_class(ImportCustomModel)
    bpy.unregister_class(PDPanel2)
    bpy.unregister_class(AlterHumanModel)

if __name__ == "__main__":
	register()	
