"""A bunch of utility functions for manipulating a Rubik's cube"""
import random
from pprint import pprint


def init_cube():
    """Returns a randomly initialized Rubik's Cube Representation"""
    # 9x6=54 faces on a rubik's cube
    faces = list(range(1, 57))
    random.shuffle(faces)
    cube = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(6)]
    pprint(cube)

def check_solution(cube):
    """checks a given jSON cube to see if it is solved"""
    for face in cube:
        is_solved = False

        # flatten face of cube to a list and sort.
        flatlist = [element for row in face for element in row]

        # sort the flattened list
        flatlist.sort()

        # check that the numbers are consecutive
        for idx, element in enumerate(flatlist):

            # skip the first iteration so that we dont get index out of range
            if idx == 0:
                continue

            # if the numbers are not consecutive the cube is not solved
            if flatlist[idx] != flatlist[idx - 1] + 1:
                return False

            is_solved = idx == len(flatlist) - 1

        return is_solved

# Here is a solved cube with the index, color and orientation definitions
# solvedCube = [
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],           # 0 White Up
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # 1 Red North
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],  # 2 Green East
#     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],  # 3 Orange South
#     [[37, 38, 39], [40, 41, 42], [43, 44, 45]],  # 4 Blue West
#     [[46, 47, 48], [49, 50, 51], [52, 53, 54]]   # 5 Yellow Down
# ]


# axis can be a number between 0 and 2. 1: WY, 2: RO, 3: BG
# Position can be a number between 0 and 2, indicating which 3x3x1 block to rotate on the
# specified axis
def rotate(cube, axis, position, rotations):
    """rotates a given 3x3x1 block on a given axis by 90deg CW"""

    assert axis in [0, 1, 2]
    assert position in [0, 1, 2]
    assert isinstance(rotations, int)
    tmp = None
    adjacent_faces = find_adjacent_faces(axis)
    end_face = adjacent_faces[-1]
    print("end_face: ", end_face)

    # transpose the edge face
    if position != 1:
        # find the index of the face being rotated
        face_index = lookup_face_index(axis, position)
        print("face index: ", face_index)
        print("adjacent faces: ", adjacent_faces)
        cube[face_index] = transpose(cube[face_index])

    for idx, face in enumerate(adjacent_faces):

        prev = tmp
        print("ind: ", idx)
        print("previous: ", prev)
        print("face: ", face)

        # rotations on the WY axis rotate rows
        # rotate (cube, 1, 1, 1) 1 rotation at the 1st position on the WY axis
        if axis == 0:
            tmp = cube[face][position]

            # shifts the rows 1 position over, the last array element becomes
            # the first,
            cube[face][position] = cube[end_face, position] if idx == 0 else prev
            continue

        # rotations on the RO axis rotate rows and columns. Rows on W:0 and Y:5 faces
        # and columns on G:2 and B:4 faces
        if axis == 1:
            rotate_row = face in [0, 5]
            tmp = cube[face, :, position] if rotate_row and face else cube[face, position]
            print("tmp: ", tmp)
            if rotate_row:
                print("cube: ", cube[end_face, :, position])
                cube[face][position] = cube[end_face, :, position] if idx == 0 else prev
                continue
            
            # columns are rotated on even (nonzero) faces
            cube[face, :, position] = cube[end_face][position] if idx == 0 else prev
            continue


        # rotations on the BG axis rotate columns
        # rotate (cube, 2, 1, 1) 1 rotation at the 1st position on the RO axis
        if axis == 2:
            tmp = cube[face, :, position]

            # shifts adjacent columns 1 position over, the last array element
            # becomes the first,
            cube[face, :, position] = cube[adjacent_faces[-1], :, position] if idx == 0 else prev
            continue
    
    print(cube)
    return cube

# the face indicies are as follows:
# 0: white, 1: red, 2: green, 3: orange, 4: blue, 5: yellow
def lookup_face_index(axis, position):
    """returns the index of the face being rotated (corresponding to given axis and position)"""
    face_index = [
        [0, None, 5],
        [1, None, 3],
        [2, None, 4]
    ]
    return face_index[axis][position]


# when rotating on a given axis, let the 2 faces on the axis of rotation be called back and front
# let the remaining 4 faces be called adjacent faces.
# the face indicies are as follows:
# 0: white, 1: red, 2: green, 3: orange, 4: blue, 5: yellow
# Here are the axis indicies definitions 0: WY, 1: RO, 2: BG
def find_adjacent_faces(axis):
    """returns the indices of faces to be rotated in a cube in the order they will be rotated"""

    adjacent_faces = [
        [1, 2, 3, 4],
        [0, 4, 5, 2],
        [0, 3, 5, 1]
    ]

    return adjacent_faces[axis]

def transpose(face):
    """transposes a 2D Face"""
    return list(map(list, zip(*face)))
