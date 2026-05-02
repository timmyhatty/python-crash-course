# 8-9: Sending messages

# This program simulates sending messages, and moving sent messages to a list showing they've been sent


"""
TO-DO:
    1. Start with the program from messages.py (exercise 8-9)
    2. Create a new list called sent_messages (this list should be empty initially)
    3. Update the function show_messages to accept a new parameter called sent_texts
    4. As the messages are print, move them from the original list to the sent_texts list
    5. Print both lists to make sure the messages were moved
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

show_messages(texts_messages, sent_messages)

print('\nPrinting the lists')
print('-------------------')
print(f'Original text messages list: {texts_messages}')
print(f'Sent messages list: {sent_messages}')