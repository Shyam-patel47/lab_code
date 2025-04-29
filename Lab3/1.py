#find vovel in string
def vovel(str1):
    count = 0
    count += str1.count('a')
    count += str1.count('e')
    count += str1.count('i')
    count += str1.count('o')
    count += str1.count('u')
    print(count)

str1 = input("enter a string:")
vovel(str1)
