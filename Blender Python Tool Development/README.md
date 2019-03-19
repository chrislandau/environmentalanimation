# How a Script Becomes an Operator in Blender

We start with a script that creates objects and then changes their size according to their proximity to a collection of other objects or "attractors"(_0_Attractor_Script.py_). Then we rationalize this into some functions (_1_Attractor_Functions.py_). Then we turn this into two, more versatile tools ("__Operators__" in Blender) (_2_Random_Array_Operator.py_ and _2_Attractor_Operator.py_).

The operators allow for a few things:
1. Undo and "[__Redo Last__](https://docs.blender.org/manual/en/dev/interface/undo_redo.html#redo-last)" (you can move a slider right after you run the operator and dynamically change the parameters)
2. Array any selection of objects w/ the Random Array operator
3. Change the parameters of the Attractor operator in real-time and apply to any collection of geometry you want.
