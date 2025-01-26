"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""

from functions import stack_maze

maze1 = {'Start': ['A'],
         'A': ['B', 'C'],
         'B': [],
         'C': ['D', 'E'],
         'D': [],
         'E': ['F', 'X'],
         'F': ['G', 'H'],
         'G': [],
         'H': []}

maze2 = {'Start': ['A'],
         'A': ['B', 'C'],
         'B': [],
         'C': ['D', 'E'],
         'D': [],
         'E': ['X', 'F'],
         'F': ['G'],
         'G': ['C']}

print(stack_maze(maze1))
print(stack_maze(maze2))
