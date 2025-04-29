'''def count_lower_upper(a):
    for ele in a:
        if (ele<='z' and ele>='a'):
            lower_count +=1
        elif (ele<='Z' and ele>='A'):
            upper_count +=1
    dict = { 'lower' : lower_count , 'upper' : upper_count}
    return dict
a = 'PrInce'
lower_count = 0
upeer_count = 0
print(count_lower_upper(a))'''
def count_lower_upper(s):
    lower_count = 0
    upper_count = 0
    for ele in s:
        if 'a' <= ele <= 'z':
            lower_count += 1
        elif 'A' <= ele <= 'Z':
            upper_count += 1
    result = {'lower': lower_count, 'upper': upper_count}
    return result

a = 'PrIncE'
print(count_lower_upper(a))

        
