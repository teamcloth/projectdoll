# This example assumes we have a mesh object selected

import bpy
import bmesh

# Get the active mesh
me = bpy.data.meshes['GZM_Shoulder.001']

# Get a BMesh representation
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(me)   # fill it in from a Mesh
for i in bm.verts:
    i.co.x -= 100


# Finish up, write the bmesh back to the mesh
bm.to_mesh(me)
bm.free()  # free and prevent further access