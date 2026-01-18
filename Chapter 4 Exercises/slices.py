cities = sorted(['detroit', 'atlanta', 'new york', 'chicago', 'san francisco'])

print('The first three items in the list are: ', end='')
for city in cities[0:3]:
    if city == cities[2]:
        print(city.title())
    else:
        print(f'{city.title()},', end=' ')

print('\nThree items from the middle of the list are: ', end='')
for city in cities[1:4]:
    if city == cities[3]:
        print(city.title())
    else:
        print(f'{city.title()},', end=' ')

print('\nThe last three items in the list are: ', end='')
for city in cities[-3:]:
    if city == cities[-1]:
        print(city.title())
    else:
        print(f'{city.title()},', end=' ')