from Rotations import updateEdge,makeMove
from Cross_Solver import solve
import random

def solveCross(cube):
    edges = updateEdge(cube)
    TOP = cube["up"][4]
    LEFT = cube["left"][4]
    RIGHT = cube["right"][4]
    FRONT = cube["front"][4]
    BACK = cube["back"][4]
    DOWN = cube["down"][4]
    solution = solve(edges,TOP,LEFT,RIGHT,FRONT,BACK)
    return solution



