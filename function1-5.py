l = [1, 3, 4, 8]


def f1(l1):
    return [i * 2 for i in l]


print(f1(l))


def f2(l2):
    def f2_2(x):
        return x * 2
    return [f2_2(i) for i in l]

print(f2(l))

def f3(l3):
    def f3_3(x):
        return x * 2
    return [sum(f3_3(i)).map(f3, l)]
print(f3(l))