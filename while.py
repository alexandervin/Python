gues = 23
running = True

while running:
    polz = int(input('Введите Ваш возраст:  '))
    if polz == gues:
        print('Ура!, Вы угадали')
        running = False
    elif polz < gues:
        print('Введите значение немного побольше')
    elif polz > gues:
        print(' Введите значение немного поменьше')
else:
    print('Цикл закончен')