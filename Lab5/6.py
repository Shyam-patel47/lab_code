lst1 = []
n = int(input("enter the number of terms:"))
for i in range(0,n):
    lst1.append(int(input()))

for i in range(0,n):
    lst1[i] = round((lst1[i]-32)*(5/9),2)

print("the temperature in celsius are as beloiw:")
print(lst1)
