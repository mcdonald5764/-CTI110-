# Displays a table from 0 to 20 of degrees in Celcius to Fahrenheit
# 10/17
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Darin McDonald
#

# Print headers to set up the table
# Use a for loop to loop the code from 0 to 20
# Calculate the formula
# Print both varibles in the table


print("Celcius\t\tFahrenheit")
print("--------------------------")

for x in range(21):
    formula = (9/5)*x + 32
    print(x,'\t\t',format(formula,'.1f'))
