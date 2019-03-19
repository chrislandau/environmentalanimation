import bpy
from random import random


# Create a class that 
class OBJECT_OT_attraction_by_collection(bpy.types.Operator):
    """Changes the size of objects based on proximity to collection of attractors"""
    # label that will appear
    bl_label = "attractors_simple"
    # this idname should be very unique
    bl_idname = "action.attractors_simple"
    # Allow the function to both register and undo after exectution if necessary.
    bl_options = {'REGISTER', 'UNDO'}
    
    # properties (Operator Framework)
    attractors_name = bpy.props.StringProperty(
        name = "Attractor Collection",
        default = "Attractors",
        description = "Name of collection containing only the desired attractors"
        )
    min_scale = bpy.props.FloatProperty(
        name = "Minimum Scale",
        default = .1,
        description = "Minimum Scale of Objects"
        )
    max_scale = bpy.props.FloatProperty(
        name = "Maximum Scale",
        default = 2.0,
        description = "Maximum Scale of Objects"
        )
    distance_factor = bpy.props.FloatProperty(
        name = "Distance Factor",
        default = 2.0,
        description = "Factor to multiply by 1/distance"
        )
    
    # 'execute' is mandatory for and addon
    def execute(self, context):
        # Here is where you define the operators that the addon will do
        # And these also define what is available in the Redo Last menu upon execution
        # So you can interactively change the properties after you have created the object
        # Here you can add any functionality that you want with loops, conditionals, etc.
        
        objects = bpy.context.selected_objects
        attractors = bpy.data.collections[self.attractors_name].objects
        scale_by_attraction(objects,
                            attractors,
                            self.min_scale,
                            self.max_scale,
                            self.distance_factor,
                            )
        
        return {'FINISHED'} # mandatory


def register():
    # register all classes (only one in this case)
    bpy.utils.register_class(OBJECT_OT_attraction_by_collection)
    
    
def unregister():
    # unregister all classes (only one in this case)
    bpy.utils.unregister_class(OBJECT_OT_attraction_by_collection)


def scale_by_attraction(objects,
                        attractors,
                        min_scale=.1,
                        max_scale=2,
                        distance_factor=2,
                        ):
    # Loop over objects
    for object in objects:
        # create empty list "distances"
        distances = []
        # Loop over attractors
        for attractor in attractors:
            # Get distance between object location and attractor location
            distance = (object.location - attractor.location).length
            # add distance to distances
            distances.append(distance)
        
        # Find closest attractor
        # Sort distances small to big
        distances.sort()
        # Create size as a function of the smallest distance
        
        # Find closest attractor
        # Sort distances small to big
        distances.sort()
        # Create size as a function of the smallest distance
        scale = distance_factor/(distances[0])
        # limit the size
        if scale > max_scale:
            scale = max_scale
        if scale < min_scale:
            scale = min_scale
        # set the scale of the object
        object.scale = (scale,scale,scale)


if __name__ == "__main__":
    register()