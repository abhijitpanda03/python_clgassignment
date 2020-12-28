'''To add 'ing' at the end of a given string (length should be at least 3). If the given
string already ends with 'ing' then add 'ly' instead. If the string length of the given
string 5. is less than 3, leave it unchanged. Sample String : 'abc' Expected Result :
'abcing' Sample String : 'string' C 220.2 Expected Result : 'stringly''''

str=input("Enter a string: ")
if len(str)<3:
    print(str)
elif str.endswith('ing'):
    print(str+'ly')
else:
    print(str+"ing")