#Write a function to create and return a list containing tuples of the form (x,x^2,x^3) for all x between 1 and given ending value (both inclusive).
def create_tuple(a):
    l = []
    for i in range(1,a+1):
        l.append((i,i**2,i**3))
    return l

a = int(input("Enter the ending value: "))
print(create_tuple(a))