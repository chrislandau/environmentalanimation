import bpy
from random import random
from mathutils import Vector
from mathutils.noise import fractal, hetero_terrain
from math import sin, cos, floor, pow, sqrt, log

import enum

#Objects we are modifying to create terrain
# CHANGE THESE TO DESIRED GEOMETRY
waterObj = bpy.data.objects["WaterPlane"]
sandObj = bpy.data.objects["SandPlane"]
mountainObj = bpy.data.objects["MountainPlane"]
plainObj = bpy.data.objects["PlainPlane"]
forestObj = bpy.data.objects["ForestPlane"]

class Biomes(enum.Enum) :
    mountains = 1
    plains = 2
    ocean = 3
    forest = 4

class Biome():
    def __init__(self, biomeType):
        self.biomeType = biomeType
    
    def generateTerrain(self) :
        if (self.biomeType == Biomes.mountains) :
            generateMountains()
            
        if (self.biomeType == Biomes.plains) :
            generatePlains()
            
        if (self.biomeType == Biomes.ocean) :
            dispArr = generateSand()
            generateWater(dispArr)
            
        if (self.biomeType == Biomes.forest) :
            generateForest()


#Biome variables
Mountain = Biome(Biomes.mountains)
Plain = Biome(Biomes.plains)
Ocean = Biome(Biomes.ocean)
Forest = Biome(Biomes.forest)

#some helper functions
def fract(x) :
    x = abs(x)
    return x - floor(x)

def clamp(x, y, z) : #clamp(x, min, max)
    if (x < y) :
        x = y
    else :
        if (x > z) :
            x = z
    return x

def min(x, y) :
    if (x < y) :
        return x
    return y

def max(x, y) :
    if (x > y) :
        return x
    return y
    
#Terrain Generation Functions
def generateMountains() : # Code for mountain terrain
    for vert in mountainObj.data.vertices :
        coord = vert.coS
        norm = vert.normal
        disp =  fractal(Vector((coord.x, coord.y, 0)), 1, .15, 3) # this seems to be a good setting for mountains
        
        disp = disp * disp * 0.05 # scale factor to smooth bumps
        
        vert.co = Vector((coord.x, coord.y, disp))
        
def generatePlains() : # Hilly terrain
    attractors = []
    for i in range(10) : # place attractors in scene
        attractors.append(Vector(((random() - 0.5) * 150, (random() - 0.5) * 150, clamp(random() * 15, 0, 15))))
        #attractors.append(Vector((i * 20 - 100, i * 20 - 100, i / 2))) #Use for testing terrain function
    
    for vert in plainObj.data.vertices :
        coord = vert.co
        numAttr = 0
        disp = 0
        
        for attractor in attractors : # calculate the affect each attractor has on a vert
            dist = sqrt(pow(attractor.x - coord.x, 2) + pow(attractor.y - coord.y, 2)) #distance to this attractor      
            scaleFac = 0.06 # this controls the falloff range of attractors
            infl = (pow(dist/(3.14 / scaleFac), 3) + 0.5) * (cos(clamp(dist, 0, (3.14 / scaleFac)) * scaleFac) * 10 + 10)
            disp += attractor.z * infl
            numAttr += 1
                
        if (numAttr == 0) :
            numAttr = 1
        disp = 7.5 * scaleFac * disp / numAttr
        
        disp += fractal(Vector((coord.x, coord.y, 0)), 1, .01, 2) * 0.2 # add some fractal flow to the ground
        
        vert.co = Vector((coord.x, coord.y, disp))
        
# Takes next two functions to create the ocean
def generateSand() : #Creates the sand bed for the ocean
    dispArr = []
    vertArr = []
    rangeMin = 100
    rangeMax = -100
    for vert in sandObj.data.vertices : # generate the sand heights
        coord = vert.co
        waveWidth = 4
        waveLength = .5
        disp = fractal(Vector((coord.x * waveWidth, coord.y * waveLength, 0)), .3, .02, 2)
        rangeMin = min(rangeMin, disp) # update min
        rangeMax = max(rangeMax, disp) # update max
        vertArr.append(vert) # append vert to array
        dispArr.append(disp) # append displacement to array
        
        #vert.co = Vector((coord.x, coord.y, disp)) # used for debugging fractal settings
    
    range = rangeMax - rangeMin
    i = 0
    for vert in vertArr : # modify the heights to look better
        coord = vert.co
        disp = dispArr[i]
        #warp the displacement based on its interpolated height
        interp = (disp - rangeMin) / range
        warp = pow(interp, 2) * 2
        if (warp > 0.9) : # flatten out the rough bumps at the top of the tallest ridges
            warp = ((warp - 0.9) / 4) + 0.9
            
        disp = (range * warp) - max(coord.x / 10, -100) # slope the sand bed down
        vert.co = Vector((coord.x, coord.y, disp - 50))
        dispArr[i] = range * warp
        i += 1
        
    return dispArr
        
