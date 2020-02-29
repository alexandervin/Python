class Robot:
    ''' Представляет железяку с именем. '''

    # переменная класса содержащая количество железяк
    poulathion = 0

    def __init__(self, name):
        '''Инициализация данных. '''
        self.name = name
        print('Инициализация {0}'.format(self.name))
        Robot.poulathion +=1

    def howMany():
        print('У нас {0:d} железа'.format(Robot.poulathion))

    def sayHi(self):
        print('Мои хозяева называют меня {0}'.format(self.name))

    def __del__(self):
        '''Уничтожается'''
        print('{0} стираееся' .format(self.name))
        Robot.poulathion -=1

    howMany = staticmethod(howMany)

droid1 = Robot('R2D2')
droid1.sayHi()
print(Robot.__doc__)
print(Robot.__init__.__doc__)
Robot.howMany()
del droid1
Robot.howMany()
