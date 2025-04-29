names = [('Aryan', 'Devaarya', 'Om'),'Happy', 'Diya', ('Taksh', 'Shrey'), 'Rutvi']
count_boy = 0
count_girl = 0
for ele in names:
    if isinstance(ele,tuple):
        for i in ele:
            count_boy += 1
    else:
        count_girl += 1

print("the number of boys are:", count_boy)
print("the number of girl are:", count_girl)
