'''Write a python program to find difference between average of all even numbers except
divisible by 4 and average of all odd numbers except divisible by 5 in a list of user defined 20
values?'''

nums=[]
even=[]
odd=[]
for i in range(20):
    nums.append(int(input("Enter number_{}:".format(i+1))))
for i in range(len(nums)):
    if nums[i]%2==0 and nums[i]%4!=0:
        even.append(nums[i])
    elif nums[i]%2!=0 and nums[i]%5!=0:
        odd.append(nums[i])
print(sum(even)/len(even)-sum(odd)/len(odd))