#Take two lists of numbers. 
# Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).
n1 = int(input("enter the number of terms in list1:"))
lst1 = []
for i in range(0,n1):
    lst1.append(int(input()))
n2 = int(input("enter the number of terms in list2:"))
lst2 = []
for i in range(0,n2):
    lst2.append(int(input()))
lst3 = []
for i in lst1:
    if i not in lst2:
        lst3.append(i)

print(lst3)