import math
length_1 = float(input('What is the value of length in centimeters? '))
width = float(input('What is a width value in centimeters? '))
area_1 = length_1 ** 2
area_2=length_1 *width
area_circle= math.pi*length_1**2
print(f'The area of a square is: {area_1}')
print(f'The area of the rectangle is: {area_2}')
print(f'The area of the circle is {area_circle}')

length_2= float(input('What is the length of the rectangle? '))
width_1=float(input('What is the width of the rectangle? '))
area_2=length_2*width_1
print(f'The area of the rectangle is: {area_2}')

import math 
radius = float(input('What is the radius of the circle? '))
area= math.pi*radius**2
print(f'The area of the circle is {area}')
