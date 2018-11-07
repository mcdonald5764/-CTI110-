# Convert inches to feet
# 10/30
# CTI-110 P5T2_FeetToInches 
# Darin McDonald
#

# Set a conversion value
# Get input from the user on how many feet there are
# Multiply feet and the conversion varible to get feet to inches
# Display how many inches per foot

inches_per_foot = 12


def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches.')


def feet_to_inches(feet):
    return feet * inches_per_foot

main()
