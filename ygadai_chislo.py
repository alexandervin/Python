zzz = 18  # загаданное число
i = 0
while True:
    chislo = int(input(f'Введите число:'))  # старт
    i += 1
    if chislo == zzz:
        print(f'ПОЗДРАВЛЯЕМ!!! Вы угадали попытки №:{i} ')
        break
    elif chislo < zzz:
        print(f'Попробуй еще раз, ваще число {chislo} МЕНЬШЕ загаданного')
    #  chislo = int(input(f'Введите число еще раз:'))
    elif chislo > zzz:
        print(f'Попробуй еще раз, ваще число {chislo} БОЛЬШЕ загаданного')
    # chislo = int(input(f'Введите число ещеЕЕ :'))
    else:
        print('???')
        break
