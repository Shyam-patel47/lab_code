# #8.	Implement a String class containing the following functions:
# # a.	Overloaded += operator function to perform string concatenation
# # b.	Method toLower() to convert upper case letters to lower case.
# # c.	Method toUpper() to convert lower case letters to upper case.
# class string:
#     def __init__(self,string):
#         self.string=string
    
#     def toLower(a):
#         return a.string.lower()
#     def toUpper(a):
#         return a.string.upper()
    
#     def __add__(self,other):
#         return (f'concated string is {self.string + other.string} and lower case is {toLower(self)} and upper case is {toUpper(self)}')
    
# s1 = string('Hello')
# print(s1.__add__(string('World')))
class string:
    def __init__(self, string):
        self.string = string
    
    def toLower(self):
        return self.string.lower()
    
    def toUpper(self):
        return self.string.upper()
    
    def __add__(self, other):
        return (f'concatenated string is {self.string + other.string} and lower case is {self.toLower()} and upper case is {self.toUpper()}')

s1 = string('Hello')
s2 = string('World')
print(s1 + s2)  # Use the overloaded + operator