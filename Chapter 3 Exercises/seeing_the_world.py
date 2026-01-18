# This program will print a list of places I'd like to visit in a variety of different ways

places_to_visit = ['paris', 'netherlands', 'cedar point', 'disneyworld', 'japan']
print(f'\nList in Original Order: {places_to_visit}')

print(f'\nSorted List (without altering original order): ', sorted(places_to_visit))
print(f"List in Original Order (to show it wasn't altered): {places_to_visit}")

print(f"\nList in Reverse Order (without altering original order): ", sorted(places_to_visit, reverse=True))
print(f"List in Original Order (to show it wasn't altered): {places_to_visit}")

places_to_visit.reverse()
print(f"\nList in Reverse Order: {places_to_visit}")
places_to_visit.reverse()
print(f"List in Reverse Order (changing it back to the original): {places_to_visit}")

places_to_visit.sort()
print(f"\nList Sorted (alphabetically): {places_to_visit}")
places_to_visit.sort(reverse=True)
print(f"List Sorted (reverse alphabetical order): {places_to_visit}")