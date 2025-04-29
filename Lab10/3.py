import random
lst1 = []
for i in range(0,10):
    lst1.append(int(random.randint(-15,15)))
print(lst1)
lst2 = list(map(lambda x:x**2,lst1))
print(lst2)
