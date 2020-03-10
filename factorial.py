import math
x = 4
xf = math.factorial(x)
print(xf)

####
number = int(input("Введите число цикл вайл: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print("Факториал числа", number, "равен", factorial)

###
number = int(input("Введите число цикл ФОР: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print("Факториал числа", number, "равен", factorial)