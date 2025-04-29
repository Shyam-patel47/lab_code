dic1 = {'apple':70,'banana':50, 'watermelon':100}
dic2 = {'banana':10,'apple':5, 'watermelon':15}
total = {}
for k,i in dic1.items():
    for e,j in dic2.items():
        if k==e:
            #if k not in total:
                total[k] = i*j
print(total)
bill = []
for i in total.values():
    bill.append(i)
print("final bill is:", sum(bill))
