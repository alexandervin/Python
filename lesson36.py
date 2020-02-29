# ООП

class A:
    property1 = 'prop1'
    property2 = 'prop2'
    name = 'Gost'

    def say_hi(self, name=' '):
        return 'Hi, ' + self.name


a = A()

print(a.say_hi())
