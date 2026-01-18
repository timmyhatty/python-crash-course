pizzas = ['3-Meat Treat', 'BBQ', 'Deep Dish']

for pizza in pizzas:
    print(f'I like {pizza} pizza!')

print('I really love pizza!')

# 4-11: My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]

pizzas.append('Hawaiian')
friend_pizzas.append('Veggie')

print('\nMy favorite pizzas are: ', end='')
for pizza in pizzas:
    if pizza == pizzas[-1]:
        print(pizza)
    else:
        print(f'{pizza},', end=' ')
    
print("My friend's favorite pizzes are: ", end=' ')
for pizza in friend_pizzas:
    if pizza == friend_pizzas[-1]:
        print(pizza)
    else:
        print(f'{pizza},', end=' ')
