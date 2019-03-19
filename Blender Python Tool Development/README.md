# How a Script Becomes an Operator in Blender

We start with a script that creates objects and then changes their size according to their proximity to a collection of other objects or "attractors" (_0_Attractor_Script.py_). Then we rationalize this into some functions (_1_Attractor_Functions.py_). __THEN__ we turn this into two, more versatile tools ("[__Operators__](https://docs.blender.org/manual/en/dev/advanced/scripting/addon_tutorial.html?highlight=operators)" in Blender) (_2_Random_Array_Operator.py_ and _2_Attractor_Operator.py_).

The operators allow for a few things:
1. Undo and "[__Redo Last__](https://docs.blender.org/manual/en/dev/interface/undo_redo.html#redo-last)" (you can move a slider right after you run the operator and dynamically change the parameters)
2. Array any selection of objects w/ the Random Array operator
3. Change the parameters of the Attractor operator in real-time and apply to any collection of geometry you want.

Other than writing these scripts, all you need to do is run the script (__ALT P__). After you run the script, in the 3D window Search for operators (__F3__). Then type "random" or "attractor". Your operator will appear. In the case of the attractor, be sure to setup a collection of attractors and to select the geometry you are scaling before running the operator.
