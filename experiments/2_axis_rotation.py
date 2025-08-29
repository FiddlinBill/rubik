from rubik import (
    check_solution,
    initialize_cube,
    rotate
)

cube = initialize_cube()

axis = 0
iteration = 0
cube = rotate(cube, 1, 0, "CCW")
print("wtf: ", check_solution(cube))
while not check_solution(cube):

    axis = 0 if axis > 1 else axis

    direction = "CW" if axis == 0 else "CCW"
    cube = rotate(cube, axis, 0, direction)
    axis += 1
    iteration += 1
    if iteration >= 8*30:
        break
    print("iteration: ", iteration)

print(cube)
