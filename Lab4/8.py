def factorial(a):
    factorial = 1
    for i in range(2,a+1):
        factorial *= i
    return factorial

a = int(input("enter a number:"))
print(factorial(a))
