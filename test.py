import unittest
from rubik import check_solution, rotate
import numpy as np

# Here is a solved cube with the index, color and orientation definitions
solved_cube = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],           # 0 White Up
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # 1 Red North
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],  # 2 Green East
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],  # 3 Orange South
    [[37, 38, 39], [40, 41, 42], [43, 44, 45]],  # 4 Blue West
    [[46, 47, 48], [49, 50, 51], [52, 53, 54]]   # 5 Yellow Down
])

alt_solved_cube = np.array([
    [[46, 47, 48], [49, 50, 51], [52, 53, 54]],  # Yellow
    [[37, 38, 39], [40, 41, 42], [43, 44, 45]],  # Blue
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],  # Orange
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],  # Green
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # Red
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]            # White
])

unsolved_cube = np.array([
    [[54, 2, 3], [4, 5, 6], [7, 8, 9]],          # White
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # Red
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],  # Green
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],  # Orange
    [[37, 38, 39], [40, 41, 42], [43, 44, 45]],  # Blue
    [[46, 47, 48], [49, 50, 51], [52, 53, 1]]    # Yellow
])


class test_check_solution(unittest.TestCase):

    # It should return true if cube is solved
    def test_solved(self):
        self.assertEqual(check_solution(solved_cube), True, "Should be true")

    # It should return true if cube is solved in a different orientation
    def test_altsolved(self):
        self.assertEqual(check_solution(alt_solved_cube), True, "Should be true")

    # It should return false if the cube is not solved
    def test_unsolved(self):
        self.assertEqual(check_solution(unsolved_cube), False, "Should be false")

class test_rotate(unittest.TestCase):
    

    # It should return true if cube is solved
    def test_solved(self):
        solution =  np.array([
            [[19, 20, 21], [4, 5, 6], [7, 8, 9]],        # 0 White Up
            [[16, 13, 10], [17, 14, 11], [18, 15, 12]],  # 1 Red North
            [[46, 47, 48], [22, 23, 24], [25, 26, 27]],  # 2 Green East
            [[28, 29, 30], [31, 32, 33], [34, 35, 36]],  # 3 Orange South
            [[1, 2, 3], [40, 41, 42], [43, 44, 45]],     # 4 Blue West
            [[37, 38, 39], [49, 50, 51], [52, 53, 54]]   # 5 Yellow Down
        ])

        self.assertTrue((rotate(solved_cube, 1, 0, 1)==solution).all())


if __name__ == '__main__':
    unittest.main()
