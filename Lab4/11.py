def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
def val(a):
    b = a - ((a**3)/fact(3)) + ((a**5)/fact(5)) - ((a**7)/fact(7))
    print(b)
    
    

a = int(input("enter the vale of angle in degrees : "))
val((a*3.14159)/180)