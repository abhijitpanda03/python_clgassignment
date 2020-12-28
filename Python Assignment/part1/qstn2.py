'''Write a python program to find sum of product of corresponding digits of two any digit
number Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1'''

num1=input('Enter 1st number:')
num2=input('Enter 2nd number:')

sum=0
if len(num1)==len(num2):
    for i in range(0,len(num1)):
        product=int(num1[i])*int(num2[i])
        sum+=product
    print('sum of product',sum)

else:
    print('You have enterd wrong input, Both numbers must be of same length')