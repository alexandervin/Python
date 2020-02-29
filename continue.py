while True:
    s = input('Введите строку -   ')
    if s == 'выход':
        break
    if len(s) <= 3:
        print('Длина строки не достаточна')
        continue
    print('Введенная строка достаточной длины')
