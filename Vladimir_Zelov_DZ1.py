# Задание 1
duration = 53
dur_d = duration // (3600 * 24)
dur_h = duration // 3600 % 24
dur_m = duration // 60 % 60
dur_s = duration % 60

if dur_d != 0:
    print(f'{dur_d} дн {dur_h} час {dur_m} мин {dur_s} сек')
elif dur_d == 0 and dur_h != 0:
    print(f'{dur_h} час {dur_m} мин {dur_s} сек')
elif dur_d == 0 and dur_h == 0 and dur_m != 0:
    print(f'{dur_m} мин {dur_s} сек')
else:
    print(f'{dur_s} сек')


# Задание 2
# Вариант 1
total = 0
for i in [k ** 3 for k in range(1, 1001, 2)]:
    if sum([int(j) for j in str(i)]) % 7 == 0:
        total += i
print(total)

total = 0
for i in [k ** 3 + 17 for k in range(1, 1001, 2)]:
    if sum([int(j) for j in str(i)]) % 7 == 0:
        total += i
print(total)


# Вариант 2
total = 0
for i in list(range(1, 1001, 2)):
    temp_cube = i ** 3
    cube_split = temp_cube
    temp_total = 0
    while cube_split != 0:
        temp_total += cube_split % 10
        cube_split = cube_split // 10
    if temp_total % 7 == 0:
        total += temp_cube
print(total)

total = 0
for i in list(range(1, 1001, 2)):
    temp_cube = i ** 3 + 17
    cube_split = temp_cube
    temp_total = 0
    while cube_split != 0:
        temp_total += cube_split % 10
        cube_split = cube_split // 10
    if temp_total % 7 == 0:
        total += temp_cube
print(total)


# Задание 3
for i in range(1, 101):
    if i % 10 == 1 and i not in (11, 12, 13, 14):
        print(f'{i} процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        if i in (11, 12, 13, 14):
            print(f'{i} процентов')
        else:
            print(f'{i} процента')
    else:
        print(f'{i} процентов')