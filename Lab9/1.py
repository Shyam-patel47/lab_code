#If a positive integer is entered through the keyword, write a recursive function to obtain 
# the prime factors of the number. 
# def is_prime(n):
#     if n == 2:
#         return True
#     c = 0
#     for i in range(2,n):
#         if n%i!=0:
#             c+=1
#     if c == n:
#         return True
from sympy import isprime

def prime_factors(a, count):
    if count == a:
        return primefactors
    else:
        if ((a%count==0 and isprime(count)) or a==2):
            primefactors.append(count)
    
    prime_factors(a, count+1)
        
    
primefactors = []
count = 2
a = int(input("Enter a number: "))
prime_factors(a,count)
print(primefactors)