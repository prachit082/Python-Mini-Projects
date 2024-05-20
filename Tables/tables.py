from tabulate import tabulate # type: ignore
data = [["Name", "Place", "Gender"], ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]
# For simple table
print(tabulate(data))

# For table with seperated headers
print(tabulate(data, headers='firstrow'))

# For table with grid format
print(tabulate(data, headers='firstrow', tablefmt='grid'))

# For table with fancy grid format
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))