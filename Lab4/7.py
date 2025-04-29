def fact(a):
    if a == 0:
        return 1
    else:
        return a*fact(a-1)
    
def ncr(n,r):
    ncr = fact(n)/(fact(r)*fact(n-r))
    print(ncr)

def npr(n,r):
    npr = fact(n)/fact(n-r)
    print(npr)
    
n = int(input("enter the number n: "))
r = int(input("enter the number r: "))
print("the value of ncr is : ")
ncr(n,r)
print("the vale of npr is : ")
npr(n,r)