# 7-5: Movie Tickets

# Cost of ticket is determined by the user's age
# < 3 = free, >= 3 and <= 12 = 10, > 12 = 15

print('MOVIE TICKET PRICES')
print('-------------------')

user_age = int(input('Enter your age: '))
if user_age < 3:
    print('Ticket Cost: FREE')
elif (user_age >= 3) and (user_age <= 12):
    print('Ticket Cost: $10.00')
elif (user_age > 12):
    print('Ticket Cost: $15.00')