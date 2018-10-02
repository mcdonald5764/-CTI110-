# This program compares the area of two rectangles and tells which of them if either
# is larger
# P3T1: Areas of Rectangles
# Darin McDonald
# 9/27/18

# Get the length and width of the first rectangle
# Get the length and width of the second rectangle
# Calculate the area of rectangle 1 and rectangle 2
# Display the area of both rectangles
# Check if the area of rectangle 1 is greater than rectangle 2
# Check if the area of rectangle 2 is greater than rectangle 1
# If neither they are both the same

rec1Length = float(input("Please enter the length of Rectangle 1: "))
rec1Width = float(input("Please enter the width of Rectangle 1: "))
rec2Length = float(input("Please enter the length of Rectangle 2: "))
rec2Width = float(input("Please enter the width of Rectangle 2: "))
print("")

area1 = rec1Length * rec1Width
area2 = rec2Length * rec2Width

print("The area of Rectangle 1 is", area1, "\nThe area of Rectangle 2 is",area2)
print("")

if area1 > area2:
    print("Rectangle 1 has the greater area!")

elif area2 > area1:
    print("Rectangle 2 has the greater area!")

else:
    print("Rectangle 1 and Rectangle 2 have the same area.")

    
