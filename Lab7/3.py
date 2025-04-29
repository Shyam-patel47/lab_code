dic = {1:[['10',10000],['20',20000]], 2:[['30',30000],['40',40000]]}

for ele in dic.values():
    temp = []
    if isinstance(ele, list):
        for i in ele:
            for j in i:
                if isinstance(j, int):
                    temp.append(j)
    print("the minimum value is:",min(temp))
    print("the maximum value is:",max(temp))


