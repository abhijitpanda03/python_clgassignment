'''Write a python program to create a list of prime numbers as per given range'''

start=int(input("Enter start no:"))
end=int(input("Enter end no:"))
for i in range(start, end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)