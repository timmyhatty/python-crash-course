# 6-10: Favorite Numbers

favorite_numbers = {
    'timothy' : [11, 22],
    'jane' : [2, 3, 5],
    'anasia' : [7],
    'tommie' : [25, 63, 100, 999],
    'paul' : [13]
}

for person, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"{person.title()}'s Favorite Numbers are: ", end='')
    else:
        print(f"{person.title()}'s Favorite Number is: ", end='')

    for number in numbers:
        if number == numbers[-1]:
            print(f"{number}")
        else:
            print(f"{number}, ", end='')