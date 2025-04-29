a = input("enter the string:" )
data ={}
for i in a:
    if i not in data:
        data[i] = a.count(i)
print(data)
