def fib(n):
    a = 1
    b = 2
    print(a)
    print(b)
    for i in range(0,(n-2)):
        c = a+b
        print(c)
        a = b
        b = c
        
n = int(input("enter number of terms you want in fibonacci series:"))
fib(n)