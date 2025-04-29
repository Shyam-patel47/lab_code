#Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it.
def creat_list(a,b):
    intersection = []
    for i in a:
        if i in b:
            intersection.append(i)
    return intersection            

s1 = input("Enter the first list: ")
s2 = input("Enter the second list: ")
print("intersection of both lists is:",creat_list(s1,s2))