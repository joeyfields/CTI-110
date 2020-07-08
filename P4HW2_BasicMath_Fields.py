# Basic Math Calculator Add/Multiplication
# Date: 05Jul2020
# CTI-110 P4HW2 - Turtle Graphic
# Martin Fields

#Pseudocode
#Create Loop
    #User Menu
    #Input menu selection
#User defined mathmatical values
    #User input 1st number
    #User input 2nd number3
#Display math equations answers
    #Addition equation
    #Display addition answer
    #Multiplication equation
    #Display multiplication answer
    #Subtraction equation
    #Display subtraction answer
#Menu option "Exit" and break loop 

#Create loop
while True:
    # User Menu
    print('---------MENU---------')
    print('1) Add Numbers')
    print('2) Multiply Numbers')
    print('3) Subtract')
    print('4) Exit')
    print('----------------------')

    # User defined mathmatical action.
    choice= input('Enter choice (1,2,3,4): ')
    stop = 4

# User defined values
    if choice in ('1','2','3'):
        #Input 1st number
        number1 = float(input('Enter 1st number: '))
        #Input 2nd number
        number2 = float(input('Enter 2nd number: '))
        print()

        # Display answer
        if choice == '1':
            #Addition equation
            sol1= number1 + number2
            #Display Addition answer
            print('{a} + {b} = '.format(a=number1, b=number2),format(sol1, ','))
        elif choice == '2':
            #Multiplication equation
            sol2= number1 * number2
            #Display multiplication answer
            print('{a} * {b} = '.format(a=number1, b=number2),format(sol2, ','))
        elif choice == '3':
            #Subtraction equation
            sol3= number1 - number2
            #Display subtraction answer
            print('{a} - {b} = '.format(a=number1, b=number2),format(sol3, ','))
    #Menu option "Exit" and break loop        
    elif choice == '4':
        print('This program will terminate.')
        break
             
    
    # If "choice" not values 1-4 print error message
    else:
        print(' Error invalid choice')
        

    




   

