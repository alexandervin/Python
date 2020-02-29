class Robot:
    ''' Представляем робота с именем'''
    population = 0

    def __init__(self, name):
        self.name = name
        print('Инициализация {0} '.format(self.name))
        Robot.population += 1

    def SayHi(self):
        print('Привет меня зовут {0}'.format(self.name))


    def __del__(self):
        print('Происходит уничтожение робота {0}'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print(' Осталось {0:d} работающих дроидов'.format(Robot.population))

    def HowMany():
        print('осталось  {0:d}   в наличие '.format(Robot.population))

    howMany = staticmethod(HowMany)


droid1 = Robot('R2D2')
droid1.SayHi()
print(Robot.population)
del droid1
print(Robot.population)
Robot.howMany()