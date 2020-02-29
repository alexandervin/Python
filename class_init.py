class Person:
    def __init__(self, name):
        self.name = name

    def SayHi(self):
        print('Скажи привет!', self.name)


p = Person('Александр')
p.SayHi()
