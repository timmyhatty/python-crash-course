# 7-4: Pizza Toppings

# Prompt the user to enter pizza toppings, print the topping has been added
# If 'quit' is entered, end the program

prompt = "Enter a topping you'd like to add"
prompt += "\nEnter 'quit' if you'd like to end the program:  "
active = True
END = 'quit'

while active:
    add_topping = input(prompt)

    if add_topping == END:
        active = False
    else:
        print(f'Adding {add_topping} to your pizza!')