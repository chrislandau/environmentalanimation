import bpy
from random import random, choice


# Create a class that randomly arrays selected objects
class OBJECT_OT_random_array_selected(bpy.types.Operator):
    """Randomly arrays linked objects within a 2D box of a certain radius"""
    # label that will appear
    bl_label = "random_array"
    # this idname should be very unique
    bl_idname = "action.random_array"
    # Allow the function to both register and undo after exectution if necessary.
    bl_options = {'REGISTER', 'UNDO'}
    
    # properties (Operator Framework)
    num = bpy.props.IntProperty(
        name = "Number of Instances",
        default = 1000,
        description = "Number of linked copies of the object"
        )
    area_radius = bpy.props.FloatProperty(
        name = "radius of the 2D box (half one side)",
        default = 20.0,
        description = "Radius of the 2D Box"
        )
    
    # 'execute' is mandatory for and addon
    def execute(self, context):
        # Here is where you define the operators that the addon will do
        # And these also define what is available in the Redo Last menu upon execution
        # So you can interactively change the properties after you have created the object
        # Here you can add any functionality that you want with loops, conditionals, etc.
        
        seeds = bpy.context.selected_objects
        objects = random_array_object_list(seeds, self.num)
        randomly_place_objects(objects, self.area_radius)
        for seed in seeds:
            seed.select_set(state=True)
        
        return {'FINISHED'} # mandatory


def register():
    # register all classes (only one in this case)
    bpy.utils.register_class(OBJECT_OT_random_array_selected)
    
    
def unregister():
    # unregister all classes (only one in this case)
    bpy.utils.unregister_class(OBJECT_OT_random_array_selected)


def rr(num):
    """
    Random Range function
    """
    rand = (random() * 2 * num)-num
    return rand

def random_array_object_list(seeds, num=1000):
    objects = []
    for i in range(num):
        current = seeds[int(random()*len(seeds))]
        for obj in bpy.data.objects:
            obj.select_set(state=False)
        bpy.context.view_layer.objects.active = current
        current.select_set(state=True)
        bpy.ops.object.duplicate(linked=True)
        object_copy = bpy.context.object
        objects.append(object_copy)
        # Randomly place object in coordinate range
    return objects
    
def randomly_place_objects(objects, area_radius=20.0):
    for object in objects:
        object.location = (rr(area_radius), rr(area_radius), 0)
        for obj in bpy.data.objects:
            obj.select_set(state=False)
 
if __name__ == "__main__":
    register()       