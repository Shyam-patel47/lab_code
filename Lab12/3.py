#Write a program to create a class that can calculate the surface area and volume of a solid. 
#The class should also have a provision to accept the data relevant to the solid.

class calculate:
    def __init__(self, length , width , height):
        self.height = height
        self.width = width
        self.length = length
        
    def surface_area(self):
        return 6*(self.length**2)
    
    def volume(self):
        return self.length**3
    
a = calculate(7,7,7)
print(f"surface area is: {a.surface_area()}")
print(f"volume is: {a.volume()}")        