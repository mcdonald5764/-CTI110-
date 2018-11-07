# Convert Kilometers into Miles
# 10/30/18
# CTI-110 P5T1_KilometerConverter 
# Darin McDonald
#

# Set a variable for the conversion of kilometers
# Get input from the user
# Convert kilometers by multiplying the entered value and the conversion variable
# Display the kilometers in miles

conversion = 0.6124


def main():
    kilometers = float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

def show_miles(km):
    miles = km * conversion

    print(km, 'kilometers equals', format(miles, '.3f'), 'miles.')

    
main()
