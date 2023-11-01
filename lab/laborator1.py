import math

def functie1():
    print("LSD")

def suma(a, b):
    s = a + b
    print(f"suma este = {s}")

def diferenta(a, b):
    d = a - b
    return d # sau direct: return a - b

def suma_si_diferenta(a,b):
    s = a + b
    d = a - b
    return s, d

def minim(a,b):
    if a < b:
        return a
    else:
        return b

def ultima_cifra(c):
    return c%10 # 453/10 = 45    453%10 = 3

def compus(o,h,c):
    return 16*o+h+12*c

def ecuatie_gr2(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Nu exista solutii reale.")
    elif delta == 0:
        print(-b / (2 * a))
    else:
        print((-b - math.sqrt(delta)) / (2 * a), " si ", (-b + math.sqrt(delta)) / (2 * a))

if __name__ == '__main__':
    """ afisare """
    print("LSD 2023")

    """ tipuri de date"""
    a = 7
    print(f"valoarea = {a}, tipul = {type(a)}")

    a = 7.0
    print(f"valoarea = {a}, tipul = {type(a)}")

    a = True
    print(f"valoarea = {a}, tipul = {type(a)}")

    a = "LSD"
    print(f"valoarea = {a}, tipul = {type(a)}")

    """ definire functie: fara parametrii, cu parametrii, cu mai multe valori de return"""
    functie1()
    suma(2,8)

    # varianta 1
    print(f"diferenta = {diferenta(10,5)}")

    # varianta 2
    d = diferenta(10,5)
    print(f"diferenta = {d}")

    s, d = suma_si_diferenta(12, 5)
    print(f"suma = {s} diferenta = {d}")

    """ functii predefinite """
    print(f"minimul = {min(5,9)}")
    print(f"pow = {pow(2, 3)}")
    print(f"sqrt = {math.sqrt(4)}")

    """ instructiunea if"""
    print(minim(5,6))

    """ exercitii propuse"""

    "Exercițiul 1: Ultima cifră Scrieți o funcție în Python care returnează ultima cifră a numărului primit ca parametru."

    print(ultima_cifra(453))

    """
    Exercițiul 2: Compus chimic 
    Scrieți o funcție în Python care primește ca parametri numărul de atomi de carbon, de hidrogen, 
    respectiv de oxigen al unui compus chimic și returnează masa moleculară
    a substanței corespunzătoare, cunoscând faptul că oxigenul are masa atomică 16, hidrogenul 1, iar carbonul 12.
    """
    print(compus(1,1,1))

    """
    Exercițiul 3: Ecuația de gradul 2
    Scrieți o funcție în Python care primește ca parametri trei întregi a, b, respectiv c, și tipărește soluțiile ecuației 
    de gradul doi ax2 + bx + c = 0, sau un mesaj daca nu există soluții reale.
    """

    ecuatie_gr2(1, -13, 30)
    

    """TEMA EX: 4, 5, 6, 7, 9 """
