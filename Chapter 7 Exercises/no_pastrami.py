# 7-9: No Pastrami

sandwich_orders = ['pastrami', 'tuna', 'BLT', 'pastrami', 'grilled cheeese', 'breakfast', 'pastrami', 'italian']
finished_sandwiches = []

print('The deli has run out of pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich} sandwich')
    finished_sandwiches.append(current_sandwich)

print(f'\nHere is a list of the sandwiches that were made: {finished_sandwiches}')
