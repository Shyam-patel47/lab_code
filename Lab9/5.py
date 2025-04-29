# calculate a^b where a and b received through keybord
def cal(a,b):
    if b == 0:
        return 1
    else:
        c = a*cal(a,b-1)
    return c
    
a =  int(input("enter the base:"))
b = int(input("enter the power:"))
print(cal(a,b))
