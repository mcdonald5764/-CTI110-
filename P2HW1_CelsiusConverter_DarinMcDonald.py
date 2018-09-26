# This program gets a temperature in Celsius from the user and converts it to Fahrenheit
# 9/25
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Darin McDonald
#

# Get temperature value input from user.
# Use formula to convert the value from Celsius to Fahrenheit.
# Display the converted temperature.

temp = float(input("Please enter a temperature: "))

convertedTemp = (9/5)*temp + 32

print(temp,"C in Fahrenheit is",convertedTemp, "F")
