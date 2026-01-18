# This program will use every function discussed in chapter 3 on a list.
cities = ['detroit', 'new york', 'chicago', 'atlanta', 'wisconsin']

# Printing the first item in the list
print(f"First Item in List: {cities[0].title()}")

# Printing the second to last item in the list
print(f"Second Item in List: {cities[-2].title()}")

# Modifying an element then printing the list
cities[2] = 'baltimore'
print(f"New List (after changing element 2): {cities}")

# Appending an item to the end of the list of cities
cities.append('san antonio')
print(f"New List (after appending city to end of list): {cities}")

# Inserting item to the middle of the list
cities.insert(3, 'miami')
print(f"New List (after inserting to the middle): {cities}")

# Removing using the fifth item in the list using the del statement
del cities[4]
print(f"New List (after deleting the fifth item): {cities}")

# Removing using the pop method (function)
cities.pop()
print(f"New List (after removing using .pop): {cities}")

# Removing using .remove (specific value)
cities.remove('detroit')
print(f"New List (after removing using .remove): {cities}")

# Printing list sorted (not changing the actual list)
print("New List (sorted, not altering original): ", sorted(cities))

# Printing list sorted (not changing the actual list) 
print("New List (sorted, not altering original): ", sorted(cities, reverse=True))

# Printing list sorted (altered)
cities.sort()
print(f"New List (altered original): {cities}")

# Printing list sorted (altered, reverse)
cities.sort(reverse=True)
print(f"New List (reversed, original altered): {cities}")