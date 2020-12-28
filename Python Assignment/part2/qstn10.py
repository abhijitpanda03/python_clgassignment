'''Write a python program to create a tuple of constents values like pi and exponent and use
them to find area of circle'''

from math import pi
const=(pi,2)
print("area=", const[0]*int(input("enter radius:"))**const[1])