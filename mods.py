class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 22

    def print_info(self):
        print(f'Имя {self.name} возраст {self.__age}')

    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')
