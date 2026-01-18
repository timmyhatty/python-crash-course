#4-13 Buffet

restaurant_food = ('chicken alfredo', 'gumbo', 'shrimp fried rice', 'spaghetti')
print('The restaurant offers the following food: ', end ='')
for food in restaurant_food:
    if food == restaurant_food[-1]:
        print(food.title())
    else:
        print(f'{food.title()},', end=' ')

restaurant_food = sorted(('chicken alfredo', 'gumbo', 'pie', 'chicken nuggets'))
print('The menu has changed! The new items are: ', end='')
for food in restaurant_food:
    if food == restaurant_food[-1]:
        print(food.title())
    else:
        print(f'{food.title()},', end=' ')