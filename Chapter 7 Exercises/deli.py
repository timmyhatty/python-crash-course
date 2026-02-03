# 7-8: Deli

sandwich_orders = ['tuna', 'BLT', 'grilled cheeese', 'breakfast', 'italian']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich} sandwich')
    finished_sandwiches.append(current_sandwich)

print(f'\nHere is a list of the sandwiches that were made: {finished_sandwiches}')