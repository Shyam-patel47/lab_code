x1 = int(input("enter number x1:"))
y1 = int(input("enter number y1:"))
x2 = int(input("enter number x2:"))
y2 = int(input("enter number y2:"))
x3 = int(input("enter number x3:"))
y3 = int(input("enter number y3:"))
def line(x1,x2,x3,y1,y2,y3):
    if(((y2-y1)/(x2-x1))==((y3-y2)/(x3-x2))):
        print("they are on one line")
    else:
        print("they are not in one line")
line(x1,x2,x3,y1,y2,y3)
