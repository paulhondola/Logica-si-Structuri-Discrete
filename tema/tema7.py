'''
4. Pentru tipurile colecție (liste, mulțimi, dicționare) e util să avem funcții care ne spun dacă există un element care satisface o anume condiție, respectiv dacă toate elementele satisfac condiția.
Implementați funcțiile exists și for_all pentru dicționare, folosind reduce. Ele iau ca parametru o funcție booleană de cheie și valoare (care exprimă condiția) și dicționarul în care se face căutarea. 

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: exists: True, for_all: False
'''
import functools

def exists(condition, my_dict):
    return functools.reduce(lambda acc, item: True if condition(item[1]) else acc or False, my_dict.items(), False)

print(exists(lambda x: x >= 5,{'a': 5, 'b': 7, 'c': 1}))

def for_all(condition, my_dict):
    return functools.reduce(lambda acc, item: acc and True if condition(item[1]) else False, my_dict.items(), True)

print(for_all(lambda x: x >= 5,{'a': 5, 'b': 5, 'c': 5}))

'''
5. Implementați cu ajutorul lui reduce funcția map care construiește un dicționar în care toate valorile au fost transformate folosind o funcție dată ca parametru.

Input: {'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1; Output: {'a': 6, 'b': 8, 'c': 7}
'''

def my_map(my_dict, f):
    return functools.reduce(lambda acc, item: {item[0]: f(item[1])} | acc, my_dict.items(), {})

print(my_map({'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1))

def add_to_dict(new_dict, pair, f):
    key, value = pair
    
    if key in new_dict.keys():
        new_dict[key] += f(value)
    else:
        new_dict[key] = f(value)
        
    return new_dict

'''
6. Scrieți o funcție care primește un dicționar de la șiruri la întregi și o listă de șiruri și returnează mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă.

Input: {'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']; Output: {5, 7}
'''

def values(dict, lst):
    return functools.reduce(lambda acc, item: {item[1]} | acc if item[0] in lst else acc, dict.items(), set())

print(values({'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']))
