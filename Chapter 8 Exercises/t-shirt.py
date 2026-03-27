# 8-3: T-Shirt

"""
TO-DO:
    - Write a function called make_shirt():
        * Accepts a size (of a shirt) and text that will be printed on the shirt
        * The function should print a sentence summarizing the size of the shirt & the message that will be printed on it
        * Call the function twice (2):
            * Once using positional arguments
            * Once using keyword arguments
"""

# Define the function make_shirt()
def make_shirt(size, message_on_shirt):
    """ This function will print information about a T-Shirt """

    # I decided to format the results like this, instead of a sentence, because it looks better
    print(f'Shirt Size: {size.upper()}\nThe Message Printed on the Shirt is: {message_on_shirt.upper()}')

make_shirt('lg', 'the beatles greatest hits')
print('--------------')
make_shirt(message_on_shirt='wayne state university', size='md')