#obtain length of given string
def length(a):
    if a == "":
        return 0
    else:
        return 1+length(a[1:])
    

a = input("enter the string : ")
print(length(a))
