import bpy


# Same as mode_1 but it adds the buttons to the top left under the dropdown
# See image_2


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
    bl_label = "Vertex P"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='VERTEX_PAINT')
        return {'FINISHED'}


class Change_Mode_Sculpt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sculpt"
    bl_label = "Sculpt"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='SCULPT')
        return {'FINISHED'}


class Change_Mode_Texture_Paint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.texturepaint"
    bl_label = "Texture P"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
        return {'FINISHED'}


class Change_Mode_Weight_Paint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.weightpaint"
    bl_label = "Weight P"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        return {'FINISHED'}



# draw modes
def draw_mode_object(self, context):
    layout = self.layout
    layout.operator("object.object")

def draw_mode_edit(self, context):
    layout = self.layout
    layout.operator("object.edit")

def draw_mode_vertexpaint(self, context):
    layout = self.layout
    layout.operator("object.vertexpaint")

def draw_mode_sculpt(self, context):
    layout = self.layout
    layout.operator("object.sculpt")

def draw_mode_texturepaint(self, context):
    layout = self.layout
    layout.operator("object.texturepaint")

def draw_mode_weightpaint(self, context):
    layout = self.layout
    layout.operator("object.weightpaint")




def register():
    bpy.utils.register_class(Change_Mode_Object)
    bpy.utils.register_class(Change_Mode_Edit)
    bpy.utils.register_class(Change_Mode_Vertex_Paint)
    bpy.utils.register_class(Change_Mode_Sculpt)
    bpy.utils.register_class(Change_Mode_Texture_Paint)
    bpy.utils.register_class(Change_Mode_Weight_Paint)
    # change VIEW3D_HT_header to VIEW3D_MT_editor_menus
    # if you like it after the original dropdown
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_weightpaint)
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_texturepaint)
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_vertexpaint)
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_sculpt)
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_edit)
    bpy.types.VIEW3D_HT_header.prepend(draw_mode_object)


# press f8 to remove the menus
def unregister():
    bpy.utils.unregister_class(Change_Mode_Object)
    bpy.utils.unregister_class(Change_Mode_Edit)
    bpy.utils.unregister_class(Change_Mode_Vertex_Paint)
    bpy.utils.unregister_class(Change_Mode_Sculpt)
    bpy.utils.unregister_class(Change_Mode_Texture_Paint)
    bpy.utils.unregister_class(Change_Mode_Weight_Paint)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_object)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_edit)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_vertexpaint)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_sculpt)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_texturepaint)
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_mode_weightpaint)


if __name__ == "__main__":
    register()
