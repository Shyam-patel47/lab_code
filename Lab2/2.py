a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
def findlarger(a,b,c):
    if a>b and a>c:
        print("largest is:",a)
    elif b>a and b>c:
        print("largest is:",b)
    else :
        print("largest is:",c)
def smaller(a,b,c):
    if a<b and a<c:
        print("smallest is:",a)
    elif b<a and b<c:
        print("smallest is:",b)
    else:
        print("smallest is",c)

findlarger(a,b,c)
smaller(a,b,c)