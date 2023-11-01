"""
Listele sunt un tip de date abstract în care elementele sunt stocate într-o manieră ordonată.
În Python, o listă este creată prin adaugarea elementelor în paranteze drepte [], separate prin virgulă.

"""

lista_intregi = [1, 2, 3]
print(lista_intregi)

"""
Listele pot contine diferite tipuri de date: numere intregi, reale, caractere, liste, tuple.
"""

# lista intregi
lista_int = [1, 2, 3]

# lista caractere
lista_char = ['a', 'b', 'c']

# lista mixta
lista_mix = [1, 'a', [2]]

"""
Accesarea elementlor listei prin indecși

Putem folosi operatorul index [] pentru a accesa un element dintr-o listă. 
Indecșii încep de la 0, deci o listă cu 3 elemente va avea un index de la 0 la 2.
"""

lista_intregi = [1, 2, 3, 4, 5]

# primul element
print(f"Primul element din lista: {lista_intregi[0]}")

# al doilea element
print(f"Al doilea element din lista: {lista_intregi[1]}")

# ultimul element
print(f"Ultimul element din lista: {lista_intregi[-1]}")

# penultimul element
print(f"Penultimul element din lista: {lista_intregi[-2]}")

# index inexistent -> IndexError: list index out of range
# print(f"Elementul 100 din lista: {lista[100]}")

"""
Taierea unei liste (List Slicing)

Putem accesa o serie de elemente dintr-o listă folosind operatorul de tăiere : (două puncte) .

Când tăiem liste, indexul de început este inclusiv, iar indexul de final este exclusiv. 
De exemplu, lista[2: 4] returnează o listă cu elemente la indexul 2, 3, dar nu 4.
"""

lista_intregi = [1, 2, 3, 4, 5]
print(f"Slice: {lista_intregi[2:4]}")

"""
Capul, coada listei

Capul listei conține doar primul element al listei - accesat prin operatorul index []. 
Coada listei conține toate elementele rămase de la al doilea până la ultimul element de listă -
 accesat prin operația de tăiere.
"""
lista_intregi = [1, 2, 3, 4, 5]
# capul (head)
print(f"Head: {lista_intregi[0]}")

# coada (tail)
print(f"Tail: {lista_intregi[1:]}")

"""
Concatenarea a doua liste

Putem folosi operatorul + pentru a combina două liste.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7]
concat = lista1 + lista2
print(f"Lista concatenata {lista1} + {lista2} = {concat}")

"""
Parcurgerea unei liste in mod recursiv 

Nota: pentru rezolvarea exercitiilor de la acest laborator nu folositi structuri repetitive (for, while), folositi recursivitatea!
Ne folosim de notiunile de cap si coada prezentate anterior pentru a parcurge listele.
"""


def afisare_lista(lista):
    if len(lista) > 0:
        head = lista[0]
        tail = lista[1:]
        print(head, end='\n')
        afisare_lista(tail)


afisare_lista([2, 4, 5])

"""
Exercitiu: Calculati si afisati suma elementelor unei liste de intregi.
"""


# TODO: exercitiu

def suma_lista(lista):
    if len(lista) > 0:
        return lista[0] + suma_lista(lista[1:])
    else:
        return 0


print(f"Suma elementelor listei {lista_intregi} este {suma_lista(lista_intregi)}")

"""

Funcția reduce()

Funcția reduce() este definită în modulul functools. Funcția reduce() primește două argumente, o funcție și un iterabil 
(in cazul nostru, o lista) si returnează o singură valoare. Deasemenea, functia reduce() are un argument optional: 
o valoare initiala. Daca aceasta valoare initiala este prezenta, ea va fi plasata inaintea tuturor elementelor in calcul.

functools.reduce(functia, iterabil, valoare initiala)
Pentru a calcula suma tuturor intregilor dintr-o lista putem folosi reduce() impreuna cu o functie anonima.
"""

import functools


def suma_lista_reduce(lista):
    return functools.reduce(lambda a, b: a + b, lista, 0)
    # sau functools.reduce(lambda a, b: a + b, lista)


print(f"(reduce) Suma elementelor listei {lista_intregi} este {suma_lista_reduce(lista_intregi)}")

"""
Putem folosi si modulul operator, invatat in laboratorul 2.
"""

import operator


def suma_lista_reduce_op(lista):
    return functools.reduce(operator.add, lista, 0)
    # sau functools.reduce(lambda a, b: a + b, lista)


print(f"(reduce+op) Suma elementelor listei {lista_intregi} este {suma_lista_reduce_op(lista_intregi)}")

"""
Funcția filter()

Funcția filter() primește, la fel ca functia reduce(), două argumente, o funcție și un iterabil. 
Insă nu returnează o singură valoare, ci returnează un alt iterabil. După cum îi spune și numele, 
functia creează o listă de elemente pentru care funcția returnează adevărat.
"""


def numere_pare(lista):
    return list(filter(lambda x: x % 2 == 0, lista))


print(f"Elementele pare ale listei {lista_intregi} sunt {numere_pare(lista_intregi)}")

"""
Funcția map()

La fel ca funcțiile filter și reduce, funcția map() primește două argumente, o funcție și un iterabil. 
Functia aplică funcția tuturor elementelor din lista.
"""


def incrementeaza_elementele(lista, n):
    return list(map(lambda x: x + n, lista))


print(f"Elementele listei {lista_intregi} adunate cu {3} sunt {incrementeaza_elementele(lista_intregi, 3)}")

"""
Exercitiu: Scrieti o functie care primeste ca parametru o lista si folosind functia map, ridica la puterea a 2-a 
toate elementele listei.
"""

# TODO: exercitiu

def putere(lista):
    return list(map(lambda x: x * x, lista))


print(f"Elementele listei {lista_intregi} la puterea a 2-a sunt {putere(lista_intregi)}")

"""
Lista cifrelor unui numar.
"""


def descompunere(nr):
    if nr <= 9:
        return [nr]
    else:
        return [nr % 10] + descompunere(nr // 10)


print(
    f"Lista cifrelor numarului 1235 este {descompunere(1235)}")  # nota: observati ca lista contine cifrele in ordine inversa


def descompunere2(nr):
    if nr <= 9:
        return [nr]
    else:
        return descompunere2(nr // 10) + [nr % 10]


print(f"Lista cifrelor numarului 1235 este {descompunere2(1235)}")

"""
1. a) Implementați funcții care construiesc lista cifrelor unui număr care satisfac o condiție anume
 (cifre impare, pare, mai mici decât 7, etc. la alegere), în ordine normală și inversă.
"""

# TODO: exercitiu

def cifre_cond(nr): #cifre pare
    if nr <= 9:
        if nr % 2 == 0:
            return [nr]
        else:
            return []

    else:
        if nr % 2 == 0 :
            return cifre_cond(nr//10) + [nr%10]
        else:
            return cifre_cond(nr//10)

print(f"lista cifrelor pare ale nr 1234567 este {cifre_cond(12345678)}")

# TODO: tema din Partea a II-a: ex 1. b,c; ex 2; ex 5; ex 6