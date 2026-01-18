multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    if number == max(multiples_of_three):
        print(number)
    else:
        print(number, end=' ')