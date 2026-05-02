# 8-6: City Names

# This program creates a function called city_country() that accepts a city and country as arguments. The city and country are then printed in a nice, formatted way.

def city_country(user_city, user_country):
    city_country_formatted = f'{user_city}, {user_country}'
    return city_country_formatted.title()

formatted_input = city_country('detroit', 'michigan')
print(formatted_input)

formatted_input = city_country('paris', 'france')
print(formatted_input)