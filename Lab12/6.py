#Write a program to create a class Date that has a list containing day, month and year attributes. 
# Define an overloaded == operator to compare two Date objects.
class date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year 
    
    def __equal__(self,other):
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return 'Both dates are same'
        else:
            return 'Both dates are not same'
        
d1 = date(1,2,2023)
d2 = date(1,3,2023)
print(d1.__equal__(d2))
