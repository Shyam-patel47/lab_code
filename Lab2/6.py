a = int(input("enter number:"))

def check(a):
    count =0
    while(a>0):
        count +=1
        a//=10
    print(count)
check(a)
