'''Writa a python program to store details of a student like
rollno,regdno,name,branch,stream,sem,phone no,address in dictionary and print the details
in cv format'''

field=["roll","regd","name","branch","stream","sem","phone","address"]
dict1={}
for f in field:
    dict1[f]=input("Enter {}: ".format(f))
print("I am {}. I am from {}.".format(dict1["name"],dict1["address"]))
print("Currently I am studying {} {} in {} sem.".format(dict1["stream"],dict1["branch"],dict1["sem"]))
print("Roll number and registration number are {}, {} respectively.".format(dict1["roll"],dict1["regd"]))
print("For further details call {}". format(dict1["phone"]))