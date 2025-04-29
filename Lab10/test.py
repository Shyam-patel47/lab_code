def prime(a):
    count = 0
    for i in range(2,a//2):
        if a%i == 0:
            count+=1
    #if count==0:
    #    return True
    #else:
    #    return False
    return True if count==0 else False
lst = [5,56,10,67,90,1010,78]
print(list(filter(lambda x :x%10==0,lst)))
print(list(filter(prime,lst)))
