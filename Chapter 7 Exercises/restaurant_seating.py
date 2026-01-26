# 7-2: Restaurant Seating

# Ask the user for the total number of people in their group
# If their group is > 8, they must wait for a table, otherwise, they may sit immediately

group_size = int(input('Welcome to our restaurant!\nHow many people are in your group: '))
if group_size > 8:
    print("Thank you! You'll have to wait for a table.")
else:
    print(f'Thank you! A table is ready for your group of {group_size}.')