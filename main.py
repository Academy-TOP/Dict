my_dict = {"Developer": "Ann"}
my_dict_2 = {"Macbook": "Pro", "Developer": "Nick", "Iphone": 1}

value = my_dict_2["Macbook"]

key = "fruit"
value = "orange"

my_dict_2[key] = value
my_dict_2['Картина'] = 'Мишки в лесу'

my_dict.update(my_dict_2)

my_dict_3 = dict.fromkeys(("Macbook", "Iphone"), 1)

print(my_dict)
print(my_dict_2)
print(value)

print(my_dict_3)
