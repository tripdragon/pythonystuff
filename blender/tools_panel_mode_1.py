# cobbled together from template and tweaks from
# https://blender.stackexchange.com/questions/167862/how-to-create-a-button-on-the-n-panel

# See Image_1

# Instructions:
# Tested in Blender 3.2
# Paste text or load file into text editor
# Press play button
# View 3d views right hand tools panel and pick bottom most
# See Image_1 you should have the various edit modes of 3d Objects

# Reason, faster way to pick modes rather than dropdown or hotkeys memory

import bpy

class Change_Mode_Edit(bpy.types.Operator):
# class Change_Mode_Edit(bpy.types.Operator, mode_name='OBJECT'):
    """Tooltip"""
    bl_idname = "object.edit"
    bl_label = "Edit"

    # @classmethod
    # def poll(cls, context):
    #     obj = context.active_object
    #     return (obj is not None and obj.type == 'MESH')

    def execute(self, context):
        # Your code here wow!
        bpy.ops.object.mode_set(mode='EDIT')
        # bpy.ops.object.mode_set(mode=mode_name)
        return {'FINISHED'}

class Change_Mode_Object(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.object"
    bl_label = "Object"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}

class Change_Mode_Vertex_Paint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.vertexpaint"
    bl_label = "VertexPaint"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='VERTEX_PAINT')
        return {'FINISHED'}

class Change_Mode_Vertex_Sculpt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sculpt"
    bl_label = "Sculpt"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='SCULPT')
        return {'FINISHED'}

class Change_Mode_Texture_Paint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.texturepaint"
    bl_label = "Texture Paint"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
        return {'FINISHED'}
        
class Change_Mode_Weight_Paint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.weightpaint"
    bl_label = "Weight Paint"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        return {'FINISHED'}



class Objects_Modes_Swapper_Z:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_region_type = "TOOLS"
    bl_category = "Modes"
    bl_options = {"DEFAULT_CLOSED"}

    # def draw(self, context):
    #     layout = self.layout
    #     layout.label(text="This is the main panel.")
    #     row = layout.row()
        # row.operator("mesh.primitive_cube_add")
        # bpy.ops.object.mode_set(mode='EDIT')
        # bpy.ops.mesh.wireframe(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01)
        


class HELLO_PT_World1(Objects_Modes_Swapper_Z, bpy.types.Panel):
    bl_idname = "HELLO_PT_World1"
    bl_label = "Panel 1"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Object modes")
        row = layout.row()
        # row.operator("mesh.primitive_cube_add")
        # would like to simply use this function but its not working yet
        # row.operator(Change_Mode_Edit.bl_idname, 'EDIT')
        row.operator(Change_Mode_Object.bl_idname)
        row = layout.row()
        row.operator(Change_Mode_Edit.bl_idname)
        row = layout.row()
        row.operator(Change_Mode_Vertex_Paint.bl_idname)
        row = layout.row()
        row.operator(Change_Mode_Vertex_Sculpt.bl_idname)
        row = layout.row()
        row.operator(Change_Mode_Texture_Paint.bl_idname)
        row = layout.row()
        row.operator(Change_Mode_Weight_Paint.bl_idname)


def register():
    bpy.utils.register_class(HELLO_PT_World1)
    bpy.utils.register_class(Change_Mode_Object)
    bpy.utils.register_class(Change_Mode_Edit)
    bpy.utils.register_class(Change_Mode_Vertex_Paint)
    bpy.utils.register_class(Change_Mode_Vertex_Sculpt)
    bpy.utils.register_class(Change_Mode_Texture_Paint)
    bpy.utils.register_class(Change_Mode_Weight_Paint)
 
 
def unregister():
    bpy.utils.unregister_class(HELLO_PT_World1)
    bpy.utils.unregister_class(Change_Mode_Object)
    bpy.utils.unregister_class(Change_Mode_Edit)
    bpy.utils.unregister_class(Change_Mode_Vertex_Paint)
    bpy.utils.unregister_class(Change_Mode_Vertex_Sculpt)
    bpy.utils.unregister_class(Change_Mode_Texture_Paint)
    bpy.utils.unregister_class(Change_Mode_Weight_Paint)

if __name__ == "__main__":
    register()
