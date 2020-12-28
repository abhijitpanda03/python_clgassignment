'''Write a Python program to print and store ‘n terms of Fibonacci series in list'''

def fibonacci(num):
    fibo=[0,1]
    i=2
    while i<=num:
        fibonext = fibo[i-1]+fibo[i-2]
        fibo.append(fibonext)
        i+=1
    return fibo
num=int(input("Enter your number: "))-1
print(fibonacci(num))