# A palindrome is a word or phrase that reads the same in both directions. 
# Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not. 
# Ignore spaces and case mismatch while checking for palindrome.
def ispalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            print("The given string is not a palindrome")
            return
    print("The given string is a palindrome")
    
a = input("Enter the string: ")
ispalindrome(a)