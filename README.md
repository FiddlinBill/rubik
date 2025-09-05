A set of functions for intitiating and manipulating a 3x3x3 Rubik's Cube.

DEFINITIONS

AXES
0 FB Front Back axis
1 UD Up Down axis
2 LR Left Right axis

ELEMENTS
there are 3 x 3 x 3 = 27 elements in a rubik's cube and each element has 6
faces. Each element is specified as 1x6 array with a number indicating color
and position in the array indicating orientation:
Let the starting colors be in the given orientation:

0 u Up (White)
1 f Forward (Red)
2 l Left (Green)
3 b Back (Orange)
4 r Right (Blue)
5 d Down (Yellow)

[u, f, l, b, r, d]

CUBE DEFINITION
a cube may be represented as a 3x3x3x6 matrix because each of the 27 elements
of a Rubik's cube has 6 faces.
Now, imagine taking 3x3x1 vertical slices of the cube looking at the red face
with white facing up. Then, on the first slice, start at the top left and
read the elements from left to right downwards. Then, move on to the next
slice.
A number has been assigned to each visible face of an element.
Up/White: 0-9
Forward/Red: 10-18
Left/Green: 19-27
Back/Orange: 28-36
Right/Blue: 37-45
Down/Yellow: 46-54
CREATING AXIS MAPS
element definition: [u, f, l, b, r, d]


MAPPING COLORS TO NEW ORIENTATION AFTER ROTATION
on the FB axis, Clockwise (CW) rotation goes like this
l -> u-> 2
f -> f-> 1
d -> l-> 5
b -> b-> 3
u -> r-> 0
r -> d-> 4

CW on FB: [2, 1, 5, 3, 0, 4]

on the FB axis, Counter Clockwise (CCW) rotation goes like this
r -> u -> 4
f -> f -> 1
u -> l -> 0
b -> b -> 3
d -> r -> 4
l -> d -> 2

CCW on FB: [4, 1, 0, 3, 5, 2]

on the UD axis, CW rotation goes like this
u -> u -> 0
r -> f -> 4
f -> l -> 1
l -> b -> 2
b -> r -> 3
d -> d -> 5

CW on UD: [0, 4, 1, 2, 3, 5]

on the UD axis, CCW rotation goes like this
u -> u -> 0
l -> f -> 2
b -> l -> 3
r -> b -> 4
f -> r -> 1
d -> d -> 5

CCW on UD: [0, 2, 3, 4, 1, 5]

on the LR axis, CW rotation goes like this
b -> u -> 3
u -> f -> 0
l -> l -> 2
d -> b -> 5
r -> r -> 4
f -> d -> 1

CW on LR: [3, 0, 2, 5, 4, 1]

on the LR axis, CCW rotation goes like this
f -> u -> 1
d -> f -> 5
l -> l -> 2
u -> b -> 0
r -> r -> 4
b -> d -> 3

CCW on LR: [1, 5, 2, 0, 4, 3]


