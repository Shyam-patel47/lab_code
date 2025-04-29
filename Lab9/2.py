#convert entered number into binary
def binary(a,b):
    if a == 0:
        return b
    b.append(a%2)
    return binary(a//2,b)

a = int(input("enter the number:"))
b = []
binary(a,b)
b.reverse()
print("the binary of give number is:",b)
#print("the binary of given number is:",b.reverse())
