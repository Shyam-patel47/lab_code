def prime(a):
    count = 0
    for i in range(2,a):
        if(a%i == 0):
            count +=1
    if(count == 0):
        print("number is prime")
    else:
        print("number is not prime")

def perfect(a):
    count = 0
    for i in range(1,int((a/2)+1)):
        if(a%i == 0):
            count += i
    if(count == a):
        print("number is perfect")
    else:
        print("number is not perfect")

def armstrong(a):
    original = a
    digits = []
    summation = 0

    while a != 0:
        digits.append(a % 10)
        a //= 10

    for digit in digits:
        power = pow(digit, len(digits))
        summation += power

    if summation == original:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")

def automorphic(a):
    if(((a*a)%10) == a):
        print("number is automorphic")
    else:
        print("number is not automorphic")

    
a = int(input("Enter the number:"))
prime(a)
perfect(a)
armstrong(a)
#palindrome(a)
automorphic(a)
