lst1 = []
n = int(input("enter number of odd elements"))
for i in range(0,n):
    lst1.append(int(input()))

lst2 = []
n = int(input("enter number of even elements"))
for i in range(0,n):
    lst2.append(int(input()))
#lst1[2] = lst2
lst1.extend(lst2)
print(lst1)
# print(len(lst1))
lst1.sort()
print(lst1)