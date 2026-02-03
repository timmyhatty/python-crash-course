# 7-10: Dream Vacation

NAME_HEADER = 'Name'
VACATION_HEADER = 'Vacation'
RESULTS_HEADER = 'HERE ARE THE RESULTS'
RESULTS_HEADER_UNDERLINE = '--------------------'

polling_active = False
responses = {}

print('FAVORITE VACATION SPOTS')
initial_input = input('Would you like to poll some users (yes/no): ').lower()
if initial_input == 'yes':
    polling_active = True

while polling_active:
    name = input('\nWhat is your name: ')
    dream_vacation = input('What is your dream vacation: ')

    responses[name] = dream_vacation

    repeat = input('Would you like to survey another person (yes/no): ').lower()
    if repeat == 'no':
        polling_active = False

print(f'\n{RESULTS_HEADER:>30}')
print(f'{RESULTS_HEADER_UNDERLINE:>30}')

print(f'\n{NAME_HEADER:>17} | {VACATION_HEADER:<17}')
for name, vacation in responses.items():
    print(f'{name:>17} - {vacation}')
    