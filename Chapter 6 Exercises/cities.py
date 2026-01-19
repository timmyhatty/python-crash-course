# 6-11: Cities

# Create a dictionary where the keys are the names of cities, and the values are a dictionary of facts about the city
cities = {
    'st louis' : {
        'country' : 'united states',
        'population' : 279_695,
        'fun fact' : 'Known as the Gateway To the West'
    },

    'tokyo' : {
        'country' : 'japan',
        'population' : 14_254_039,
        'fun fact' : 'Largest metropolis city in the world'
    },

    'amsterdam' : {
        'country' : 'netherlands',
        'population' : 933_680,
        'fun fact' : 'Oldest stock exchange; founded in 1602'
    },
}

# Print the name of the city and the facts about it
for city, city_info in cities.items():
    print(f'{city.title()}')
    print(f'  Country: {city_info['country'].title()}')
    print(f'  Population: {city_info['population']}')
    print(f'  Fun Fact: {city_info['fun fact']}\n')
