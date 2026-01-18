# 5-11: Ordinal Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# No MAGIC numbers
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9

if numbers:
    for number in numbers:
        if number == ONE:
            print('1st')
        elif number == TWO:
            print('2nd')
        elif number == THREE:
            print('3rd')
        elif number == FOUR:
            print('4th')
        elif number == FIVE:
            print('5th')
        elif number == SIX:
            print('6th')
        elif number == SEVEN:
            print('7th')
        elif number == EIGHT:
            print('8th')
        elif number == NINE:
            print('9th')
else:
    print('ERROR: Empty list')