import bpy
from random import random

def main():
    # Put all attractors in a Collection called "Attractors"
    # this will grab all objects associated with that collection
    attractors = bpy.data.collections["Attractors"].objects
    objects = random_array_icospheres()
    # Randomly Array some spheres
    scale_by_attraction(objects, attractors)
        
def random_array_icospheres(num=1000, radius=1, area_radius=20.0):
    # Create empty list "objects"
    objects = []
    # Loop 1000 times
    for i in range(num):
        # Create new ico sphere
        bpy.ops.mesh.primitive_ico_sphere_add(radius=1)
        # set freshly created object as variable "ico"
        ico = bpy.context.object
        # Randomly place spehere in coordinate range
        ico.location = (rr(area_radius), rr(area_radius), 0)
        # Add ico sphere to list "objects"
        objects.append(ico)
    return objects

def scale_by_attraction(objects,
                        attractors,
                        min_size=.1,
                        max_size=2,
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
        size = distance_factor/(distances[0])
        # limit the size
        if size > max_size:
            size = max_size
        if size < min_size:
            size = min_size
        # set the scale of the object
        object.scale = (size,size,size)

def rr(num):
    """
    Random Range function
    """
    rand = (random() * 2 * num)-num
    return rand

if __name__ == "__main__" : main()


