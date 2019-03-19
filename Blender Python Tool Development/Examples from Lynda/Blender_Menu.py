import bpy

# Define the menu as a class, inherit Menu class
class My_Custom_Menu(bpy.types.Menu):
	"""A custom menu"""
	bl_label = "My custom Menu"
	# should be unique
	bl_idname = "my_custom_menu_98292829"
	

	# draw function
	def draw(self, context):
		layout = self.layout # "Convenience variable" 
		# This is how we add menu items to the menu...
		layout.operator("wm.open_mainfile")
		layout.operator("wm.save_as_mainfile")
		# Usually we would not do this in a menu. It would be in a panel
		layout.prop(context.object, "location")

# register
def register():
	bpy.utils.register_class(My_Custom_Menu)
	
def unregister():
	bpy.utils.unregister_class(My_Custom_Menu)

if __name__ == "__main__":
	register()
	# This just calls the menu when the script is run.
	# But you could call the menu during the execution of an operator or other script (if it is registered)
	bpy.ops.wm.call_menu(name =  My_Custom_Menu.bl_idname)
