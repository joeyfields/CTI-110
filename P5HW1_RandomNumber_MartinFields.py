#This program generates a random number between 1 and 100
#07 July 2020
#CTI-110 P5HW1- Random Numer
#Martin Fields

#Import necessart data files
#Display Main menu
#User guess
    #User input guess
#Check guess
    #guess loop
        #guess too low
        #guess too high
    #correct guess    
#Menu selection
        #generate random number
        #main menu choice
        #choice 1 "Play" 
        #choice 2 "Exit" 
#define program execution tree
#execute program



import random

#Display Main menu
def display_menu():
    print('MAIN MENU')
    print('-' * 24)
    print('\t ','1) Play Game')
    print('\t ','2) Exit')
    
#User guess
def user_guess():
    #User input guess
    user_input = int(input('Enter your guess: '))
    return user_input
  
        
#Check guess
def check_answer(random_number, guess):
    #guess loop
    while guess != random_number:
        #guess too low
        if random_number > guess:
            print('Too Low, try again')
            guess = int(input('Enter another guess: '))
        #guess too high
        elif random_number < guess:
            print('Too High, try again')
            guess = int(input('Enter another guess: '))
    #correct guess
    print('Great Guess!')
            
        
            
#Menu selection
def menu_choice():
    while True:
        #generate random number
        random_number = random.randrange(1, 100)
        #main menu choice            
        choice = int(input('Enter your selection: '))
        #choice 1 "Play"    
        if choice == 1:
            print('Guess a number between 1 and 100: ')
            guess = user_guess()
            check_answer(random_number, guess)
        #choice 2 "Exit"        
        elif choice == 2:
            print('Thank you for playing!')
            break
        else:
            print('Please enter selection between 1 and 2')
#define program execution tree
def main():
    display_menu()
    menu_choice()
#execute program
main()

