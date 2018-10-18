# Uses the turtle object to draw the Trifoce from Zelda
# 10/17
# P4HW4
# Darin McDonald
#

import turtle

# Turns the turtle object around
turtle.right(180)

# Draws a Triangle shape
for x in (1,2,3):
    # Draws a Triangle shape inside the a triangle shape
    for x in (1,2,3):
        turtle.forward(100)
        turtle.right(120)
    turtle.forward(100)
    turtle.left(120)
