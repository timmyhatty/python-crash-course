cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
    if number == 10:
        print(cube)
    else:
        print(cube, end=' ')