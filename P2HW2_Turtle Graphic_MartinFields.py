# Code Utiliizing the Turtle Graphic
# Date: 18Jun2020
# CTI-110 P2HW2 - Turtle Graphic
# Martin Fields

#This code will draw two squares that are filled, rotated 45 deg and connected at their apex
import turtle
turtle.hideturtle()
turtle.fillcolor('white')
#Square 1 Leg 1
turtle.begin_fill()
turtle.left(45)
turtle.forward(100)
# Square 1 Leg 2
turtle.left(90)
turtle.forward(100)
# Square 1 Leg 4 & Square 2 Leg 1
turtle.left(90)
turtle.forward(200)
#Draw Second Square
#Square 2 Leg 2
turtle.right(90)
turtle.forward(100)
# Square 2 Leg 3
turtle.right(90)
turtle.forward(100)
# Square 2 Leg 4 & Square 1  Leg 4
turtle.right(90)
turtle.forward(200)
turtle.end_fill()
