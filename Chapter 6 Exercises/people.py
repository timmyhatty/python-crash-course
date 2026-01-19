# 6-7: People

ssmith = {
    'username' : 'ssmith',
    'first_name' : 'sam',
    'last_name' : 'smith',
    'age' : '34',
    'city' : 'atlanta',
}

swoods = {
    'username' : 'swoods',
    'first_name' : 'symere',
    'last_name' : 'woods',
    'age' : 31,
    'city' : 'philadelphia'
}

hpotter = {
    'username' : 'hpotter',
    'first_name' : 'harry',
    'last_name' : 'potter',
    'age' : 18,
    'city' : 'hogwarts'
}

people = [ssmith, swoods, hpotter]

for person in people:
    print(f'Username: {person['username']}')
    print(f'\tFirst Name: {person['first_name'].title()}')
    print(f'\tLast Name: {person['last_name'].title()}')
    print(f'\tAge: {person['age']}')
    print(f'\tCity: {person['city'].title()}\n')