#CTI-110
#P3T1b_FieldsMartin
#Martin Fields
#30June2020

#Pseudocode
#Import Turtle
#Turtle Setup, Speed, 
#Draw First Inital
#Draw Second inital
#End turtle

#Import Turtle
import turtle

#Setup the turtle
ANIMATION_SPEED = 0
turtle.speed(0)

#Draw First Inital
turtle.left (90)
turtle.forward (50)
turtle.right (135)
turtle.forward (30)
turtle.left (90)
turtle.forward (30)
turtle.right (135)
turtle.forward (50)
turtle.penup()

#Position Turtle for second Inital
turtle.left (90)
turtle.forward (20)
turtle.pendown()

#Draw Second Inital
turtle.left (90)
turtle.forward (50)
turtle.right (90)
turtle.forward (30)
turtle.right (180)
turtle.penup()
turtle.forward (30)
turtle.left (90)
turtle.pendown()
turtle.forward (20)
turtle.left (90)
turtle.forward (20)
turtle.hideturtle()
#End Turtle Graphic                   
turtle.done()


