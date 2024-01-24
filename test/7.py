from functools import reduce

'''
# TODO 4. Pentru tipurile colecție (liste, mulțimi, dicționare) e util să avem funcții care ne spun dacă există un element care satisface o anume condiție, respectiv dacă toate elementele satisfac condiția.

Implementați funcțiile exists și for_all pentru dicționare, folosind reduce. Ele iau ca parametru o funcție booleană de cheie și valoare (care exprimă condiția) și dicționarul în care se face căutarea. 

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: exists: True, for_all: False
'''

def exists(dictionary, condition):
    return reduce(lambda acc, item: acc or condition(item),dictionary.values(), False)


def for_all(dictionary, condition):
    return reduce(lambda acc, item: acc and condition(item),dictionary.values(), True)

    
print(exists({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))
print(for_all({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))


'''
# TODO 5. Implementați cu ajutorul lui reduce funcția map care construiește un dicționar în care toate valorile au fost transformate folosind o funcție dată ca parametru.

Input: {'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1; Output: {'a': 6, 'b': 8, 'c': 7}
'''

def map_dictionary(dictionary, function):
    return reduce(lambda acc, pair: acc | {pair[0]: function(pair[1])}, dictionary.items(), {})

print(map_dictionary({'a': 5, 'b': 7, 'c': 1}, lambda x: x + 1))

'''
# TODO 6. Scrieți o funcție care primește un dicționar de la șiruri la întregi și o listă de șiruri și returnează mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă.

Input: {'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']; Output: {5, 7}
'''

def common_keys(dictionary, lst):
    return reduce(lambda acc, pair: acc.union({pair[1]}) if pair[0] in lst else acc, dictionary.items(), set())


print(common_keys({'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']))