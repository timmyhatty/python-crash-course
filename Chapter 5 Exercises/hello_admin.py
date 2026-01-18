# 5-8: Hello Admin

list_of_users = ['KnowWifi', 'yodecari', 'SUPERTIMBOY', 'TIMTIMMYTIMOTHY', 'exCelsior']
admin = 'TIMTIMMYTIMOTHY'.lower()

if list_of_users:
    for username in list_of_users:
        if username.lower() == admin:
            print(f'Hello {username}, would you like a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again!')
else:
    print('We need to find some users!')