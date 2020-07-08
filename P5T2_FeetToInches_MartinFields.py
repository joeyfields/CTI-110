#Feet to Inches Converter
#05 July 2020
#CTI-110 P5T2_FeetToInches
#Martin Fields

#Pseudocode
#Conversion Factor
#main function
	#User input # of feet
#convert feet to inches
#Feet to inches function
#execute program

#Conversion Factor Ft to In
INCHES_PER_FOOT = 12

#main function
def main():
	#User input # of feet
	feet = float(input('Enter "Feet" to be converted: '))
	
	#Convert Feet to Inches
	print(feet, 'equals', feet_to_inches(feet),'inches.')

#The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
	return feet * INCHES_PER_FOOT

#Execute program
main()
