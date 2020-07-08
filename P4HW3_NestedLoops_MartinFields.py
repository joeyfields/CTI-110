#Nested Loop to draw pattern
#5 July 2020
#CTI-110 P4HW3- Nested Loops
#Martin Fields

#Pseudocode
    #Create rows with "#"
    #Create spaces in rows between the #'s
    #Display the pattern

#Create rows with "#"
for row in range (6):
    print( '#', end='', sep='')
    #Create incrimental spaces in rows
    for spaces in range(row):
        print(' ', end='',sep='')
    #Display pattern
    print( '#', sep='' )
