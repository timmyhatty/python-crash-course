# 6-5: Rivers

rivers = {
    'nile' : 'egypt',
    'amazon river' : 'brazil',
    'yangtze' : 'china'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

print('\nRivers: ', end='')
for river in rivers.keys():
    if river != 'yangtze':
        print(f'{river.title()}, ', end='')
    else:
        print(f'{river.title()}')

print('Countries: ', end='')
for country in rivers.values():
    if country != 'china':
        print(f'{country.title()}, ', end='')
    else:
        print(f'{country.title()}')