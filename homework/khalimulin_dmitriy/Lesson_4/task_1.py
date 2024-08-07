my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}


my_dict['tuple'] = list((10, 4.2, 'test', True, 253, 325235))
my_dict['list'] = [2354235, 'super', 244151, 4235.24, False]
my_dict['dict'] = {
    'phoneNumber': '89308476463',
    'firstname': 'Oleg',
    'lastname': 'Gaz',
    'surname': 'Gazovich',
    'code': 341125
}
my_dict['set'] = {2341234, 'test', 3636214, None, False}

# Поиск последнего значения в 'tuple'
search_last_value = my_dict['tuple'][-1]

# Добавляем значение в список и удаляем второй элемент списка 'list'
my_dict['list'].append("432236")
my_dict['list'].pop(1)

# Добавляем элемент с ключом ('i am a tuple',) и удаляем 'lastname'
my_dict['dict'][(str('i am a tuple',))] = "Новое значение"
del my_dict['dict']['lastname']

# Добавляем новый элемент в множество и удаляем элемент из множества
my_dict['set'].add(324345)
my_dict['set'].discard('test')

print(my_dict)
