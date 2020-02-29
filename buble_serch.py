##########################################################################
from random import randint

def bubble(array):
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)
bubble(a)
print(a)
