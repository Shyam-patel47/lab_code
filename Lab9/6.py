#a list have -ve and +ve values replace all -ve with 0
def change(a,i = 0):
    if len(a) == i:
        return a
    else:
        if a[i]<0:
            a[i] = 0
    return change(a,i+1)

a = [1,0,3,-5,4,8,-6,-7,22,14,-10]
print(change(a))
