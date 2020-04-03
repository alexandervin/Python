class Backpack:
    ''' Рюкзак'''

    def add(self, item):
        '''метод - положить в рюкзак'''
        print('Врюкзак положили', item)
        self.content = item


my_backpack = Backpack()
my_backpack.add(item='Ноутбук')

my_son_backpack = Backpack()
my_son_backpack.add(item='учебник')

print(my_son_backpack.content)
print(Backpack.add)
print(my_backpack.add) 