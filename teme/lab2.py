# lab2

# exercitiul 1

"""
Exercițiul 1: valori distincte

Scrieți o funcție cu trei parametri (de același tip oarecare),
care returnează câte valori distincte există între argumentele primite
(unul, două sau trei) și tipărește, după caz,
un mesaj: "toate argumentele sunt distincte/egale" sau
"argumentele 1 și 2 (resp. 2 și 3, sau 1 și 3) sunt egale".
Evitați pe cât posibil duplicarea de cod: pentru porțiuni de cod
similare, creați (și apelați) o funcție care conține partea comună și are
ca parametri valorile care diferă.
"""

def compare2(x, y, poz1, poz2):
    if x == y:
        print(f"argumentele {poz1} și {poz2} sunt egale")

def compare3(x, y, z):
    if x == y == z:
        print("toate argumentele sunt egale")
    elif x != y != z:
        print("toate argumentele sunt distincte")
    else:
        compare2(x, y, 1, 2)
        compare2(x, z, 1, 3)
        compare2(y, z, 2, 3)


a = 1
b = 2
c = 5
compare3(a, b, c)


# exercitiul 2

"""
Exercițiul 2: mediana

Scrieți o funcție care calculează mediana a trei valori (valoarea aflată între celelalte două).
Încercați să scrieți cod cât mai simplu, și să nu-l repetați. 
Puteți folosi o funcție auxiliară care calculează mediana a trei numere, 
pentru care știm că primul e mai mic sau egal decât al doilea. 
Sau puteți încerca să compuneți doar funcțiile standard max/min de două elemente 
(expresia trebuie să fie oarecum simetrică). Care din variante necesită mai puține comparații?
"""
def mediana(x, y, z):
    return x + y + z - max(x, y, z) - min(x, y, z)


a = 4
b = 5
c = 6

print(mediana(a, b, c))

# exercitiul 3

"""
Exercițiul 3: operații cu funcții
În matematică, am extins uneori operatorul + de la numere la funcții, defining funcția f + g prin 
relația (f + g)(x) = f(x) + g(x)
a) Definiți o funcție care ia ca parametru două funcții f și g și returnează funcția definită ca suma 
lor prin relația de mai sus.
b) Scrieți o funcție mai generală, care primește ca parametru și operatorul binar 
(o funcție de două argumente) care e aplicată celor două funcții. Verificați că o puteți folosi 
cu operator.add și operator.sub pentru a calcula suma și diferența, dar încercați și alți operatori.
"""

import operator
def addfunc(f, g):
    return lambda x: f(x) + g(x)


def func_op(f, g, op):
    return lambda x: op(f(x), g(x))


def f1(x):
    return x


def f2(x):
    return x


print(func_op(f1, f2, operator.pow)(3))

# exercitiul 4


"""
Exercițiul 4: functie anonima
Scrieti o funcție anonima care adaugă 15 la un număr dat ca argument.
"""

x = 10
print((lambda x: x + 15)(x))
