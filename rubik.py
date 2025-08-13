"""A bunch of utility functions for manipulating a Rubik's cube"""
import numpy as np

# DEFINITIONS

# AXES
# 0 FB Front Back axis
# 1 UD Up Down axis
# 2 LR Left Right axis

# ELEMENTS
# there are 3 x 3 x 3 = 27 elements in a rubik's cube
# each element has 6 faces. Let the starting colors be in the given
# orientation:

# 0 u Up (White)
# 1 f Forward (Red)
# 2 l Left (Green)
# 3 b Back (Orange)
# 4 r Right (Blue)
# 5 d Down (Yellow)

# CUBE DEFINITION
# Imagine taking 3x3x1 slices of the cube looking at the red face with white
# facing up.
# Then, on the first slice, start at the top left and reading the
# elements from left to right downwards. Then, move on to the next slice.
# A number has been assigned to each visible face of an element.
# Up/White: 0-9
# Forward/Red: 10-18
# Left/Green: 19-27
# Back/Orange: 28-36
# Right/Blue: 37-45
# Down/Yellow: 46-54

# Each element is specified as 1x6 array with a number indication color and
# position in the array
# indicating orientation.
# [u, f, l, b, r, d]

# mapping colors to their new orientation
# element definition: [u, f, l, b, r, d]
# orientation definition: [up, front, left, back, right, down]
# on the FB axis, CW rotation goes like this
# l -> u-> 2
# f -> f-> 1
# d -> l-> 5
# b -> b-> 3
# u -> r-> 0
# r -> d-> 4

# FB: [2, 1, 5, 3, 0, 4]

# on the UD axis, CW rotation goes like this
# u -> u -> 0
# r -> f -> 4
# f -> l -> 1
# l -> b -> 2
# b -> r -> 3
# d -> d -> 5

# UD: [0, 4, 1, 2, 3, 5]

# on the LR axis, CW rotation goes like this
# b -> u -> 3
# u -> f -> 0
# l -> l -> 2
# d -> b -> 5
# r -> r -> 4
# f -> d -> 1

# LR: [3, 0, 2, 5, 4, 1]

# SLICING
# FB 90deg rotation
# rotate(0, 0) -> cube[0, :, :]
# rotate(0, 1) -> cube[1, :, :]
# rotate(0, 2) -> cube[2, :, :]

# UD 90deg rotation
# rotate(1, 0) -> cube[:, 0, :]
# rotate(1, 1) -> cube[:, 1, :]
# rotate(1, 2) -> cube[:, 2, :]

# LR 90deg rotation
# rotate(2, 0) -> cube[:, :, 0]
# rotate(2, 1) -> cube[:, :, 1]
# rotate(2, 2) -> cube[:, :, 2]


def initialize_cube():
    """initializes a zero cube and fills the faces with ascending numbers"""
    cube = np.zeros((3, 3, 3, 6))
    cube[:, 0, :, 0] = np.arange(1, 10).reshape((3, 3))
    cube[0, :, :, 1] = np.arange(10, 19).reshape((3, 3))
    cube[:, :, 0, 2] = np.arange(19, 28).reshape((3, 3))
    cube[2, :, :, 3] = np.arange(28, 37).reshape((3, 3))
    cube[:, :, 2, 4] = np.arange(37, 46).reshape((3, 3))
    cube[:, 2, :, 5] = np.arange(46, 55).reshape((3, 3))

    return cube


def rotate(cube, axis, position):
    """rotates a 3x3x1 block of a Rubik's cube around a given axis"""
    selectors = [
        (position, slice(None), slice(None)),
        (slice(None), position, slice(None)),
        (slice(None), slice(None), position)
    ]

    # Get affected slice
    affected = cube[selectors[axis]]

    # Process rotation
    affected = rotate_slice(affected, axis)
    affected = map_color_to_orientation(affected, get_axis_map(axis))

    # Assign back
    cube[selectors[axis]] = affected
    return cube


def rotate_slice(elements, axis):
    return np.rot90(elements, axes=(0, 1) if axis == 1 else (1, 0))


def get_axis_map(axis):
    return [
        [2, 1, 5, 3, 0, 4],
        [0, 4, 1, 2, 3, 5],
        [3, 0, 2, 5, 4, 1]
    ][axis]


def map_color_to_orientation(block, axis_map):
    """Rearranges the colors of an element to their new orientation"""
    return np.array(
        [[element[axis_map] for element in elements] for elements in block]
    )


def check_solution(cube):
    """checks a given cube to see if it is solved"""
    for face_index in np.arange(6):
        is_solved = False
        face = cube[:, :, :, face_index]
        # remove zeros and sort array
        filtered_face = np.sort(face[np.where(face != 0)])

        # check that the numbers are consecutive
        for idx in np.arange(9):
            # skip the first iteration so that we dont get index out of range
            if idx == 0:
                continue

            # if the numbers are not consecutive the cube is not solved
            if filtered_face[idx] != filtered_face[idx - 1] + 1:
                return False

            is_solved = idx == len(filtered_face) - 1

        return is_solved
