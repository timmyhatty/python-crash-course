# 7-3: Multiples of Ten

# Ask the user for a number, then determine if the number is a multiple of 10
user_num = int(input('Please enter a number: '))
if user_num % 10 == 0:
    print(f'{user_num} is a multiple of 10')
else:
    print(f'{user_num} is not a multiple of 10')