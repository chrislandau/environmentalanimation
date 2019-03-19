import bpy

# class panel
class Our_Custom_Panel(bpy.types.Panel):
	# panel attributes
	bl_label = "My custom panel"
	bl_idname = "object_pt_mycustompanel"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "object"

	# draw function
	def draw(self, context):
		self.layout.label("Hello panel")
		layout = self.layout
		layout.label("This is a really really long label")
		# prop
		layout.prop(context.active_object, "name")
		layout.operator("mesh.primitive_cube_add", "Add a cube"
		# operators
		# row()
		row = layout.row()
		row.prop(scene, "frame_start")
		row.prop(scene, "frame_end")
		
		layout.label(text='Aligned Row:")
		row.prop(scene, "frame_start")
		row.prop(scene, "frame_end")
		# Create two columns by creating a split
		split = layout.split()

		
		# first column()
		col = split.column()
		col.label(text="Column One:")
		col.prop(scene, "frame_end")
		col.prop(scene, "frame_start")
		# box()

		# second column()
		# this may seem strange that we are using the same name "col" as before, but this works ok. It is designed this way to make it easier to copy and paste some code and tweak the text name.
		col = split.column(align=True)
		col.label(text="Column Two:")
		col.prop(scene, "frame_start")
		col.prop(scene, "frame_end")
		
		# box render window()
		box.layout.box()
		box.label(text(="Different button sizes:")
		row = box.row(align=True)
		row.operator("render.render")
		
		sub = row.row()
		sub.scale_x = 2.0
		sub.operator('render.render")
		sub.operator('render.render")
		sub.operator('render.render")

# register
def register():
	bpy.utils.register_class(Our_Custom_Panel)
def unregister():
	bpy.utils.unregister_class(Our_Custom_Panel)

if __name__ == "__main__":
	register()
	
	
	
	
	
	
	
	
	
	
	
	
	
