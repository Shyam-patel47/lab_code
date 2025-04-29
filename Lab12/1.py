#Write a program to create a class that represents Complex numbers containing real and imaginary parts 
# and then use it to perform complex number addition, subtraction, multiplication and division.
class complex:
    def __init__(self,real1,ima1,real2,ima2):
        self.real1 = real1
        self.imaginary1 = ima1
        self.real2 = real2
        self.imaginary2 = ima2
        
    def add(self):
        rel = self.real1 + self.real2
        ima = self.imaginary1 + self.imaginary2
        print(f"Addition of complex numbers is {rel} + {ima}i") 

    def sub(self):
        rel = self.real1 - self.real2
        ima = self.imaginary1 - self.imaginary2
        print(f"Substraction of complex numbers is {rel} + {ima}i") 
       
    def mul(self):
        rel = self.real1 * self.real2 - self.imaginary1 * self.imaginary2
        ima = self.real1 * self.imaginary2 + self.imaginary1 * self.real2
        print(f"Multiplication of complex number is {rel} + {ima}i")

a = complex(2,3,4,5)
a.add()
a.sub()
a.mul()