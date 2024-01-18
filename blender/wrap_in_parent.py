import bpy
import bmesh

# Wraps the selected object with a parent empty object
# Useful to focus on local transformations
# Saves a few menu clicks for creating and setting object to parent via commands


# save the current selected, make an empty, select the previous and then
# select the empty and parent the previous to the empty
p = bpy.context.selected_objects[0]
pos = p.matrix_world.translation

bpy.ops.object.empty_add(type='ARROWS', radius=10)
g = bpy.context.active_object
g.matrix_world.translation = pos


pos = bpy.context.view_layer.objects.active

bpy.data.objects[p.name].select_set(True)
bpy.data.objects[g.name].select_set(True)

bpy.context.view_layer.objects.active = bpy.data.objects[g.name]
#bpy.ops.object.parent_no_inverse_set()
bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=False)
