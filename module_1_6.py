my_dict = {'Andrey': 1975, 'Kamila': 1999, 'Kata': 2002}
print('Dict: ', end=' '),print(my_dict)
print('existing value Andrey: ', my_dict['Andrey'])
#print('Not existing value :','none')
#if ['Kamilas'] in my_dict()
 #   print(my_dict[''])
#else:
 #   print('такого ключа нет')
print(my_dict.get('Kamilasss','такого ключа нет'))
print('модифицированный словарь'),
my_dict.update({'verblud': 1981,
                'Artem': 1915})
print(my_dict)
print ('год рождения камилы')
a = my_dict.pop('Kamila')
print(a)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314}
print(my_set)
my_set.update({5, 6})
print(my_set)
print(my_set.discard(5))
print(my_set)