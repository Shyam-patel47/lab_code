from math import sqrt, pow

a = float(input("enter the x cordinate of center:"))
b = float(input("enter the y cordinate of center:"))
r = float(input("enter the radius:"))

x = float(input("enter the x cordinate"))
y = float(input("enter the y cordinate"))

def check(a,b,r,x,y):
    distance = sqrt(pow((x-a),2)+pow((y-b),2))
    if(distance<r):
        print("point lies inside the circle")
    else:
        print("point is on or outside the circle")

check(a,b,r,x,y)
