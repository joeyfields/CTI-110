#CTI-110
#P3HW1 - Color Mixer
#Martin Fields
#25June2020

#Primary color Mixer
#User input color 1.
Color1 = input('Enter 1st color: ')
#User input color 2.
Color2 = input('Enter 2nd color: ')
#Print Color Result.
if (Color1 == 'red' and Color2 == 'blue') or (Color1 == 'blue' and Color2 == 'red'):
    print('Color Mix red and blue = Purple')
elif (Color1 == 'red' and Color2 == 'yellow') or (Color1 == 'yellow' and Color2 == 'red'):
    print('Color Mix red and blue = Orange')
elif (Color1 == 'yellow' and Color2 == 'blue') or (Color1 == 'blue' and Color2 == 'yellow'):
    print('Color Mix red and blue = Green')
#Print "Error" if colors entered are not 2 of the following (Red,Blue,Yellow).
else:
    print('Error "Only colors Red, Blue, Green can be used"')
