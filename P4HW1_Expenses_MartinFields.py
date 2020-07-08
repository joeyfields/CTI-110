#CTI-110
#P4HW1 - Expens200es
#Martin Fields
#30June2020

#Pseudocode
#Expense Calculator
#Enter starting amount
#Track number of expense entries
#Track running balance
#Loop control variable
#Add to counter
#Get expenses
#Enter another expense?
#Calculate balance
#Display beggining amount and number of expenses entered
#Display amount remaining after expenses.


#Expense Calculator

#Enter starting amount
Begin_Balance = float(input('Enter starting amount in account?: '))

#Track number of expense entries
count = 0
#Track running balance
total = 0.0

#Creste a variable to control the loop.
keep_going = 'y'


if keep_going == 'y':
    while keep_going == 'y':
        #Same as entry_num plus 1
        count += 1
        #Get Expense
        expense = float(input('Enter expense ' +str(count) +':'))
       
        #Query about additional expenses
        keep_going = input('Do you wnat to enter another expense? (y/n)')
        #Calculate balance
        total = Begin_Balance - expense



    else:
        #Display beggining amount
        print('Amount in account before expense subtraction $', Begin_Balance)
        print('Number of expenses entered: ', count)
        
        #Display number of expenses entered
        print('Amount in account AFTER expenses subtracted is $', total)       
                      
