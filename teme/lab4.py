# partea a II-a

# TODO 1 a

"""
1. a) Implementați funcții care construiesc lista cifrelor unui număr care satisfac o condiție anume (cifre impare, pare, mai mici decât 7, etc. la alegere), în ordine normală și inversă
"""

def cifre_pare(n):
    if n == 0:
        return []
    elif n % 2 == 0:
        return cifre_pare(n // 10) + [n % 10]
    else:
        return cifre_pare(n // 10)
    

print(f"Lista cu cifre pare ale numarului 12345 este:{cifre_pare(12345)} ---> ordine normala")


def cifre_pare2(n):
    if n == 0:
        return []
    elif n % 2 == 0:
        return [n % 10] + cifre_pare2(n // 10)
    else:
        return cifre_pare2(n // 10)

print(f"Lista cu cifre pare ale numarului 12345 este:{cifre_pare2(12345)} ---> ordine inversa")

# TODO 1 b

"""
b) Implementați o funcție care construiește lista cifrelor unui număr care satisfac o condiție dată ca parametru sub forma unei funcții cu tipul int -> bool.
"""

def first_and_last_digit(num):
    return str(num)[0] == str(num)[-1]

def build_new_list(lst):
    return [x for x in lst if first_and_last_digit(x)]

def build_new_list_rec(lst):
    if len(lst) == 0:
        return []
    elif first_and_last_digit(lst[0]):
        return [lst[0]] + build_new_list_rec(lst[1:])
    else:
        return build_new_list_rec(lst[1:])
    
def build_new_list_filter(lst):
    return list(filter(first_and_last_digit, lst))

lst = [121, 135, 342, 343, 676, 958259]

print(f"Iterative method: {build_new_list(lst)}")
print(f"Recursive method: {build_new_list_rec(lst)}")
print(f"Filter function method: {build_new_list_filter(lst)}")

# TODO 1 c

"""
c) Invers, dată fiind o listă de cifre, construiți numărul format doar din cifrele care respectă o condiție (dată ca parametru funcție cu tipul int -> bool). Rezolvați problema direct, recursiv, și apoi prin folosirea lui filter (selectarea cifrelor) cu reduce (pentru construirea numărului).
"""
def impar(n):
    return n % 2

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def build_number(lst):
    nr = 0
    for i in lst:
        if impar(i):
            nr = 10 * nr + i
    return nr

def build_number_rec(lst):
    if len(lst) == 0:
        return 0
    elif impar(lst[-1]):
        return 10 * build_number_rec(lst[:-1]) + lst[-1]
    else:
        return build_number_rec(lst[:-1])
    
def filter_list(lst):
    return list(filter(impar, lst))

import functools

def build_number_reduce(lst):
    return functools.reduce(lambda a, b: 10 * a + b if impar(a) else b, filter_list(lst), 0)

print(f"Iterative method: {build_number(lst)}")
print(f"Recursive method: {build_number_rec(lst)}")
print(f"Filter and reduce method: {build_number_reduce(lst)}")


# TODO 2

"""
2. Implementați funcția fromto care generează lista numerelor întregi dintr-un interval dat, scrieți o funcție care creează lista tuturor întregilor dintr-un interval dat, divizibili cu o valoare dată d.
Indicație: Găsiți cel mai mare număr divizibil din interval, și continuați pas cu pas.
"""
def fromto(start, end, div):
    if start > end:
        return []
    else:
        if start % div == 0:
            return [start] + fromto(start + 1, end, div)
        else:
            return fromto(start + 1, end, div)
    

print(f"Lista numerelor divizibile cu 5 este:{fromto(1, 100, 5)}")


# TODO 3
"""
3. a) Implementați funcția nth care returnează al n-lea element dintr-o listă.
b) Implementați o funcție firstn care returnează o listă cu primele n elemente dintr-o listă dată.
"""
def nth(lst, n):
    return lst[n - 1]

def firstn(lst, n):
    return lst[:n]

n = 5
print(f"Primele {n} elemente din lista: {firstn(lst, n)}")


# TODO 5

"""
5. a) Implementați o funcție numita filter, cu acelasi comportament ca si functia predefintita filter, folosind reduce().
b) Implementați funcția exists care determină (returnează adevărat/fals) dacă există un element din listă care satisface o condiție (o funcție de element cu valoare booleană, dată ca parametru).
"""

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def filter_version(lst):
    return functools.reduce(lambda a, b: a + [b] if b % 2 else a, lst, [])

print(f"Filter version: {filter_version(lst)}")

def f(n):
    return n % 2

def exists(lst):
    if len(lst) == 0:
        return False
    elif f(lst[0]):
        return True
    else:
        return exists(lst[1:])
    
print(exists(lst))

# TODO 6

"""
6. a) Implementați folosind reduce o funcție countif care ia ca parametru o funcție f cu valori boolene și o listă și returnează numărul de elemente pentru care funcția f e adevărată.
"""

lst = [121, 2322, 33, 9257, 257, 205809, 259, 11]
def palindrom(n):
    return str(n)[0] == str(n)[-1]

def countif(lst, condition):
    return functools.reduce(lambda a, b: a + condition(b), lst, 0)

print(f"Numarul de palindroame din lista: {countif(lst, palindrom)}")

"""
b) Implementați similar o funcție sumif care calculează suma tuturor elementelor (presupuse întregi) pentru care funcția f e adevărată.
"""

def sumif(lst, condition):
    return functools.reduce(lambda a, b: a + b if condition(b) else a, lst, 0)

print(f"Suma palindroamelor din lista: {sumif(lst, palindrom)}")

# TODO: tema din Partea a II-a: ex 1. b,c; ex 2; ex 5; ex 6

# TODO 7

"""
7. Implementați funcțiile split și combine care transformă o listă de perechi într-o pereche de liste, și invers.
Ex: split([ (1,2), (3,4), 5,6)]) -> ([1,3,5], [2,4,6])  

combine([1,3,5], [2,4,6]) -> [ (1,2), (3,4), 5,6) ]
"""

lst = [(1, 2), (3, 4), (5, 6)]

def split(lst):
    new_lst = [[], []]
    for i in lst:
        new_lst[0].append(i[0])
        new_lst[1].append(i[1])

    return new_lst


def split_rec(lst):
    def aux():
        if len(lst) == 0:
            pass
        else:
            new_lst[0].append(lst[0][0])
            new_lst[1].append(lst[0][1])
            lst.pop(0)
            aux()

    new_lst = [[], []]
    aux()
    return new_lst


print(f"Split list: Iterative Method: {split(lst)}")
print(f"Split list: Recursive Method: {split_rec(lst)}")


lst = [[1, 3, 5], [2, 4, 6]]

def combine(lst):
    new_lst = []
    for i, j in zip(lst[0], lst[1]):
        new_lst.append([i, j])

    return new_lst


def combine_rec(lst):
    def aux():
        if len(lst[0]) == 0:
            pass
        else:
            new_lst.append([lst[0][0], lst[1][0]])
            lst[0].pop(0)
            lst[1].pop(0)
            aux()

    new_lst = []
    aux()
    return new_lst


print(f"Combine list: Iterative method: {combine(lst)}")
print(f"Combine list: Recursive method: {combine_rec(lst)}")


# TODO 8

"""
8. Implementați funcția partition care ia ca parametru o funcție cu valori boolene și o listă și returnează o pereche de liste, cu elementele care satisfac, respectiv nu satisfac funcția f.
# partition (lambda x : x >= 5) [4,6,7,5,4,8,9] -> ([6, 7, 5, 8, 9], [4, 4])

"""

lst = [4, 6, 7, 5, 4, 8, 9]

def partition(lst):
    return [list(filter(lambda x: x >= 5, lst)), list(filter(lambda x: not x >= 5, lst))]


print(f"Lista {lst} partitionata este: {partition(lst)}")

# TODO 9

"""
9. Scrieți o funcție care ia o listă de cifre și returnează valoarea numărului cu cifrele respective.
"""

cif_lst = [1, 2, 4, 2, 1, 5, 6, 7]

def form_number(lst):
    if len(lst) == 0:
        return 0
    else:
        return 10 * form_number(lst[:-1]) + lst[-1]


print(f"Valoarea numarului format cu lista {cif_lst} este: {form_number(cif_lst)}")


# TODO 10

"""
10. Scrieți o funcție care elimină duplicatele consecutive: ia ca parametru o listă și construiește o 
listă în care toate secvențele de elemente consecutive egale au fost înlocuite cu un singur element.
"""

lst = [1, 1, 2, 3, 2, 2, 4, 4, 2, 1, 5, 6, 7, 7, 7, 7, 7]
def elim_consec_dupl(lst):
    if len(lst) == 1:
        return [lst[0]]
    elif lst[0] == lst[1]:
        return elim_consec_dupl(lst[1:])
    else:
        print(lst[0], lst[1])
        return [lst[0]] + elim_consec_dupl(lst[1:])


print(f"Lista {lst} fara duplicate este: {elim_consec_dupl(lst)}")

# TODO 11

"""
11. Scrieți o funcție care compară două liste după următoarea relație de ordine: o listă mai scurtă e "mai mică" 
decât una mai lungă; dacă lungimile sunt egale, ordonarea e determinată de prima pereche de elemente diferite. 
Evitați parcurgerea inutilă sau repetată a listelor. 
Funcția va returna un întreg negativ, 0 sau pozitiv în funcție de ordonarea celor două liste argument.

-- strcmp --
>0 - l1 < l2
=0 - l1 = l2
<0 - l1 < l2
"""

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4, 5, 5]

def compare(lst1, lst2):
    # check if the lists are identical
    if lst1 == lst2:
        return 0
    # check for the length inequality test
    elif len(lst1) != len(lst2):
        return 1 if len(lst1) > len(lst2) else -1
    else:
        # the case when the length is the same
        def comp_aux(l1, l2):
            # stop condition
            if len(l1) == 0:
                return 0
            else:
                # check the first items of the lists
                if l1[0] > l2[0]:
                    return 1
                elif l1[0] < l2[0]:
                    return -1
                else:
                    # in case they are identical, hop on to the next pair of items
                    return comp_aux(l1[1:], l2[1:])

        return comp_aux(lst1, lst2)


print(f"strcmp({lst1}, {lst2}) = {compare(lst1, lst2)}")


# TODO 13

"""
13. Scrieți o funcție care desparte o listă în două liste a căror lungime diferă cu cel mult 1, 
punând alternativ câte un element în fiecare din liste. (Funcția va returna o pereche de liste).
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def half_list(lst):
    new_lst = [[], []]
    def aux():
        if len(lst) == 0:
            pass
        elif len(lst) == 1:
            new_lst[0].append(lst[0])
        else:
            new_lst[0].append(lst[0])
            new_lst[1].append(lst[1])
            lst.pop(0)
            lst.pop(0)
            aux()

    aux()
    return new_lst

print(f"The list {lst} split into 2: {half_list(lst)}")
