class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.forman(self.name))

    def tell(self):
        print('Имя: {0}, возраст {1}'.format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):

        SchoolMember.__init__(self, name, age)

        self.salary = salary
        print('Создан препод {0}'.format(self.name))

    def tell(self):
        print('Зарплата:{0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, ball):

        SchoolMember.__init__(self, name, age)

        self.ball = ball
        print('Создан студент {1}'.format(self.name))

    def tell(self):
        print('')