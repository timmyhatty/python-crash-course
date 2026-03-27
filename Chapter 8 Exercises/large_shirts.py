# 8-4: Large Shirts
# This is a modification of exercise 8-3

"""
TO-DO:
    - Modifications to make_shirt():
        * Modify make_shirt() so that shirts are large by default
        * Modify make_shirt() so the default message is "I love Python!"
    - Call the function twice (2):
        * A large shirt w/ the default message
        * A medium shirt with the default message
        * A shirt of any size w/ any message
"""

# Define the function make_shirt()
def make_shirt(size='LG', message_on_shirt='I love Python!'):
    """ This function will print information about a T-Shirt """

    # I decided to format the results like this, instead of a sentence, because it looks better
    print(f'Shirt Size: {size.upper()}\nThe Message Printed on the Shirt is: {message_on_shirt.upper()}')
    print('-----------\n')

make_shirt()
make_shirt(size='md')
make_shirt('xs', 'THE BEATLES: GREATEST HITS')