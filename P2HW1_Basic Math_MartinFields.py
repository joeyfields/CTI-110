# Basic Math Calculator Add/Multiplication
# Date: 10Jun2020
# CTI-110 P2HW2 - Turtle Graphic
# Martin Fields

# User define varible #1.

number1 = int(input('Enter 1st number: '))

# User defined varible #2.
number2 = int(input('Enter 2nd number: '))

# Add the two varibles.
sol1 = number1 + number2

# Show the Addition solution.
print('{a}+{b}='.format(a=number1, b=number2),format(sol1, ',')) 

# Multiply the two varibles.
sol2 = number1 * number2

# Show the Multiplication product.
print('{a}*{b}='.format(a=number1, b=number2),format(sol2, ','))   

#Pseudocode:
    #user input1 {user inputs first number for problem}
    #user input2 {user inputs second number for problem}
    #sol1 is input1 + input2
    #sol2 is input1 * input2
    #Display solution of sol1
    #print(input #1 + input #2 = sol1)
    #Display product of sol2
    #print(input #1 8 input #2 = sol2)
