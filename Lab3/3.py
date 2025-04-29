#check on estring is in another or not
def check(str1,str2):
    if str2 in str1:
        print("YES")
    else:
        print("NO")

str1 = input("Enter first string:")
str2 = input("Enter second string:")
check(str1,str2)
