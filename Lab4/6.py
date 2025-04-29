#Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
a = 0
while a<24:
    if a==0:
        print("MIGHTNIGHT")
    elif a<12:
        print(a, "AM")
    elif a==12:
        print("NOON")
    elif a>12 and a<24:
        print(a-12, "PM")
    a+=1