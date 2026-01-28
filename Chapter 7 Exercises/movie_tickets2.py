# 7-5(c): Movie Tickets

# Cost of ticket is determined by the user's age
# < 3 = free, >= 3 and <= 12 = 10, > 12 = 15

print('MOVIE TICKET PRICES')
print('-------------------')

prompt = "\nWould you like to run the program again?"
prompt += "\nEnter 'Y' or 'quit' (to exit): "

while True:
    user_age = int(input("\nEnter your age (or '-1' to exit): "))

    if user_age == -1:
        break
    elif user_age < 3:
        print('Ticket Cost: FREE')
    elif (user_age >= 3) and (user_age <= 12):
        print('Ticket Cost: $10.00')
    elif (user_age > 12):
        print('Ticket Cost: $15.00')