# 7-5(a): Movie Tickets

# Cost of ticket is determined by the user's age
# < 3 = free, >= 3 and <= 12 = 10, > 12 = 15

print('MOVIE TICKET PRICES')
print('-------------------')

prompt = "\nWould you like to run the program again?"
prompt += "\nEnter 'Y' or 'quit' (to exit): "

active = 'y'
while True:
    if active == 'y':
        user_age = input("\nEnter your age: ")

        if user_age == 'quit':
            break
        else:
            if int(user_age) < 3:
                print('Ticket Cost: FREE')
            elif (int(user_age) >= 3) and (int(user_age) <= 12):
                print('Ticket Cost: $10.00')
            elif (int(user_age) > 12):
                print('Ticket Cost: $15.00')

            active = input(prompt).lower()
    else:
        break