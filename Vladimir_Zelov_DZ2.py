import random

# Задание 1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Задание 2
tmp_ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
treatment_ls = []
for el in tmp_ls:
    if el.isdigit():
        treatment_ls.append('"')
        treatment_ls.append(f'{int(el):02}')
        treatment_ls.append('"')
    elif '+' in el or '-' in el:
        treatment_ls.append('"')
        treatment_ls.append(f'{el[0]}{int(el[1:]):02}')
        treatment_ls.append('"')
    else:
        treatment_ls.append(el)

print(treatment_ls)

new_ls = []

for i in range(len(treatment_ls)):
    if treatment_ls[i] != '"':
        if treatment_ls[i].isdigit() or '+' in treatment_ls[i] or '-' in treatment_ls[i]:
            new_ls.append(f'"{treatment_ls[i]}"')
        else:
            new_ls.append(treatment_ls[i])

print(" ".join(new_ls))


# Задача 3
# Вариант 1
def format_ls1(ls):
    treatment_str = ''
    for i in ls:
        if i.isdigit():
            treatment_str += f'"{int(i):02}" '
        elif i.startswith('+' or '-'):
            treatment_str += f'"{i[0]}{int(i[1:]):02}" '
        else:
            treatment_str += f'{i} '
    return treatment_str[:-1]


# Вариант 2
def format_ls2(ls):
    for i in range(len(ls)):
        if ls[i].isdigit():
            ls[i] = f'"{int(ls[i]):02}"'
        elif ls[i].startswith('+' or '-'):
            ls[i] = f'"{ls[i][0]}{int(ls[i][1:]):02}"'
    return ' '.join(ls)


tmp_ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'Функция 1 - {format_ls1(tmp_ls)}')
print(f'Функция 2 - {format_ls2(tmp_ls)}')

# Задание 4

ls = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in ls:
    print(f'Привет, {el.split()[-1].title()}!')

for el in range(len(ls)):
    ls[el] = ls[el].split()[-1].title() + ' ' + ' '.join(ls[el].split()[:-1])

print(ls)

# Задание 5

cash = [round(random.uniform(0, 10000), 2) for i in range(20)]
print(cash)
for el in cash:
    tmp_num = str(el).split('.')
    if len(tmp_num[-1]) == 1:
        print(f'{tmp_num[0]} руб {tmp_num[-1]}0 коп')
    else:
        print(f'{tmp_num[0]} руб {tmp_num[-1]} коп')

higher = sorted(cash)
lower = sorted(cash, reverse=True)
print(f'Цены отсортированные по возрастанию: {higher}')
print(f'Цены отсортированные по убыванию: {lower}')
print(f'Цены пяти самых дорогих товаров: {lower[:5]}')
