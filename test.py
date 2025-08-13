import unittest
import numpy as np
from rubik import (
    check_solution,
    get_axis_map,
    initialize_cube,
    rotate,
    rotate_slice,
    map_color_to_orientation
)

# a position 0 slice on the fb axis that has been rotated 90 CW.
# Colors have not been remapped
slice_after_rot90 = np.array([  # 1st slice
    [
         [0, 16, 27, 0, 0, 46], [0, 13, 24, 0, 0, 0], [7, 10, 21, 0, 0, 0]
    ],
    [
        [0, 17, 0, 0, 0, 47], [0, 14, 0, 0, 0, 0], [8, 11, 0, 0, 0, 0]
    ],
    [
        [0, 18, 0, 0, 43, 48], [0, 15, 0, 0, 40, 0], [9, 12, 0, 0, 37, 0]
    ]
])

# a slice taken at position 0 on the fb axis and rotated 90
# orientation has been remapped
rot90_fb = np.array([
    [
        [21, 16, 46,  0,  0, 0],
        [20, 13, 0,  0,  0,  0],
        [19, 10, 0,  0,  1,  0]
    ],
    [
        [0, 17,  47,  0,  0, 0],
        [0, 14,  0,  0,  0,  0],
        [0, 11,  0,  0,  2,  0]
    ],
    [
        [0, 18,  48,  0, 0, 39],
        [0, 15,  0,  0, 0,  38],
        [0, 12,  0,  0, 3,  37]
    ]
])

rot90_fb_no_map = np.array([
    [
        [0, 16, 21,  0,  0, 46],
        [0, 13, 20,  0,  0,  0],
        [1, 10, 19,  0,  0,  0]
    ],
    [
        [0, 17,  0,  0,  0, 47],
        [0, 14,  0,  0,  0,  0],
        [2, 11,  0,  0,  0,  0]
    ],
    [
        [0, 18,  0,  0, 39, 48],
        [0, 15,  0,  0, 38,  0],
        [3, 12,  0,  0, 37,  0]
    ]
])


# a slice taken at position 0 on the ud axis and rotated 90
# orientation has been remapped
rot90_ud = np.array([
    [
        [3, 37, 12, 0, 0, 0],
        [6, 40, 0, 0, 0, 0],
        [9, 43, 0, 0, 30, 0]
    ],
    [
        [2, 0, 11, 0, 0, 0],
        [5, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 29, 0]
    ],
    [
        [1, 0, 10, 19, 0, 0],
        [4, 0, 0, 22, 0, 0],
        [7, 0, 0, 25, 28, 0]
    ]
])


# a slice taken at position 0 on the ud axis and rotated 90
# orientation has not been remapped
rot90_ud_no_map = np.array([
    [
        [3, 12, 0, 0, 37, 0],
        [6, 0, 0, 0, 40, 0],
        [9, 0, 0, 30, 43, 0]
    ],
    [
        [2, 11, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0],
        [8, 0, 0, 29, 0, 0]
    ],
    [
        [1, 10, 19, 0, 0, 0],
        [4, 0, 22, 0, 0, 0],
        [7, 0, 25, 28, 0, 0]
    ]
])


# a slice taken at position 0 on the lr axis and rotated 90
# orientation has been remapped
rot90_lr = np.array([
    [
         [28, 7, 25, 0, 0, 0],
         [0, 4, 22, 0, 0, 0],
         [0, 1, 19, 0, 0, 10]
    ],
    [
         [31, 0, 26, 0, 0, 0],
         [0, 0, 23, 0, 0, 0],
         [0, 0, 20, 0, 0, 13]
    ],
    [
         [34, 0, 27, 52, 0, 0],
         [0, 0, 24, 49, 0, 0],
         [0, 0, 21, 46, 0, 16]
    ]
])

rot90_lr_no_map = np.array([
    [
         [7, 0, 25, 28, 0, 0],
         [4, 0, 22, 0, 0, 0],
         [1, 10, 19, 0, 0, 0]
    ],
    [
         [0, 0, 26, 31, 0, 0],
         [0, 0, 23, 0, 0, 0],
         [0, 13, 20, 0, 0, 0]
    ],
    [
         [0, 0, 27, 34, 0, 52],
         [0, 0, 24, 0, 0, 49],
         [0, 16, 21, 0, 0, 46]
    ]
])


class test_check_solution(unittest.TestCase):

    # It should return true if cube is solved
    def test_solved(self):
        self.assertEqual(
            check_solution(initialize_cube()),
            True,
            "Should be true"
        )

    # It should return false if cube is not solved
    def test_not_solved(self):
        cube = initialize_cube()
        cube[0, 0, 0, 0] = 100
        self.assertEqual(check_solution(cube), False, "Should be false")


class test_initialize_cube(unittest.TestCase):

    # It should return a 3x3x3x6 array
    def test_initialize_cube_dimensions(self):
        cube = initialize_cube()
        self.assertEqual(cube.shape, (3, 3, 3, 6))

    # It should return a solved cube
    def test_initialize_cube_solved(self):
        self.assertEqual(
            check_solution(initialize_cube()),
            True,
            "Should return a solved cube"
        )

class test_rotate_slice(unittest.TestCase):

    # It should rotate on the FB axis successfully
    def test_rotate_slice_fb(self):
        cube = initialize_cube()
        np.testing.assert_array_equal(
            rotate_slice(cube[0, :, :], 0),
            rot90_fb_no_map
        )

    # It should rotate on the UD axis successfully
    def test_rotate_slice_ud(self):
        cube = initialize_cube()
        np.testing.assert_array_equal(
            rotate_slice(cube[:, 0, :], 1),
            rot90_ud_no_map
        )

    # It should rotate on the LR axis successfully
    def test_rotate_slice_rl(self):
        cube = initialize_cube()
        np.testing.assert_array_equal(
            rotate_slice(cube[:, :, 0], 2),
            rot90_lr_no_map
        )
class test_rotate(unittest.TestCase):

    # It should rotate on the FB axis position 0 successfully
    def test_rotate_fb(self):
        cube = initialize_cube()
        cube[0, :, :] = rot90_fb
        np.testing.assert_array_equal(
            rotate(initialize_cube(), 0, 0),
            cube
        )

    # It should rotate on the UD axis successfully
    def test_rotate_ud(self):
        cube = initialize_cube()
        cube[:, 0, :] = rot90_ud
        np.testing.assert_array_equal(
            rotate(initialize_cube(), 1, 0),
            cube
        )

    # It should rotate on the UD axis successfully
    def test_rotate_lr(self):
        cube = initialize_cube()
        cube[:, :, 0] = rot90_lr
        np.testing.assert_array_equal(
            rotate(initialize_cube(), 2, 0),
            cube
        )
class test_map_orientation(unittest.TestCase):

    def test_map_orientation_slice_fb(self):
        axis_map = get_axis_map(0)
        mapped_elements = map_color_to_orientation(rot90_fb_no_map, axis_map)
        np.testing.assert_array_equal(
            mapped_elements,
            rot90_fb
        )


if __name__ == '__main__':
    unittest.main()
