#Generate 20 random integers and store them in a list. 
#Accept a number from the user and print position of all occurrences of that number in the list.
import random
lst1 = []
for i in range(0,20):
    x=random.randint(1,100)
    lst1.append(x)
print(lst1)
a = int(input("enter number you want to find in list:"))
count =0
for i in range(0,20):
    if (lst1[i] == a):
        print("value found at", i)
    else:
        count +=1
    
if count == 20:
    print("value not found in list")
 