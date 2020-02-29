def rec_summ(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + rec_summ(x - 1)

print(rec_summ(5))


def rec_fact(x):
    if x == 0:
        return 1
    else:
        return x * rec_fact(x - 1)

print(rec_fact(5))


def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


print(fibo(10))
