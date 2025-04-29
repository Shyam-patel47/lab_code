#to remove on string from another
def check(str1,str2):
    if str2 in str1:
        str1 = str1.replace(str2,"")
        print(str1)
    else:
        print(str1)

str1 = input("Enter first string:")
str2 = input("Enter second string:")
check(str1,str2)
