# Write a program that defines a function convert() that receives a string containing a sequence of 
# whitespace separated words and returns a string after removing all duplicate words and sorting them alphanumerically. 
# Hint: use set(), list () , sorted(), join().
def convert(a):
    l = a.split()
    l = list(set(l))
    l = sorted(l)
    return " ".join(l)

a = input("Enter the string with whitespace seprated words: ")
print(convert(a))