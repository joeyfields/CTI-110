# Basic Math Calculator Add/Multiplication
# Date: 10Jun2020
# CTI-110 P2HW2 - Turtle Graphic
# Martin Fields

# User Menu
print('---------MENU---------')
print('1) Add Numbers')
print('2) Multiply Numbers')
print('3) Subtract')
print('4) Exit')
print('----------------------')

# User defined mathmatical action.
choice= input('Enter choice (1,2,3,4): ')

# User defined values
if choice in ('1','2','3'):
    number1 = float(input('Enter 1st number: '))
    number2 = float(input('Enter 2nd number: '))

#Math equations    
    sol1= number1 + number2
    sol2= number1 * number2
    sol3= number1 - number2

# Display answer
if choice == '1':
    print('{a}+{b}='.format(a=number1, b=number2),format(sol1, ','))
elif choice == '2':
    print('{a}*{b}='.format(a=number1, b=number2),format(sol2, ','))
elif choice == '3':
    print('{a}-{b}='.format(a=number1, b=number2),format(sol3, ','))
elif choice == '4':
    print('This program will terminate.')
# If "choice" not values 1-4 print error message
else:
    print(' Error invalid choice')
    




   

