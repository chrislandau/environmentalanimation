## Designing an Add-On

# First, answer a few basic questions...
# What kind of things do I... 1. do often, 2. take long to setup, and 3. are complicated or complex problems to solve?
# What problem is the add-on supposed to solve or what task will it acheive?
# Is there a tool that will do this already?
# Are the existing tools a viable option?
# What is this used for?
# What kind of inputs and outputs will it require?
# What is the user experience?

# Next, take stock of the inputs, outputs
# Geometry
# Variables
# Properties
# Classes

# Finally, Map out how to get there (do this in text form, as this can be the beginning of your script
# Classes - These may be operators, panels or other pieces
# Properties - Design properties that are at play and their parameters
# Layout the interface, etc
# Functions - describe the functin necessary to acheive your goals
# Design the algorithms necessary to acheive efficient functionality



## Add-On Example
# This example of a self-contained addon is largely from LinkedIn Learning's "Blender: Python Scripting" with Patrick W. Crawford

## Basic Structure of a self-contained addon:
    # info
    # imports
    # classes / operators
    # registration


# bl_info (Define addon properties)
bl_info = {
        "name":"Add Smooth Monkey",
        "author":"Chris Landau",
        "version":(0.0.1),
        "blender":(2,8),
        "location":"View3D > Add > Mesh > Add Smooth Monkey",
        "description":"Adds a new smooth monkey",
        "warning":"",
        "wiki_url":"",
        "category":"Add Mesh"
        }
        
import bpy

# classes

# operator classes

# "OBJECT_OT_..." is a convention for... object operator type?
class OBJECT_OT_add_smooth_monkey(bpy.types.Operator):
    """Adds a smooth monkey to the 3D view"""
    # label that will appear
    bl_label = "Add smooth monkey"
    # this idname should be very unique
    bl_idname = "mesh.add_smooth_monkey"
    # Allow the function to both register and undo after exectution if necessary.
    bl_options = {'REGISTER', 'UNDO'}
    
    # properties (Operator Framework)
    smoothness = bpy.props.IntProperty(
        name = "Smoothness"
        default = 2,
        description = "Subsurface level"
        )
    size = bpy.props.FloatProperty(
        name = "Size",
        default = 1,
        description = "Size of Monkey added"
        )
    name = bpy.props.StringProperty(
        name = "Name",
        default = "Monkey",
        description = "Name of added Monkey"
        )
    
    # 'execute' is mandatory for and addon
    def execute(self, context):
        # Here is where you define the operators that the addon will do
        # And these also define what is available in the Redo Last menu upon execution
        # So you can interactively change the properties after you have created the object
        # Here you can add any functionality that you want with loops, conditionals, etc.
        
        #For example: Add the monkey
        bpy.ops.mesh.primitive_monkeyadd(radius=self.size)
        # Change smoothing options
        bpy.ops.object.shade_smooth()
        # Add subdivision modifier
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subsurf"].levels = self.smoothness
        
        bpy.context.object.name = self.name
        
        return {'FINISHED'} # mandatory

# panel classes
class smooth_monkey_panel(bpy.types.Panel):
    """The smooth monkey add panel"""
    bl_label = "Smooth Monkey"
    bl_idname = "OBJECT_PT_smooth_monkey"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_catgegory = "Create"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Add smooth monkey named:")
        # Here is a custom property that was created in the register function. It is also deleted in the unregister function.
        col.prop(context.scene, "smooth_monkey_name", text="", icon="MESH_MONKEY")
        p = col.operator(OBJECT_OT_add_smooth_monkey.bl_idname)
        p.name = context.scene.smooth_monkey_name
    
# button functions
def add_object_button(self.context):
    self.layout.operator(
        OBJECT_OT_add_smooth_monkey.bl_idname,
        # icons can be found using developer icons addon
        icon = "MESH_MONKEY"
        )


# registration
def register():
    
    # Define custom properties
    bpy.types.Scene.smooth_monkey_name = bpy.props.StringProperty(
        name = "Monkey Name"'
        default = "Suzanne"
        description = "Name of object after adding to the scene"
        
        )
    # register all classes
    bpy.utils.register.class(OBJECT_OT_add_smooth_monkey)
    bpy.utils.register.class(smooth_monkey_panel)
    # INFO_MT_mesh_add is the menu to append the operator to (a menu)
    # Find this menu by looking in the source and definition for the class (right click on the add monkey button in that menu)
    
    # register all types
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    
def unregister():
    # unregister all classes
    bpy.utils.unregister.class(OBJECT_OT_add_smooth_monkey)
 bpy.utils.unregister.class(smooth_monkey_panel)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    
    # unregister all types (delete)
    del bpy.types.Scene.smooth_monkey_name

if __name__ == "__main__":
    register()
