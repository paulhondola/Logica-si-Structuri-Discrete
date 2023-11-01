"""
Recursivitatea este un concept fundamental în matematică și în programare ce presupune ca în definirea unei noțiuni să se facă referire la ea însăși.
FOARTE IMPORTANT! În cadrul oricărei definiții recursive trebuie să existe măcar un caz de bază (elementar),
la care să se ajungă după parcurgerea unui anumit număr de pași.


Știm deja din laboratoarele anterioare că putem defini funcții care în interiorul lor pot apela alte funcții.
Putem chiar să definim funcții care să se apeleze pe ele însăși. O astfel de funcție care apare în propria sa
definiție poartă numele de funcție recursivă.

Exemplu: Factorial
factorial 5! = 1*2*3*4*5 sau 5*4*3*2*1

factorial(5) ->  5 * factorial(4)
                        -> 4 * factorial(3)
                                ->  3 * factorial(2)
                                            ->  2 * factorial(1)
                                                        -> 1
                                            <-    2*1    <- 1
                                <-   3*2*1
                        <- 4*3*2*1
               <- 5*4*3*2*1
return 5*4*3*2*1 = 120
"""


def factorial_notok(n):
    return n * factorial(n - 1)  # de ce nu este corecta varianta data?


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f"factorial(3)={factorial(3)}")

"""
Limitarile python in ceea ce priveste recursivitatea:

Exercițiul 3: Suma primelor N numere naturale
Implementați în Python o funcție recursivă pentru a calcula suma primelor N numere naturale.
"""


def suma_n_numere(n):
    if n == 1:
        return 1
    else:
        return n + suma_n_numere(n - 1)


print(f"suma_n_numere(7)={suma_n_numere(7)}")
print(f"suma_n_numere(995)={suma_n_numere(995)}")
# print(f"suma_n_numere(1000)={suma_n_numere(1000)}")  # maxim 988 de elemente in stiva

"""
Exercitiu: Scrieti o functie recursiva care afiseaza numerele de la n la 1 in ordine descrescatoare.
"""


# TODO: rezolvare exercitiu

def afisare_n_1(n):
    if n >= 1:
        print(n, end=",")
        afisare_n_1(n - 1)


afisare_n_1(7)

"""
Exercitiu: Scrieti o functie recursiva care afiseaza numerele de la 1 la n in ordine crescatoare.
"""

# TODO: rezolvare exercitiu

def afisare_1_n(n):
    if n >= 1:
        afisare_1_n(n - 1)
        print(n, end=",")

print()
afisare_1_n(7)


"""
Exercițiul 1: Progresie aritmetică
Implementați în Python o funcție recursivă pentru a calcula valoarea termenului de rang n,
pentru progresia aritmetică definită de relația:  a(n)=2×a(n−1)−3
Se consideră valoare termenului a(0)=2.
Funcția va primi ca unic parametru numărul natural n.
"""
# TODO: rezolvare exercitiu

def pa(n):
    if n == 0:
        return 2
    else:
        return 2*pa(n-1)-3

print()
print(f"pa(3)={pa(2)}")

"""
Exercițiul 4: Cifrele unui număr
a) Implementați în Python o funcție recursivă pentru a calcula produsul cifrelor unui număr dat ca parametru.
"""

# TODO: rezolvare exercitiu


def prod_cifre(n):
    if n < 10:
        return n
    else:
        return n%10*prod_cifre(n//10)   # // impartire fara rest

print(f"prod_cifre(1234)={prod_cifre(123)}")

"""
Exercițiul 6: Număr prim
Implementați în Python o funcție care returneaza True dacă un număr  n este prim, altfel False.
"""

# TODO: rezolvare exercitiu


def aux(n, i):
    if i <= n / 2:
        if n % i == 0:
            return False
        else:
            return aux(n, i + 1)
    else:
        return True


def prim(n):
    if n == 1:
        return False
    else:
        return aux(n,2)


print(prim(13))
print(prim(14))
print(prim(7))

# TODO: TEMA Exercițiul 4: b,c,d
# TODO: Exercițiul 5
# TODO: Exercițiul 9
