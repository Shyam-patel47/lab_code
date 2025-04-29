#Write a recursive function that reverses the list of numbers that it receives.
def reverse(a,b,i):
    b.append(a[len(a)-1-i])
    if len(a)-1-i == 0:
        return b
    else:
        return reverse(a,b,i+1)

a = list(input("Enter a list of numbers with ,: ").split(","))
b = []
i = 0
print(reverse(a,b,i))