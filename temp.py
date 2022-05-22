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
