#Create a class Weather that has a list containing weather parameters. Define an overloaded in operator 
# that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)
class Weather:
    def __init__(self, *args):
        self.weather_parameters = list(args)

    def __contains__(self, item):
        return item in self.weather_parameters

a = Weather('sunny', 'rainy', 'cloudy')
print(input('Enter the weather parameter to check: ') in a)
