#This program quizzes the user on basic Addition and Subtraction problems.
#06 July 2020
#CTI-P5HW2 - Math Quiz
#Martin Fields


#Pseudocode:
#Import necessary data files
#Display Main menu
#User input answer
    #Print problem
    #User input answer        
#Verify answer
    #Display message if correct
    #Display message if incorrect    
#Menu selection
        #Get random numbers
        #Choice one Addition                   
        #Choice two Subtraction 
        #Choice three exit program   
        #Incorrect value entered
#define "main" tree to execute program)
#Execute program



#Import necessary data files
import random
import math

#Display Main menu
def display_menu():
    print('Main Menu')
    print('-' * 24)
    print('1) Add Random Numbers')
    print('2) Subtract Random Numbers')
    print('3) Exit')
    
#User input answer
def get_user_answer(problem):
    #Print problem
    print(problem)
    #User input answer
    user_input = int(input('Enter your answer: '))
    return user_input
        
#Verify answer
def check_answer(answer, solution):
    #Display message if correct
    if answer == solution:
        print('Good Job!')
    #Display message if incorrect
    else:
        print('Incorrect')
    
#Menu selection
def menu_choice():
    while True:
        #Get random numbers
        number_one = random.randrange(1, 100)
        number_two = random.randrange(1, 100)
        #User menu choice
        choice = int(input('Enter your selection: '))
        #Choice one Addition
        if choice == 1:
            problem = str(number_one) + '+' + str(number_two)
            answer = get_user_answer(problem)
            solution = number_one + number_two
            check_answer(answer, solution)                   
        #Choice two Subtraction       
        elif choice == 2:
            problem = str(number_one) + '-' + str(number_two)
            answer = get_user_answer(problem)
            solution = number_one - number_two
            check_answer(answer, solution) 
        #Choice three exit program   
        elif choice == 3:
            print('Thank you for playing!')
            break
        #Incorrect value entered
        else:
            print('Please enter selection between 1 and 3')
#define "main" tree to execute program
def main():
    display_menu()
    menu_choice()
#Execute program
main()
