# 4-12: More Loops

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('sushi')
friend_foods.append('gumbo')

print('My favorite foods are:', end=' ')
for food in my_foods:
    if food == my_foods[-1]:
        print(food.title())
    else:
        print(f'{food.title()},', end=' ')
        
print("My friend's favorite foods are:", end=' ')
for food in friend_foods:
    if food == friend_foods[-1]:
        print(food.title())
    else:
        print(f'{food.title()},', end=' ')