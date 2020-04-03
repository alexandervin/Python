class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class Canfly:

    def __init__(self):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0


class Drone(Robot, Canfly):
    def operate(self):
        print('Робот ведет разведку с воздуха')


orbiter = Drone(model='Orbiter II')
orbiter.take_off()
print(orbiter.altitude, orbiter.velocity)

orbiter.fly()
print(orbiter.altitude, orbiter.velocity)

orbiter.operate()
print(orbiter.altitude, orbiter.velocity)

orbiter.land_on()
print(orbiter.altitude, orbiter.velocity)
