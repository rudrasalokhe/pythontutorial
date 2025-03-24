# Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.

def casechecking(str):
    upper_count = 0 
    lower_count = 0 
    for char in str:
        if char.isupper():
            upper_count += 1 
        elif char.islower():
            lower_count += 1  
    return upper_count, lower_count
string = input("Enter your string: ")
upper, lower = casechecking(string)
print(f'The upper cases in string are: {upper}')
print(f'The lower cases in the string is: {lower} ') 