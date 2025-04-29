def check(a):
    alphabet = 0
    digit = 0
    for i in a:
        if('A'<=i<='Z' or 'a'<=i<='z'):
            alphabet +=1
        elif('0'<=i<='9'):
            digit +=1
    print("the alphabet is:", alphabet )
    print("the digit is:", digit)


a = input("Enter the string:")
check(a)
