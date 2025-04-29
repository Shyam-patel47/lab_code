def total(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
def average(*a):
    return total(*a)/len(a)

lst = []
for i in range(5):
    lst.append(int(input("enter number: ")))

print("total is:"total(*lst))
print("average is:"average(*lst))
