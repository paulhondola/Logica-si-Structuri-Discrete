import functools

"""
Un dicționar constă dintr-o colecție de perechi cheie-valoare. Fiecare pereche cheie-valoare mapează cheia cu valoarea asociată.

Pentru a defini un dicționar prin folosirea unei liste, separate prin virgulă, de perechi cheie-valoare între acolade({}).
Două puncte (:) separă fiecare cheie de valoarea asociată.
"""
dictionar_capitale = {
    'Bucuresti': 'Romania',
    'Budapesta': 'Ungaria',
    'Chisinau': 'Moldova'
}

print(dictionar_capitale)  # {'Bucuresti': 'Romania', 'Budapesta': 'Ungaria', 'Chisinau': 'Moldova'}

"""
Dictionarele au urmatoarele caracterisitici:
o anumită cheie poate apărea într-un dicționar o singură dată, cheile duplicate nu sunt permise.
"""

dictionar_capitale['Bucuresti'] = 'RO'  # schimbarea valorii asociate unei chei
print(dictionar_capitale)

"""
Cheia trebuie să fie de un tip imuabil (de exemplu, nu poate sa fie o lista)
"""
# dictionar_capitale[['a']] = 'b' # "TypeError: unhashable type: 'list'"


"""
Accesarea tuturor elementelor din dictionar de tipul cheie-valoare se face cu ajutorul items().
Accesarea tuturor cheilor din dictionar se face cu ajutorul keys().
Accesarea tuturor valorilor din dictionar se face cu ajutorul values().

Lungimea unui dictionar (numarul de elemente) se obtine cu ajutorul functiei len
"""
print(
    f"elemente: {dictionar_capitale.items()}")  # dict_items([('Bucuresti', 'RO'), ('Budapesta', 'Ungaria'), ('Chisinau', 'Moldova')])
print(f"chei:{dictionar_capitale.keys()}")  # dict_keys(['Bucuresti', 'Budapesta', 'Chisinau'])
print(f"valori:{dictionar_capitale.values()}")  # dict_values(['RO', 'Ungaria', 'Moldova'])
print(f"lungimea:{len(dictionar_capitale)}")

elev_nota = {
    'Alex': 10,
    'Mihai': 9,
    'Ioana': 10
}

print(elev_nota.items())  # dict_items([('Alex', 10), ('Mihai', 9), ('Ioana', 10)])

# Exercitiu: calculati media elevilor

# Varianta1
def functie_suma(acc, elev):
    _, nota = elev  # despachetam fiecare tuplu primit ca parametru (exemplu: ('Alex', 10))
    return acc + nota


def medie_elevi(dictionar):
    suma_note = functools.reduce(functie_suma, dictionar.items(), 0)
    return suma_note / len(dictionar)

# Varianta2
def medie_elevi2(dictionar):
    suma_note = functools.reduce(lambda suma, elev: suma + elev[1], dictionar.items(), 0)
    return suma_note / len(dictionar)


print(f"Media elevilor {elev_nota} este {medie_elevi(elev_nota)}")
print(f"Media elevilor {elev_nota} este {medie_elevi2(elev_nota)}")

"""
Parcurgerea recursiva a dictionarelor. Pentru parcurgerea recursiva a dictionarelor, convertim dictionarul primit ca
 parametru in 'dict_items', apoi convertim 'dict_items' intr-o lista pe care o sa o parcurgem recursiv.
"""

# Varianta3

def suma_recursiva(dict_list):
    if len(dict_list) > 0:
        nume, nota = dict_list[0]
        return nota + suma_recursiva(dict_list[1:])
    else:
        return 0


def medie_elevi_recursiva(dictionar):
    suma_note = suma_recursiva(list(dictionar.items()))
    return suma_note / len(dictionar)


print(f"Media elevilor {elev_nota} este {medie_elevi_recursiva(elev_nota)}")

"""
1. Scrieți o funcție care ia o listă de asociere cu perechi de tip (șir, întreg) și creează un dicționar în care 
fiecare șir e asociat cu suma tuturor valorilor cu care e asociat în listă.

Input: [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]; Output: {'a': 10, 'b': 8, 'c': 2}
"""
def adauga_in_dictionar(new_dict, pair):
    key, value = pair
    if key in new_dict.keys():
        new_dict[key] += value
    else:
        new_dict[key] = value
    
    return new_dict
    

def dict_perechi(lst):
    return functools.reduce(adauga_in_dictionar, lst, dict())

print("EX1 -->", dict_perechi([('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]))

# TODO: clasa

"""
2. Scrieți o funcție care ia o listă de șiruri de caractere și creează un dicționar în care fiecare șir e asociat cu 
numărul aparițiilor din listă.

Input: ["aaa", "bbb", "aabbb"]; Output: {'a': 5, 'b': 6}
"""

def add_to_dict(new_dict, letter):
    
    if letter in new_dict.keys():
        new_dict[letter] += 1
    else:
        new_dict[letter] = 1
    
    return new_dict
    
def concat_strings(lst):
    return functools.reduce(lambda acc, item: acc + item, lst, '')

def create_dict(lst):
    return functools.reduce(add_to_dict, concat_strings(lst), dict())

print(create_dict(["aaa", "bbb", "aabbb"]))


# TODO: exercitiu


"""
3. Implementați cu ajutorul lui reduce funcția filter care creează un nou dicționar doar cu perechile din dicționarul 
dat care satisfac o funcție dată.

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: {'a': 5, 'b': 7}
"""

def add_to_dict(new_dict, pair):
    key, value = pair
    
    if key in new_dict.keys():
        new_dict[key] += value
    else:
        new_dict[key] = value
        
    return new_dict

def filter_dict(my_dict, condition):
    return functools.reduce(lambda acc, item: add_to_dict(acc, item) if condition(item[1]) else acc, my_dict.items(), dict())
    
print(filter_dict({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))
# TODO: exercitiu


# TEMA: ex 4,5,6

"""
4. Pentru tipurile colecție (liste, mulțimi, dicționare) e util să avem funcții care ne spun dacă există un element care satisface o anume condiție, respectiv dacă toate elementele satisfac condiția.
Implementați funcțiile exists și for_all pentru dicționare, folosind reduce. Ele iau ca parametru o funcție booleană de cheie și valoare (care exprimă condiția) și dicționarul în care se face căutarea. 

Input: dict: {'a': 5, 'b': 7, 'c': 1}; conditie: valoare >= 5; Output: exists: True, for_all: False

5. Implementați cu ajutorul lui reduce funcția map care construiește un dicționar în care toate valorile au fost transformate folosind o funcție dată ca parametru.

Input: {'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1; Output: {'a': 6, 'b': 8, 'c': 7}

6. Scrieți o funcție care primește un dicționar de la șiruri la întregi și o listă de șiruri și returnează mulțimea tuturor valorilor din dicționar care corespund șirurilor din listă.

Input: {'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']; Output: {5, 7}

"""