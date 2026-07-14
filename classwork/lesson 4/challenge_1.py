#Ask user for 3 sides of a triangle
#calculate the area of triangle
#print out area

import math

#intake sides of triangle
side1 = float(input("Please enter first side of triangle: "))
side2 = float(input("Please enter second side of triangle: "))
side3 = float(input("Please enter third side of triangle: "))

#calculate area of triangle (heron's formula)
s = (side1 + side2 + side3)/2
area = math.sqrt(s*((s-side1)*(s-side2)*(s-side3)))

#prints the area
print("The area of the triangle is: {}".format(area))