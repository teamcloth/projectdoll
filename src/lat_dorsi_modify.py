import bpy
import bmesh

full_body = bpy.data.objects['male_modelBody']

for i in range(len(full_body.vertex_groups)):
    if full_body.vertex_groups[i].name == 'DEF-lat_dorsi.L':
        print("Found vertex group DEF-lat_dorsi.L at index: " + str(i))
        lat_dorsi_left_index = i
    elif full_body.vertex_groups[i].name == 'DEF-lat_dorsi.R':
        print("Found vertex group DEF-lat_dorsi.R at index: " + str(i))
        lat_dorsi_right_index = i
        
print("lat_dorsi_left_index: " + str(lat_dorsi_left_index))
print("lat_dorsi_right_index: " + str(lat_dorsi_right_index))

lat_dorsi_left_vertices = []
lat_dorsi_right_vertices = []
        
for vertex in full_body.data.vertices:
    for g in vertex.groups:
        if g.group == lat_dorsi_left_index:
            lat_dorsi_left_vertices.append(vertex)
            
print(lat_dorsi_left_vertices)

for vertex in lat_dorsi_left_vertices:
    vertex.co.x += 0.5