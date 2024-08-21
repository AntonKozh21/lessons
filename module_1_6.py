my_dict = {'Anton': 2000, 'Kristina': 1998, 'Evgeniy': 1999}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Kirill'))
my_dict.update({'Viktor': 1995,
                'Irina': 1996})
deleted_value_ = my_dict.pop('Evgeniy')
print(deleted_value_)
print(my_dict)
# работа с множествами
my_set = {21, 21, 21, True, 'Fox', True, 21}
print(my_set)
my_set.update({'Cow',
               (3.14, 3, 777)})
my_set.discard('Fox')
print(my_set)
