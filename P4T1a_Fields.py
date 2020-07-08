#CTI-110
#P3T1a_FieldsMartin
#Martin Fields
#30June2020

#Pseudocode
#Turtle Setup, Speed, 
#User input # squares (nested loop min=100)
#Draw Square
#Decrease square size
#End turtle

#Turtle
import turtle

#Setup the turtle
ANIMATION_SPEED = 0
turtle.speed(0)

#Define square size
side = side_unit = 300

squares = 1

#User input number of squares (min 100)
while squares >= 1:
    squares = int(input('How many squares would you like?:'))
    if squares <=100:
        print('You must have at-least 100 square.')
        squares - int(input('How many squares would you like?:'))
    #Draw Squares
    else:
        for sq in range (squares):
            for count in range (4):
                    turtle.forward (side)
                    turtle.left (90)
                    #Decrease Square Size
                    side = side_unit - 3 * sq
                    turtle.hideturtle()
#End Turtle Graphic                   
turtle.done()


