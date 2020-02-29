a = abs(int(input('Введите число:')))
print(a)
summ = 0
mult = 1

while a > 0:
    x = a % 10
    summ += x
    