import functools as ft

def dict_reunion(dict1, dict2):
    
    keys3 = dict1.keys() & dict2.keys()
    
    dict3 = ft.reduce(lambda acc, item: acc | {item: (dict1[item] + dict2[item])}, keys3, {})
    
    return dict3
    
    
    
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict2 = {'a': 1, 'd': 2, 'f': 3, 'g': 4, 'e': 5}
print(dict_reunion(dict1, dict2))