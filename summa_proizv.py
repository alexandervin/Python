'''
Программа на входе запрашивает число, выыодит сумму и произведение цифр этого числа
'''

a = abs(int(input('Введите число: ')))
summ = 0
proizv = 1

while a > 0:
    x = a % 10
    summ += x
    proizv *= x
    a = a // 10

print(summ,proizv)

