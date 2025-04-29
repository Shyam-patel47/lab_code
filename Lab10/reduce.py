from functools import reduce
def max(a,b):
    return a if a>b else b

l = [1,2,3,4,5,6,7]
print(reduce(max,l))
print(reduce(lambda x,y:x if x>y else y,l))
