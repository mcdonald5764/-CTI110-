# This program asks for an amount of budgeted money and tells the user if they
# are over or under budget and how much if they are
# 10/17
# CTI-110 P4HW1 - Budget Analysis
# Darin McDonald
#

# Set intial variables to start off the program (the loop, total amount, budget)
# Use a while loop to create an infinite loop until the varible = false
# Get input of expense from the user and add it to a total varible
# Check to see if the user input 0 and if so stop the loop, if not keep going
# Outside of the loop check to see if the loop has stopped
# Using the total variable see if  it is over the budget variable
# If so use a formula to calulate how much and display the information
# If not use a formula to see how much under and display the information


looping = "true"
total = 0
budget = float(input("Please set an amount of money budgeted for this month! $"))

while looping == "true":
    expense = float(input("Enter monthly expenses or type 0 to finish $"))
    total += expense
    if expense == 0:
        looping = "false"

if looping != "true":
    print()
    if total > budget:
        print("This month you've spent a total of $",format(total,'.2f'))
        overBudget = total - budget
        print("You are $",format(overBudget,'.2f'),"over budget!")
    else:
        print("This month you've spent a total of $",format(total,'.2f'))
        underBudget = budget - total
        print("You are $",format(underBudget,'.2f'),"under budget!")
