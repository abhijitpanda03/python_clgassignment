'''Write a python program compute following series and take a numbers num as input
x-x 3 /3! + x 5 /5!-x 7 /7!+------+x n /n!
where x=sum of all even digits except 2 and 8
and n= sum of all odd digits except 1 and 3'''

from math import factorial
num=input( "Enter a number:" )
x=sum([int(i) for i in num if i in ( '0 ' , ' 4 ' , ' 6 ' ) ])
n=sum([int(i) for i in num if i in ( '5 ' , ' 7 ' , ' 9 ' ) ])
print(sum([(-1)**i*x**j/factorial(j) for i,j in enumerate(range(1,n+1,2))]))