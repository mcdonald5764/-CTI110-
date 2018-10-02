# CTI-110 
# P3HW1 - Roman Numerals 
# Darin McDonald 
# 9/27
#

# Get an integer 1 through 10 from the user
# Check if the number input by the user is equal to 1
# Display the number as a Roman numeral
# Use an else if to check if the number is equal to 2 and so forth until 10
# Display the number as a Roman numeral
# Use an else to check if the user enters any integer besides 1 through 10
# Display an invalid number message


num = int(input("Please enter a number from 1 - 10: "))

if num == 1:
    print("The number 1 as a Roman numeral is displayed as I")

elif num == 2:
    print("The number 2 as a Roman numeral is displayed as II")

elif num == 3:
    print("The number 3 as a Roman numeral is displayed as III")

elif num == 4:
    print("The number 4 as a Roman numeral is displayed as IV")
    
elif num == 5:
    print("The number 5 as a Roman numeral is displayed as V")
    
elif num == 6:
    print("The number 6 as a Roman numeral is displayed as VI")

elif num == 7:
    print("The number 7 as a Roman numeral is displayed as VII")

elif num == 8:
    print("The number 8 as a Roman numeral is displayed as VIII")

elif num == 9:
    print("The number 9 as a Roman numeral is displayed as IX")

elif num == 10:
    print("The number 10 as a Roman numeral is displayed as X")

else:
    print("This is not a valid number! Please enter a number from 1 - 10")
