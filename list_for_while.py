company = ['Google', 'Yandex', 'Amazon', 'WildBerries']
for i in company:
    print(i)

###
count = 0
while count < len(company):
    print(company[count])
    count+=1

l1 = list(range(1,10))
print(l1)

l2 = [2,8,9,23,56,67,1,4,62,3,6,1,4]
print(l2)
print(sorted(l2))
l2.reverse()
print(l2)
l3 = l2.copy()
l3.reverse()
print(l3)

str = 'Переверни эту строку'
print(str[::-1])

##
for key, value in users.items():
    print(key, " - ", value)