lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = []
#lst2 = [ele**2 for ele in lst1 if ele%2 !=0]
for ele in lst1:
    if ele%2 !=0:   
       lst2.append(ele*ele)
print(lst2)
