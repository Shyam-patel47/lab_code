#Generate 30 random numbers and put them in a list. 
# Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
lst = []
for i in range(0,30):
    lst.append(random.randint(-50,50))
negative = []
positive = []
for i in range(0,30):
    if lst[i]<0:
        negative.append(lst[i])
    else:
        positive.append(lst[i])
        
print("the positive numbers are: ", positive)
print("the negative numbers are: ", negative)