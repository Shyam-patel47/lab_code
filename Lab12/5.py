#Write a program that creates and uses a Time class to perform various time arithmetic operations.
class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second 
    
    def __add__(self,other):
        return (f'added time is {self.hour + other.hour}:{self.minute + other.minute}:{self.second + other.second}')
    
    def __sub__(self,other):
        return (f'subtracted time is {self.hour - other.hour}:{self.minute - other.minute}:{self.second - other.second}')
    
t1 = time(1,2,3)
t2 = time(4,5,6)
print(t1 + t2)
print(t2 - t1)