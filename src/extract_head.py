import bpy
import bmesh

# Get the head vertices:
head_mesh = bpy.data.meshes['GZM_Head']
bm_head = bmesh.new()
bm_head.from_mesh(head_mesh)

head_vertices = list(bm_head.verts)

# Now let's get the meshes for the entire body:
full_body_mesh = bpy.context.object.data
bm_body = bmesh.new()
bm_body.from_mesh(full_body_mesh)

body_vertices = list(bm_body.verts)

# List to hold the actual head vertices with respect to the vertices in the body:
actual_head_vertices = []

for i in range(len(body_vertices)):
    next_body_vertex = body_vertices[i]
    print("next_body_vertex.co.x is")
    print(next_body_vertex.co.x)
    print("next_body_vertex.co.y is")
    print(next_body_vertex.co.y)
    print("next_body_vertex.co.z is")
    print(next_body_vertex.co.z)
    
    for j in range(len(head_vertices)):
        next_head_vertex = head_vertices[j]
        
        if (abs(next_body_vertex.co.x - next_head_vertex.co.x) < 0.1) and \
           (abs(next_body_vertex.co.y - next_head_vertex.co.y) < 0.1) and \
           (abs(next_body_vertex.co.z - next_head_vertex.co.z) < 0.1):
               actual_head_vertices.append(next_body_vertex)
               print("FOUND A VERTEX!")
        else:
            print("DID NOT FIND VERTEX!")
               
        
print("Length of actual_head_vertices")
print(len(actual_head_vertices))