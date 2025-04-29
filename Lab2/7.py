a = int(input("enter number:"))

def check(a):
    if(a%4 == 0):
        if(a%100==0):
            if(a%400==0):
                print(a,"is leap year")
            else:
                print(a,"is not leap year")
        else:
            print(a,"is leap year")
    else:
        print(a,"is not leap year")
check(a)
