a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
def check(a,b,c):
    if((a+b+c)==180):
        print("valid triangle")
    else:
        print("not valid triangel")
        
check(a,b,c)
