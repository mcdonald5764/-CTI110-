# Asks the amount of bugs caught in the span of a week and displays the total
# 10/17
# CTI-110 P4T2 - Bug Collector
# Darin McDonald
#

# Set the acc variable
# Use a for loop to get input of bugs amount from the user for 8 intervals 
# Add that amount to the total
# Once outside the loop display the total

total = 0

for day in range(1,8):
    print('Enter the bugs collect on day',day)

    bugs = int(input())

    total += bugs

print('You collected a total of', total, 'bugs.')
