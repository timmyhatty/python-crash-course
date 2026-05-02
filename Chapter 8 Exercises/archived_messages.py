# 8-11: Archived messages

# This program keeps a copy of sent messages even after they've been sent

"""
TO-DO:
    1. Start w/ the 8-10 program (sending_messages.py)
    2. Pass the texts_messages as a copy
    3. Print texts_messages and sent_messages, showing the original list has been preserved
"""

texts_messages = ['What are you doing?', 'How are you?', "Are you going to Jane's party today?"]
sent_messages = []

def show_messages(texts, sent_texts):
    print('Printing the sent messages')
    print('--------------------------------')
    while texts:
        current_message = texts.pop()
        print(current_message)
        sent_texts.append(current_message)

# This line is the change from 8-10 ([:] passes a copy of the list to the function)
show_messages(texts_messages[:], sent_messages)

print('\nPrinting the lists')
print('-------------------')
print(f'Original text messages list: {texts_messages}')
print(f'Sent messages list: {sent_messages}')