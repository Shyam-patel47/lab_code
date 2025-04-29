def check(lst):
    a = lst[::-1]
    if a==lst:
        return a

lst = ["madam","python","malayalam","12321"]
lst2 = list(filter(check, lst))
print(lst2)
