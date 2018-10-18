# Shows how much tuition will cost if it raised by 3% each year
# 10/17
# CTI-110 P4HW3 - Tuition Increase
# Darin McDonald
#

# Set the starting variable of 8000 for tuition
# Display how much tution is to the user
# Use a for loop to get 3% of the current tuition then update
# Display the new tuition and loop until 5 years have been displayed

tuition = 8000
print('Tuition this year cost $',format(tuition,'.2f'))

for x in range(1,6):
    increase = (tuition * 0.03)
    tuition = increase + tuition
    print('The year after that tuition will cost $',format(tuition,'.2f'))

    
