
#Kilometer to Miles Converter
#05 July 2020
#CTI-110 P5T1_KilometerConverter
#Martin Fields

#Pseudocode
#Conversion Factor Miles = Kilometers X 0.6214
#User Input # of KM to be converted
#Conversion Formula 
#Display Conversion

#Conversion Factor Km to Mi
CONVERSION_FACTOR = 0.6214

#Define Function Main
def main():
	#User Input # of KM to be converted
	km = float(input('Input # of Kilometers (Km) to be converted: ')) 	
	#Display the distance converted to miles
	show_miles(km)
	
#Define Function 2
def show_miles (km):
	#Conversion Formula (Miles = Kilometers X 0.6214)
	Mi = km * CONVERSION_FACTOR 
	#Display Conversion
	print(km,'kilometers equals', Mi, 'miles.')
main()
