'''Write a python program to compute following series and take input x and n
I.1-x 2 /2! + x 3 /3!-x 4 /4!+------+x n /n!'''

from math import factorial
x=int(input("Enter x"))
n=int(input("Enter n"))
Sum=1
for i in range(2,n+1):
    Sum+=((-1)**(i+1))*((x**i)/factorial(i))
print(Sum)