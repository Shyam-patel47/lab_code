#Write a recursive function to obtain average of all numbers present in a given list.
def average(a,sum,i):
    sum = sum + int(a[i])
    if i == len(a)-1:
        return sum/len(a)
    else:
        return average(a,sum,i+1)
        
a = list(input("Enter a list of numbers with ,: ").split(","))
sum = 0
i = 0
print("the average of give numbers is:", average(a,sum,i))