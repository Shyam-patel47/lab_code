lst1 = ['apple', 'banana', 'google', 'amazon', 'microsoft', 'intel']
lst2 = [ele for ele in lst1 if ele.count('a')!=0]
#for ele in lst1:
#    if ele.count('a')!=0:
#        lst2.append(ele)
print(lst2)
