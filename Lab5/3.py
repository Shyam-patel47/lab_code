#Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list
import random
lst = []
for i in range(0,50):
    x = lst.append(random.randint(1,30))
print(lst)

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             lst.remove(lst[j])
unique_lst = set(lst)
print("unique numbers are")
print(unique_lst)