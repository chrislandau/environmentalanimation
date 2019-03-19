# How a Script Becomes an Operator in Blender

We start with a script that creates objects and then changes their size according to their proximity to a collection of other objects or "attractors"(0_Attractor_Script.py). Then we rationalize this into some functions (1_Attractor_Functions.py). Then we turn this into two, more versatile tools (operators in Blender) (2_Random_Array_Operator.py and 2_Attractor_Operator.py).

The operators allow for a few things:
1. Undo and "Redo Last" (you can move a slider right after you run the operator and dynamically change the parameters)
2. Array any selection of objects w/ the Random Array operator
3. Change the parameters of the Attractor operator in real-time and apply to any collection of geometry you want.
