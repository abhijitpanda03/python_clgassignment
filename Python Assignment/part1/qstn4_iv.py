'''Write a python program to compute following series and take input x and n
IV.x-x 3 /3! + x 5 /5!-x 7 /7!+x 11 /11!------+x n /n!'''

from math import factorial
num=input("Enter a number:")
x=sum([int(i) for i in num if int(i) in[0,4,6]])
n=sum([int(i) for i in num if int(i) in [5,7,9]])
s=0
result=0
for i in range(1,n+1,2):
    result+=(-1)**s*x**i/factorial(i)
    s+=1
print(result)