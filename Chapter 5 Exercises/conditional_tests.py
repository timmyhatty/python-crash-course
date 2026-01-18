# 5-1: Conditional Tests

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

friends = ['carmella', 'jalen', 'ethan']
name_of_friend = 'aliyah'
print("\nIs name_of_friend in friends [list]? I predict False")
print(name_of_friend in friends)

print('\nIs jalen in friends [list]? I predict True')
print('jalen' in friends)

print('\nIs ethan not in friends [list]? I predict False')
print('ethan' not in friends)

age_of_consent = 16
print('\nIs the age of consent less than 16? I predict False')
print(age_of_consent < 16)

my_age = 26
print('\nAm I 26 years old? I predict True')
print(my_age == 26)

favorite_food = 'greek yogurt bowl'
print('\nIs your favorite food a "Greek Yogurt Bowl"? I predict True')
print(favorite_food.title() == 'Greek Yogurt Bowl')

print('\nIs "Timothy" equal to "yogurt"? I predict False')
print('Timothy' == 'yogurt')

print('\nIs "Timothy" (lowercase) equal to "timothy"? I predict True')
print('Timothy'.lower() == 'timothy')