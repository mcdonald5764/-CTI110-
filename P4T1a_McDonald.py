# Uses the turtle object to draw a square and a triangle
# 10/17
# P4T1A
# Darin McDonald
#

import turtle

# Draws a square
for x in (1,2,3,4):
    turtle.forward(50)
    turtle.left(90)

# Moves the turtle forward to draw the triangle to the side
turtle.forward(120)

# Draws the triangle
for x in (1,2,3):
    turtle.left(120)
    turtle.forward(70)

