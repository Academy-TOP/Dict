print('Пустой словарь:')
my_dict = {}
print(my_dict, type(my_dict))

print('\nЗаполняем словарь:')
my_dict = {"Developer": "Ann"}
my_dict_2 = {"Macbook": "Pro", "Developer": "Nick", "Iphone": 1}
print(my_dict)
print(my_dict_2)

print('\nВыведем значение одного из ключей:')
value = my_dict_2["Macbook"]
print(value)

print('\nДобавим элементы в словарь:')
key = "fruit"
value = "orange"
my_dict_2[key] = value
print(my_dict_2)
my_dict_2['Картина'] = 'Мишки в лесу'
print(my_dict_2)

print('\nОбновление словаря:')
my_dict.update(my_dict_2)
print(my_dict)

print('\nСоздаем словарь:')
my_dict_3 = dict.fromkeys(("Macbook", "Iphone"), 1)
my_dict_4 = dict.fromkeys(("Macbook", "Iphone"))
print(my_dict_3)
print(my_dict_4)

print('\nСписок ключей:')
print(my_dict.keys())
print('\nСписок значений:')
print(my_dict.values())
print('\nСписок пар ключей и значений:')
print(my_dict.items())

print('\nЗнакомимся с методом "Get":')
print(my_dict.get("Developer"))
print(my_dict.get("Key"))
print(my_dict)

print('\nЗнакомимся с методом "setdefault":')
print(my_dict.setdefault("Developer"))
print(my_dict.setdefault("Key"))
print(my_dict)

print('\nЗнакомимся с методом "pop":')
my_dict = {"Macbook": "Pro", "Developer": "Nick", "Iphone": 1}
print(my_dict)
print(my_dict.pop("Macbook"))
print(my_dict)
#print(my_dict.pop("Key"))

print('\nЗнакомимся с методом "popitem":')
my_dict = {"Macbook": "Pro", "Developer": "Nick", "Iphone": 1}
print(my_dict.popitem())
print(my_dict)
