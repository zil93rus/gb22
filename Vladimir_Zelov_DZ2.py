# Задание 1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

tmp_ls = ['в', '5', 'часов', '17.6', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']
treatment_ls = []
for el in tmp_ls:
    if el.isdigit():
        treatment_ls.append('"')
        treatment_ls.append(f'{int(el):02}')
    elif '+' in el or '-' in el:
        treatment_ls.append('"')
        treatment_ls.append(f'{el[0]}{int(el[1:]):02}')
    else:
        treatment_ls.append(el)

print(treatment_ls)
print(' '.join(treatment_ls).replace(' "', ''))
