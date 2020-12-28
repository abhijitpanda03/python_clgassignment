'''Write a python program to find sum of product of corresponding even digits of first any digit
number and corresponding odd digit of any digit number Such as n=1234 m=4567
output=4*7+2*5'''

num1=input("Enter first number:")
num2=input("Enter second number:")

even=[int(i) for i in num1 if int(i)%2==0]
odd=[int(i) for i in num2 if int(i)%2!=0]
sum=0
for (i,j) in zip(even,odd):
    sum+=int(i)*int(j)

print(sum)