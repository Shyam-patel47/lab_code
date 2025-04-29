#4.	Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. 
# The class should also have a provision to accept the data relevant to the shape.
class calculate:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2*(22/7)*self.radius
    def area(self):
        return (22/7)*(self.radius**2)
    
a = calculate(10)
print(f"circumference is: {a.circumference():.5f}")
print(f"area is: {a.area():.5f}")
