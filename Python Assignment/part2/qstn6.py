'''Write a python program to store names of 10 fruits in strings and sort in alphabetical order'''

fruit=[]
for i in range(10):
    st=input("Enter name of fruit_{}:".format(i+1))
    fruit.append(st.strip())
fruit.sort()
print(fruit)