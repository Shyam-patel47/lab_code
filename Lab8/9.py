#Write a program that defines a function count_alpha_digits() that accepts a string and calculates the 
# number of alphabets and digits in it. It should return these values as a dictionary.
def count_alpha_digits(p):
    alpha = 0
    digit = 0
    other = 0
    for i in p:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        else:
            other += 1
    return {"alphabets" : alpha, "digits" : digit, "other characters" : other}

a = input("Enter the string: ")
print(count_alpha_digits(a))