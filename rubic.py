import random
from pprint import pprint

# Returns a randomly initialized Rubik's Cube Representation
def initCube ():
    # 9x6=54 faces on a rubik's cube
    faces = list (range(1, 57))
    random.shuffle(faces)
    cube = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(6)]
    pprint(cube)

# checks a given jSON cube to see if it is solved
def checkSolution (cube):
    for face in cube:
        isSolved = False

        # flatten face of cube to a list and sort.
        flatlist = [el for row in face for el in row].sort()
        for idx, el in enumerate(flatlist):
            if idx == 0:
                continue
            
            if flatlist[idx] !> flatlist[idx-1]
                break

            isSolved = True if idx == len(flatlist) -1

    print(cube)

initCube()
