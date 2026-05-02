# 8-9: Messages

# This program passes of list of short text messages to a function; the function will print each message.

"""
TO-DO:
    1. Define the function show_messages(), which accepts a list as an argument
        - Within the function, print each text message on a newline
    2. Create a list of text messages
    3. Call the show_messages() function, passsing the list of text messages to the function
"""

def show_messages(texts):
    for text_message in texts:
        print(text_message)

texts_messages = ['What are you doing?', 'How are you?', "Are you going to Jane's party today?"]
show_messages(texts_messages)