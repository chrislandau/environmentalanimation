import bpy

# Add items to existing panels. Existing panels would be defined below in the register and unregister functions.
# (replace "__name__" with the name of the desired panel to append to)
def draw(self, context):
    layout = self.layout
    
    world = context.scene.world
    visibility = world.cycles_visibility
    
    flow = layout.column_flow()
    
    flow.prop(visibility, "camera")
    flow.prop(visibility, "diffuse")
    flow.prop(visibility, "glossy")
    flow.prop(visibility, "transmission")
    flow.prop(visibility, "scatter")
    
def register():
     #TODO replace "__name__" with panel class name that you want to append to (for both register and unregister functions)
    bpy.types.__name__.append(draw)
    
def unregister():
    bpy.types.__name__.remove(draw)
    
    
if __name__ == "__main__"":
    register()
