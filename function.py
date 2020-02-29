l = [1, 2, '33', 4, 5]


def f1(l1):
    return [i * 2 for i in l]


print(f1(l))


def f2(l2):
    def umn(x):
        return int(x) * 2

    return [umn(i) for i in l]


print(f2(l))


def f3(l3):
    def umn(x):
        if isinstance(x, int):
            return x * 2

    return [umn(i) for i in l]


print(f3(l))


def f4(l4):
    def umn(x):
        if isinstance(x, int):
            return x * 2

    return [umn(i) for i in l if umn(i)]


print(f4(l))


def f5(l5):
    '''
    Умножает каждый элемент списка на 2.

    :param:
    :param:
    '''
    def umn(x):
        return x * 2

    return list(map(umn, l))


print(f5(l))
