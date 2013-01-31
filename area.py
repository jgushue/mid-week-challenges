# Jackie Gushue
# Mid-week Challenge

# Code calculates the area of a circle, rectangle, or triangle 
# depending on the user input

import math

shape = raw_input("Enter shape (\'circle\', \'rectangle\', or \'triangle\'):  ")

if shape == "circle":
	radius = float(raw_input("Enter radius of circle:  "))
	cir_area = math.pi*(radius**2)
	print ("Circle area = " + str(cir_area))
elif shape == "rectangle":
	length = float(raw_input("Enter length of rectangle:  "  ))
	width = float(raw_input("Enter width of rectangle:  "  ))
	rect_area = length * width
	print ("Rectangle area = " + str(rect_area))
else:
	base = float(raw_input("Enter base length of triangle:  "  ))
	height = float(raw_input("Enter height of triangle:  "  ))
	tri_area = 0.5*base*height
	print ("Triangle area = " + str(tri_area))

