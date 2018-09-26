# This program tells the percentage of males and female students registered in a class
# 9/25
# CTI-110 P2HW2 - Male Female Percentage
# Darin McDonald
#

# Get a number value of male students from the user.
# Get a number value of female students from the user.
# Calculate the total amount of students
# Calcuate the amount of male students divided by the total number.
# Calculate the amount of female students divided by the total number.
# Display the percentages of students out of 100% to the user.

males = int(input("How many male students are registered for class?: "))
females = int(input("How many female are students registered for class?: "))

total = males + females
mPercent = int((males/total)*100)
fPercent = int((females/total)*100)

print("")
print("The percentage of registered students is",mPercent,"% males and",fPercent,"% females!")
