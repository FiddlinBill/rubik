import numpy as np

cube = np.zeros((6,3,3))
i = 1
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            cube[x][y][z] = i
            i += 1 
            print(cube[x][y][z])
print(cube)
white = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
])

red = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

yellow = np.array([
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
])

orange = np.array([
    [28, 29, 30],
    [31, 32, 33],
    [34, 35, 36]
])

green = np.array([
    [37, 38, 39],
    [40, 41, 42],
    [43, 44, 45]
])

blue = np.array([
    [46, 47, 48],
    [49, 50, 51],
    [52, 53, 54]
])



# There are 3 axis, Red, White, and Green. look at the center element of the axis, the closest 
# sheaf that rotates around the axis will be labelled 1, then next 2

def rotateCol(axis, direction):
   if (direction == "clockwise"):
       temp = white[:, col] 
 
     
print("Matrix =", matrix) 
