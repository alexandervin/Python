dict_a = {
    "Александр": 18,
    "Евгений": 16,
    "Андрей": 23
}


print(dict_a)

dict_b = dict_a.copy()
print(dict_b)

dict_a.pop("Евгений")

print(dict_b)
print(dict_a)
