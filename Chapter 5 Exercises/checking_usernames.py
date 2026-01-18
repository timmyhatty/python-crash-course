# 5-10: Checking Usernames

current_users = ['KnowWifi', 'yodecari', 'SUPERTIMBOY', 'TIMTIMMYTIMOTHY', 'exCelsior']
new_users = ['CurlyGirl01', 'PaintedRed', 'TIMTIMMYTIMOTHY', 'yodecari', 'DumpTruckMcgee']

current_users_lowercase = current_users[:]
index = 0
for username in current_users_lowercase:
    current_users_lowercase[index] = username.lower()
    index += 1

if new_users:
    for username in new_users:
        if username.lower() in current_users_lowercase:
            print(f'{username} is already being used. Please enter a different, unique username')
        else:
            print(f'{username} is available')
else:
    print('There are no new users')