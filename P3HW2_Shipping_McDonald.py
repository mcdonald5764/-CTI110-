# CTI-110
# P3HW2 - Shipping Charges 
# Darin McDonald
# 9/27
#

# Get a number of pounds input from the user
# Check to see if the weight is less than or equal to 2
# Display the cost of the weight multipled by the first rate per pound
# Check to see if the weight is more than 2 but less than or equal to 6
# Display the cost of the weight multipled by the second rate per pound
# Check to see if the weight is more than 6 but less than or equal to 10
# Display the cost of the weight multipled by the third rate per pound
# If none of these are true the weight is greater than 10
# Display the cost of the weight multipled by the last rate per pound

print("Welcome to The Fast Freight Shipping Company!")
weight = float(input("How much does the package way in pounds(lbs)?: "))

if weight <= 2:
    print("This package will cost $", format(weight * 1.50, '.2f'), "to ship!")

elif weight > 2 and weight <= 6:
   print("This package will cost $", format(weight * 3.00, '.2f'), "to ship!")

elif weight > 6 and weight <= 10:
   print("This package will cost $", format(weight * 4.00, '.2f'), "to ship!")

else:
    print("This package will cost $", format(weight * 4.75, '.2f'), "to ship!")
