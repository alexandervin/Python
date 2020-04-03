class Backpak:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print('В рюкзак положили:', item)

    def inspect(self):
        print('В рюкзаке лежит')
        for item in self.content:
            print('------', item)


my_backpack = Backpak(gift='ручка')
my_backpack.add(item='ноут')
my_backpack.add(item='зарядка')
my_backpack.add(item='флэшка')

my_backpack.inspect() 
