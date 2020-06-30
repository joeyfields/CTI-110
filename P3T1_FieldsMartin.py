# Find Area of a Rectangle
# Date: 10Jun2020
# CTI-110 P3T1 - Area of Rectangle
# Martin Fields

#Define Lenght and Width Rectangle 1 (R1).
R1L = float(input('Enter length of First rectange: '))
R1W = float(input('Enter width of First rectange: '))
#Calculate Area R1.
Area1 = R1L * R1W
#Define Lenght and Width Rectangle 2 (R2).
R2L = float(input('Enter length of Second rectange: '))
R2W = float(input('Enter width of Second rectange: '))
#Calculate Area R2.
Area2 = (R2L * R2W)
#Rectangle 1 has greater area.
if Area1 > Area2:
    print('First rectangle has a greater area!')
#Rectangle 2 has greater area.
elif Area1 < Area2:
    print('Second rectangle has a greater area!')
#The area of rectangle 1 and rectangle 2 are equal.
elif Area1 == Area2:
    print('Both rectangles have the same area!')

