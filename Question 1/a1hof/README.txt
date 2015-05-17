MONEY CHANGE AND JUG ALGORITHMS WITHOUT HIGHER-ORDER FUNCTIONS
--------------------------------------------------------------
money1.py: Implements the money change algorithm without an explicit use of a tree.
money2.py: Implements the money change algorithm by explicitly using a tree data-structure implemented in tree2.

jugs1.py: Implements the jugs algorithm using the tree data structure of tree2 module.

MONEY CHANGE AND JUG ALGORITHMS USING HIGHER-ORDER FUNCTIONS
------------------------------------------------------------
The following files implement the main search using the higher order function 'search' in the bfs2 module.
money3.py
jugs2.py

The following files implement the main search and extendSolution using the bfs2 module. While money3 and jugs2 implement the extendSolution function all by themselves, the following files make use of the makeExtendSolution higher order function of bfs2 module to build their extendSolution function.
money4.py
jugs3.py

LIBRARY MODULES
---------------
bfs1.py: Implements a higher order breadth first search function called search. 
bfs2.py: Implements two higher order functions, search (as in bfs1) and makeExtendSolution which returns a function extendSolution.
tree2.py: Implements the tree abstract data type.
