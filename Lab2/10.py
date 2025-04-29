a = int(input("enter number:"))
b = int(input("enter number:"))
def check(a,b):
    parameter = 2*(a+b)
    area = a*b
    if(area>parameter):
        print("area is greater")
    else:
        print("parameter is greater")
check(a,b)
