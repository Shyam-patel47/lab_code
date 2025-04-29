def calcuate(*a):
    for n in a:
        ex = str(n)
        ex1 = ex+ex
        ex2 = ex+ex+ex
        ex3 = ex+ex+ex+ex
        value = n + int(ex1) + int(ex2) + int(ex3)
        lst1.append(value)
    #     value = ((n) + ((n*10)+n) + ((n*100)+(n*10)+n) + ((n*1000)+(n*100)+(n*10)+n))
    #     lst1.append(value)
    
        
lst1 = []
a = [v for v in range(4,8)]
calcuate(*a)
print(lst1)
