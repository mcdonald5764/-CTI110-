# Uses the turtle object to draw the D and M intials
# 10/17
# P4T1B
# Darin McDonald
#

import turtle

# Starting variables
turtle.pensize(2)
turtle.left(90)


# Draws the D
for x in (1,2,3):
    turtle.forward(90)
    turtle.right(120)

# Picks up the pen, moves it, and sets it back down   
turtle.penup()
turtle.left(270)
turtle.forward(100)
turtle.pendown()

# Draws the M
turtle.left(60)
turtle.forward(80)
turtle.right(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.right(120)
turtle.forward(80)
turtle.left(120)

    

