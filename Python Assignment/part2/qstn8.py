'''Write a python program to find 1 st ,2 nd and 3 rd largest and smallest numbers in a list 20 user
defined values.'''

nums=[]
for i in range(20):
    nums.append(int(input("Enter number_{}:".format(i+1))))
nums.sort()
print("largest:", nums[-3:])
print("smallest:", nums[:3])