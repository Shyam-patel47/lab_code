# Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
lst1 = [('cake', 50), ('maggi', 20), ('pizza', 100), ('burger', 80), ('pasta', 70)]
lst2 = sorted(lst1, key=lambda x: x[1], reverse=True)
print(lst2)