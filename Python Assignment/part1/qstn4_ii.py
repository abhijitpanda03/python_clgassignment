'''Write a python program to compute following series and take input x and n
II.x-x 3 /3! + x 5 /5!-x 7 /7!+------+x n /n!'''

from math import factorial
x=int(input("Enter x:"))
n=int(input("Enter n:"))
Sum=0
s=2
for i in range(1,n+1,2):
    Sum+=((-1)**(s))*((x**i)/factorial(i))
    s+=1
print(Sum)