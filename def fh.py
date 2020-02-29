l = [1,2,3,8,6,78]
def f1(*params):
    res = 0
    for i in params:
        res = res + i
    return res

a1 = f1(1, 2, 4, 5)
a2 = f1(1, 2, 4, 10)
print(a2)


print(sum(l))

l2 = [1,2,3,8,6,100]

j = 0
for i in l2:
    j += i
print(j)


N1 = 10
A1 = [0] * N1
for i in range (N1):
    A1[i] = i
print(A1)

N2 = 10
A2 = [i for i in range(N2)]
print(A2)

from random import randint
A3 = [randint(1, 100)
      for i in range(25)]
print(A3)
m = max(A3)
mi = A3.index(m)
print(max(A3))
print(mi)