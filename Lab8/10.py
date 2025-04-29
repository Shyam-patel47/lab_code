#Write a program that defines a function called frequency() which computes the frequency of words present 
# in a string passed to it. The frequencies should be returned in sorted order of words in the string
def frequency(b):
    b = b.lower()
    dic = {}
    for i in b:
        dic[i] = b.count(i)
    
    sorted_dic = str(sorted(dic.items()))
    return sorted_dic

a = input("Enter the string: ")
print(frequency(a))