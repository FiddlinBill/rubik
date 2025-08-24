"""A bunch of utility functions for manipulating a Rubik's cube"""
import numpy as np

# DEFINITIONS

# AXES
# 0 FB Front Back axis
# 1 UD Up Down axis
# 2 LR Left Right axis

# ELEMENTS
# there are 3 x 3 x 3 = 27 elements in a rubik's cube and each element has 6
# faces. Each element is specified as 1x6 array with a number indicating color
# and position in the array indicating orientation:
# Let the starting colors be in the given orientation:

# 0 u Up (White)
# 1 f Forward (Red)
# 2 l Left (Green)
# 3 b Back (Orange)
# 4 r Right (Blue)
# 5 d Down (Yellow)

# [u, f, l, b, r, d]

# CUBE DEFINITION
# a cube may be represented as a 3x3x3x6 matrix because each of the 27 elements
# of a Rubik's cube has 6 faces.
# Now, imagine taking 3x3x1 vertical slices of the cube looking at the red face
# with white facing up. Then, on the first slice, start at the top left and
# read the elements from left to right downwards. Then, move on to the next
# slice.
# A number has been assigned to each visible face of an element.
# Up/White: 0-9
# Forward/Red: 10-18
# Left/Green: 19-27
# Back/Orange: 28-36
# Right/Blue: 37-45
# Down/Yellow: 46-54


# MAPPING COLORS TO NEW ORIENTATION
# element definition: [u, f, l, b, r, d]
# on the FB axis, Clockwise (CW) rotation goes like this
# l -> u-> 2
# f -> f-> 1
# d -> l-> 5
# b -> b-> 3
# u -> r-> 0
# r -> d-> 4

# CW on FB: [2, 1, 5, 3, 0, 4]

# on the FB axis, Counter Clockwise (CCW) rotation goes like this
# r -> u -> 4
# f -> f -> 1
# u -> l -> 0
# b -> b -> 3
# d -> r -> 4
# l -> d -> 2

# CCW on FB: [4, 1, 0, 3, 5, 2]

# on the UD axis, CW rotation goes like this
# u -> u -> 0
# r -> f -> 4
# f -> l -> 1
# l -> b -> 2
# b -> r -> 3
# d -> d -> 5

# CW on UD: [0, 4, 1, 2, 3, 5]

# on the UD axis, CCW rotation goes like this
# u -> u -> 0
# l -> f -> 2
# b -> l -> 3
# r -> b -> 4
# f -> r -> 1
# d -> d -> 5

# CCW on UD: [0, 2, 3, 4, 1, 5]


# on the LR axis, CW rotation goes like this
# b -> u -> 3
# u -> f -> 0
# l -> l -> 2
# d -> b -> 5
# r -> r -> 4
# f -> d -> 1

# CW on LR: [3, 0, 2, 5, 4, 1]


# on the LR axis, CCW rotation goes like this
# f -> u -> 1
# d -> f -> 5
# l -> l -> 2
# u -> b -> 0
# r -> r -> 4
# b -> d -> 3

# CCW on LR: [1, 5, 2, 0, 4, 3]

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

solved_faces = np.split(np.arange(1, 55), 6)

face_selectors = [
    (slice(None), 0, slice(None), 0),
    (0, slice(None), slice(None), 1),
    (slice(None), slice(None), 0, 2),
    (2, slice(None), slice(None), 3),
    (slice(None), slice(None), 2, 4),
    (slice(None), 2, slice(None), 5)
]


def initialize_cube():
    """initializes a solved cube, which is a zero cube where each face is
    filled with ascending numbers"""
    cube = np.zeros((3, 3, 3, 6))
    for idx, selector in enumerate(face_selectors):
        cube[selector] = solved_faces[idx].reshape((3, 3))

    return cube


def rotate(cube, axis=0, position=0, direction="CW"):
    """rotates a 3x3x1 block of a Rubik's cube around a given axis"""
    selectors = [
        (position, slice(None), slice(None)),
        (slice(None), position, slice(None)),
        (slice(None), slice(None), position)
    ]

    # Get affected slice
    affected = cube[selectors[axis]]

    # Process rotation
    affected = rotate_slice(affected, axis, direction)
    affected = map_color_to_orientation(
        affected,
        get_axis_map(axis, direction)
    )

    # Assign back
    cube[selectors[axis]] = affected
    return cube


def rotate_slice(elements, axis=0, direction="CW"):

    # determines which direction to rotate
    rotation_axes = {
        "CW": (1, 0) if axis != 1 else (0, 1),
        "CCW": (0, 1) if axis != 1 else (1, 0)
    }[direction]

    return np.rot90(elements, axes=rotation_axes)


def get_axis_map(axis=0, direction="CW"):

    return {
        "CW": [
            [2, 1, 5, 3, 0, 4],
            [0, 4, 1, 2, 3, 5],
            [3, 0, 2, 5, 4, 1]
        ],
        "CCW": [
            [4, 1, 0, 3, 5, 2],
            [0, 2, 3, 4, 1, 5],
            [1, 5, 2, 0, 4, 3]
        ]
    }[direction][axis]


def map_color_to_orientation(block, axis_map):
    """Rearranges the colors of an element to their new orientation"""
    return np.array(
        [[element[axis_map] for element in elements] for elements in block]
    )


def check_solution(cube):
    """checks a given cube to see if it is solved"""
    for selector in face_selectors:
        face = np.sort(cube[selector].flatten())
        is_contained = any(
            np.array_equal(face, solved_face) for solved_face in solved_faces
        )
        if not is_contained:
            return False

    return True
