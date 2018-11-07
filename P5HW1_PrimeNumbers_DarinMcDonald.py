# Determines if a number is prime or not
# 10/30/18
# CTI-110 P5HW1 - Prime Numbers
# Darin McDonald
#

# Get an integer input from the user
# Determine if the number is prime by using the formula num1 % num2
# If the caluclations = 0 then the number is not prime so return false
# If not the number is prime so return true
# Display a statement to the user depending on what is_prime returns


def main():
    num = int(input("Please enter a number: "))

    if is_prime(num) == False:
        print("This number is not prime!")
    else:
        print("This number is prime!")
        
def is_prime(num):
    if num<2:
        return False
    for x in range(2,num):
        if num % x == 0:
            return False
        return True
            

main()
