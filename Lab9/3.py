#A string is entered through the keyboard. Write a recursive function that counts the 
# number of vowels in this string.
def vowel_count(a,i,count):
    if i == len(a):
        return count
    if a[i] in ['a','e','i','o','u']:
        return vowel_count(a,i+1,count+1)
    else:
        return vowel_count(a,i+1,count)
    

a = input("Enter a string: ")
b = vowel_count(a.lower(),0,0)
print("the number of vovels in the string is:",b)