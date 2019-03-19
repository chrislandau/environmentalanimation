import bpy
from random import random

# In blender, put all attractors in a Collection called "Attractors"
# this will grab all objects associated with that collection
attractors = bpy.data.collections["Attractors"].objects

# Setup Random Range function
def rr(num):
    rand = (random() * 2 * num)-num
    return rand


# Randomly Array some spheres
# Create empty list "objects"
objects = []
# Loop 1000 times
for i in range(1000):
    # Create new ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(radius=1)
    # set freshly created object as variable "ico"
    ico = bpy.context.object
    # Randomly place spehere in coordinate range
    ico.location = (rr(20.0), rr(20.0), 0)
    # Add ico sphere to list "objects"
    objects.append(ico)


# Loop over objects
for ico in objects:
    # create empty list "distances"
    distances = []
    # Loop over attractors
    for attractor in attractors:
        # Get distance between ico location and attractor location
        distance = (ico.location - attractor.location).length
        # add distance to distances
        distances.append(distance)
    
    
    # Find closest attractor
    # Sort distances small to big
    distances.sort()
    # Create size as a function of the smallest distance
    size = 2/(distances[0])
    # limit the size
    if size > 2:
        size = 2
    if size < .1:
        size = .1
    # set the scale of the object
    ico.scale = (size,size,size)
