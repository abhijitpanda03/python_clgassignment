'''Write a python program to compute following series and take input x and n
III.1+x 2 /2! + x 4 /4!+x 6 /6!+------+x n /n!'''

from math import factorial
x=int(input("Enter x:"))
n=int(input("Enter n:"))
Sum=1
for i in range(2,n+1,2):
    Sum+=(x**i)/factorial(i)
print(Sum)