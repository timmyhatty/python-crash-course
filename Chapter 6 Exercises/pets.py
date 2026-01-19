# 6-8: Pets

# Dictionaries for the pets
    # Stores the name, animal type, and owner's name
millie = {
    'name' : 'millie',
    'animal' : 'dog',
    'owner' : 'timothy',
}

maya = {
    'name' : 'maya',
    'animal' : 'dog',
    'owner' : 'timothy',
}

arnold = {
    'name' : 'arnold',
    'animal' : 'turtle',
    'owner' : 'jonathan',
}

maurice = {
    'name' : 'maurice',
    'animal' : 'horse',
    'owner' : 'the clown'
}

pets = [millie, maya, arnold, maurice]

# Printing the keys & values for each pet
print("List of Pets\n------------")
for pet in pets:
    print(f'{pet['name'].title()}')
    print(f'   Animal: {pet['animal'].title()}')
    print(f'   Owner: {pet['owner'].title()}')