import unittest
from rubic import checkSolution

solvedCube = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], #Yellow
 [[10, 11, 12], [13, 14, 15], [16, 17, 18]], #Red
 [[19, 20, 21], [22, 23, 24], [25, 26, 27]], #Blue
 [[28, 29, 30], [31, 32, 33], [34, 35, 36]], #Green
 [[37, 38, 39], [40, 41, 42], [43, 44, 45]], #Orange
 [[46, 47, 48], [49, 50, 51], [52, 53, 54]]] #White

 altSolvedCube = [[46, 47, 48], [49, 50, 51], [52, 53, 54]], #White
 [[37, 38, 39], [40, 41, 42], [43, 44, 45]], #Orange 
 [[28, 29, 30], [31, 32, 33], [34, 35, 36]], #Green
 [[19, 20, 21], [22, 23, 24], [25, 26, 27]], #Blue
 [[10, 11, 12], [13, 14, 15], [16, 17, 18]], #Red
 [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]] #Yellow

unSolvedCube = [[[54, 2, 3], [4, 5, 6], [7, 8, 9]], #Yellow
 [[10, 11, 12], [13, 14, 15], [16, 17, 18]], #Red
 [[19, 20, 21], [22, 23, 24], [25, 26, 27]], #Blue
 [[28, 29, 30], [31, 32, 33], [34, 35, 36]], #Green
 [[37, 38, 39], [40, 41, 42], [43, 44, 45]], #Orange
 [[46, 47, 48], [49, 50, 51], [52, 53, 1]]] #White

# It should return true if cube is solved
class TestCheckSolution(unittest.TestCase):
    def test_solved(self):
        self.assertEqual(checkSolution(solvedCube), True, "Should be true")

# It should return true if cube is solved in different orientation
class TestCheckSolution(unittest.TestCase):
    def test_solved(self):
        self.assertEqual(checkSolution(altSolvedCube), True, "Should be true")
    
# It should return false if the cube is not solved
class TestCheckSolution(unittest.TestCase):
    def test_solved(self):
        self.assertEqual(checkSolution(unSolvedCube), False, "Should be false")



if __name__ == '__main__':
    unittest.main()