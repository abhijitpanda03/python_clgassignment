'''To get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself.'''

str=input("Enter a string: ")
result=str[0]
for c in str[1:]:
    if c != str[0]:
        result+=c
    else:
        result+='$'     
print(result)