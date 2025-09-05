"""A bunch of utility functions for manipulating a Rubik's cube"""
from random import randrange
import numpy as np

face_selectors = [
    (slice(None), 0, slice(None), 0),
    (0, slice(None), slice(None), 1),
    (slice(None), slice(None), 0, 2),
    (2, slice(None), slice(None), 3),
    (slice(None), slice(None), 2, 4),
    (slice(None), 2, slice(None), 5)
]

solved_faces = np.split(np.arange(1, 55), 6)


def randomize_cube(cube, rotations=30):
    """randomizes a given cube"""
    for rotation in np.arange(rotations):
        directions = ["CW", "CCW"]
        axis = randrange(3)
        direction = randrange(2)
        position = randrange(3)

        cube = rotate(cube, axis, position, directions[direction])

    return cube


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
    '''gets the map for mapping colors to their new orientation'''
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
