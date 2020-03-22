# coding=utf-8
my_list = ['dog', 'cat', 'hamster']
i = 0
while i < len(my_list):
    poz = my_list[i]
    print('Проверяем', poz)
    if poz == 'cat':
        print('Кошак нашелся')
        break
    i += 1

