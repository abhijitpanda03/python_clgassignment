'''Write a python program to find total mark of a student and take 5 diifrent subject along with
marks of 10 students using dictionary'''

dict1={}
for i in range(10):
    st='Student_' +str(i+1)
    dict1[st]={}
    for j in range(5):
        st1='Subject_'+str(j+1)
        a=int(input("Enter marks for {} of {}:".format(st1,st)))
        dict1[st][st1]=a
for std,mark in dict1.items():
    tot=0
    for k in mark:
        tot+=mark[k]
print("Total marks of {} is {}".format(std,tot))