#This program calculates the number of bugs collected in 5 days.
#30June2020
#CTI-110-P4T2- Bug Collector
#Martin Fields

#Pseudocode
#Define Max number of entrires
#Begin Accumulator
#Bug Collector Explaination
#Get numbers to accumulate
#Display total Bugs collected.


#This program accumulates the total numbers of Bugs Collected over five days.
#Of bugs collected entered by user.

#Define Max number of entrires
MAX = 5

#Begin Accumulator
total = 0.0

#Bug Collector Explaination
print('This program calculates total bugs collected,over five days')
print()

#Get numbers to accumulate
for counter in range(MAX):
    number = int(input('Enter # of Bugs Collected Today: '))
    total = total + number
    
#Display total Bugs collected.    
    print('The total bugs collected in five days: ', total)
