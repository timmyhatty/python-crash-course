# 6-9: Favorite Places

# Dictionary that uses names as keys, and a list of favorite places as the values
favorite_places = {
    'timothy' : ['netherlands', 'las vegas', 'lafayette'],
    'tom' : ['japan', 'united kingdom'],
    'martin' : ['chicago', 'cairo']
}

# Print the names of each person and their favorite places
for person, places in favorite_places.items():
    print(f"{person.title()}'s Favorite Places are:")
    for place in places:
        print(f'   {place.title()}')