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

###

# ! Программа Обменный пункт

print("Для выхода нажмите Y")

while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    cache = round(money / 56, 2)
    print("К выдаче", cache, "долларов")

print("Работа обменного пункта завершена")

####
# ! Программа Обменный пункт

print("Для выхода нажмите Y")

while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    if money < 0:
        print("Сумма должна быть положительной!")
        continue
    cache = round(money / 56, 2)
    print("К выдаче", cache, "долларов")

print("Работа обменного пункта завершена")