def generateWater(sandArr) :
    
    i = 0
    for vert in waterObj.data.vertices :
        sandDisp = sandArr[i] # gets the displacement of the sand beneath the water
        coord = vert.co
        disp = 1.3 * pow(2 * (fract((coord.x / 75) - (coord.y / 200)) - 0.5), 2) * sandDisp # wave height based on sand below
        
        waveWidth = 3
        waveLength = 1.5
        disp += 1.3 * fractal(Vector((coord.x * waveWidth, coord.y * waveLength, 0)), .5, .01, 2) # base procedural wave shape
                    
        vert.co = Vector((coord.x, coord.y, disp))
        i += 1
        
        
def generateForest() :
    
    #reset trees
    oldtrees = []
    for tree in bpy.data.collections["TreeCol"].objects:
        oldtrees.append(tree)
    bpy.ops.object.delete({"selected_objects": oldtrees}) #delete the existing trees
    
    minX = forestObj.data.vertices[0].co.x
    minY = forestObj.data.vertices[0].co.y
    maxX = forestObj.data.vertices[0].co.x
    maxY = forestObj.data.vertices[0].co.y
    for vert in forestObj.data.vertices : # build the forest floor
        coord = vert.co
        disp = 0.75 * fractal(Vector((coord.x, coord.y, 0)), .1, .2, 4)
        
        vert.co = Vector((coord.x, coord.y, disp))
        minX = min(minX, coord.x)
        minY = min(minY, coord.y)
        maxX = max(maxX, coord.x)
        maxY = max(maxY, coord.y)
    
    rangeX = maxX - minX
    rangeY = maxY - minY
    
    # Tree Placement
    trees = []
    forestCo = forestObj.location #Center of the forest plane 
    for i in range(15) : # create 15 initial trees
        trees.append(Vector((0.2 * rangeX * (random() - 0.5) + (forestCo.x + (minX + 0.2 * rangeX) + 0.8 * rangeX * 0.05 * i), 0.8 * rangeY * (random() - 0.5) + forestCo.y, 1))) # Vector represents tree coords x,y and tree age
        
    steps = 5 # grow the forest for this many iterations
    while (steps > 0) :
        for tree in trees : #for each tree do
            age = tree.z
            if (age > 1 and age < 5) : # if a tree is older than 1 step old and less than 5 steps
                for i in range(6) : # generate a maximum of 6 seeds
                    if (random() < 0.1 or i < 1) : # 10% chance a seed lives, at least 1 seed always lives
                        # make sure the tree is within the forest boundaries
                        locX = clamp(100 * (random() - 0.5) + tree.x, minX + forestCo.x, maxX + forestCo.x)
                        locY = clamp(100 * (random() - 0.5) + tree.y, minY + forestCo.y, maxY + forestCo.y)
                        trees.append(Vector((locX, locY, 1)))
                    
            tree.z += 1 #increment tree age
        steps -= 1 # decrement the steps left
        
    for tree in trees : # create the tree geometry
        bpy.ops.mesh.primitive_ico_sphere_add(location = Vector((tree.x, tree.y, 10 * (0.6 + random() * 0.4) * sqrt(tree.z)))) #height is based on age of the tree
        treeTop = bpy.context.selected_objects[0]
        treeTop.scale = Vector((tree.z * 2, tree.z * 2, 1.5 * sqrt(tree.z))) #size of the tree also based on age
        bpy.ops.mesh.primitive_cylinder_add(location = Vector((tree.x, tree.y, 0.5 * treeTop.location.z)))
        treeTrunk = bpy.context.selected_objects[0]
        treeTrunk.scale = Vector((0.15 * pow(tree.z, 2), 0.15 * pow(tree.z, 2), 0.5 * treeTop.location.z))
        
#Mountain.generateTerrain()
#Plain.generateTerrain()
#Ocean.generateTerrain()
#Forest.generateTerrain()
