#Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a given string is pangram or not, 
# through a user-defined function ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or 
# “Crazy Fredrick bought many very exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present 
# in the string and use <= to check whether alphaset is a subset of the given string.

def ispangram(a):
    print(a)
    count = 0
    s1 = set(a)
    for i in s1:
        if i.isalpha():
            count += 1
    if count == 26:
        return "The given string is a pangram"
    else:
        return"The given string is not a pangram"
    


a = "The quick brown fox jumps over the lazy dog"
b = "Crazy Fredrick bought many very exquisite opal jewels"
c = input("Enter third string for which you want to check pangram: ")
print(ispangram(a))
print(ispangram(b))
print(ispangram(c))
