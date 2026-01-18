# This program creates a guest list and sends a message to invite each guest to the party.

guest_list = ['frieren the mage', 'fern the mage', 'stark the warrior']

# Invite messages
print(f"Hello {guest_list[0].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[1].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[2].title()}, you've been invited to the Royal Dinner!")
print('The number of people invited: ', len(guest_list))
print()

# Unfortunately Frieren can not make the dinner, Heiter is her replacement
cant_attend = guest_list.pop(0)
print(f'Unfortunately, {cant_attend.title()} cannot attend the dinner.')
guest_list.insert(0, 'heiter the priest')
del cant_attend

# New invite messages
print()
print('THE NEW INVITEES')
print('----------------')
print(f"\nHello {guest_list[0].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[1].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[2].title()}, you've been invited to the Royal Dinner!")
print('The number of people invited: ', len(guest_list))

# More guests can be invited
print("\n\nA bigger table has been found, so more people will be invited to the dinner!")

guest_list.insert(0, "himmel the hero")
guest_list.insert(2, "ubel the serial killing (mage)")
guest_list.append('wibbel the mage')

# New invite messages
print()
print('THE NEW INVITEES')
print('----------------')
print(f"\nHello {guest_list[0].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[1].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[2].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[3].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[4].title()}, you've been invited to the Royal Dinner!")
print(f"Hello {guest_list[5].title()}, you've been invited to the Royal Dinner!")
print('The number of people invited: ', len(guest_list))

# The table(s) won't arrive, so we'll only be able to invite two people to dinner
print("\nUnfortunately, the larger tables will not arrive, so only two guests can be invited to dinner!")

# Telling guests they can't attend
cant_attend = guest_list.pop(0)
print(f"\nI'm sorry {cant_attend.title()}, you can't attend the dinner!")

cant_attend = guest_list.pop(0)
print(f"I'm sorry {cant_attend.title()}, you can't attend the dinner!")

cant_attend = guest_list.pop(2)
print(f"I'm sorry {cant_attend.title()}, you can't attend the dinner!")

cant_attend = guest_list.pop(2)
print(f"I'm sorry {cant_attend.title()}, you can't attend the dinner!")

# Telling the remaining people they're still invited
print(f"\n{guest_list[0].title()}, you're still invited!")
print(f"{guest_list[1].title()}, you're still invited!")
print('The number of people invited: ', len(guest_list))

# Empty the list
del guest_list[0]
del guest_list[0]
print(f"\n{guest_list}")