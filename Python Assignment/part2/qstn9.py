'''Write a python pogram to find repeated numbers as well as frequency of repetition of
numbers in a list of 20 user defined values?'''

from collections import Counter

nums=[]
for i in range(20):
    nums.append(int(input("Enter number_{}:".format(i+1))))
c=Counter(nums)
for i in c:
    if c[i]>1:
        print(i,"is repeadted ", c[i], " times")