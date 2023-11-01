#lab 1 - tema
import math


# problema 1 - ultima cifra a unui nr
def uc(nr):
    return nr % 10


# problema 2 - compus chimic
def masa_atomica(car, hidro, oxi):
    return 12 * car + hidro + 16 * oxi


# problema 3 - ecuatia de gradul 2
def ec_gr2(a, b, c):
    delta = b * b - (4 * a * c)
    if delta < 0:
        print(f"Ecuatia {a}x^2 + {b}x + {c} = 0 nu are solutii reale.")
    elif delta == 0:
        root = (-1 * b) / (2 * a)
        print(f"Ecuatia are ca radacina dubla pe {root}")
    else:
        root1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        root2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print(f"Ecuatia are ca radacini pe {root1} si {root2}")


# problema 4 - an bisect
def bisect(an):
    if an % 4 == 0 and an % 100 != 0:
        return True
    elif an % 400 == 0:
        return True
    else:
        return False


# problema 5 - functie pe ramuri
def f(x):
    if x < -3:
        return 2 * x + 1
    elif x == -3:
        return 0
    else:
        return 3 * x * x + 6 * x - 5


# problema 6 - interval
def interval(a, b, c):
    return a <= c <= b


# problema 7 - sort
def sort3(a, b, c):
    return max(a, b, c), min(max(a, b), max(b, c)), min(a, b, c)


# problema 8 - ora plecare / sosire
def dif_timp(plecare, sosire):
    # HH:MM:SS
    h_plecare = int(plecare[0:2])
    m_plecare = int(plecare[3:5])
    s_plecare = int(plecare[6:8])

    h_sosire = int(sosire[0:2])
    m_sosire = int(sosire[3:5])
    s_sosire = int(sosire[6:8])

    if s_sosire < s_plecare:
        if m_sosire > 0:
            m_sosire -= 1
            s_sosire += 60
        else:
            h_sosire -= 1
            m_sosire += 59
            s_sosire += 60

    if m_sosire < m_plecare:
        h_sosire -= 1
        m_sosire += 60

    h = h_sosire - h_plecare
    m = m_sosire - m_plecare
    s = s_sosire - s_plecare
    return 3600 * h + 60 * m + s


# problema 9 - lungimea si aria unui cerc
def lung_arie_cerc(radius):
    L = 2 * math.pi * radius
    A = math.pi * radius * radius
    return L, A


# problema 10 - numarul de zile
"""
def bisect(an):
    if an % 4 == 0 and an % 100 != 0:
        return True
    elif an % 400 == 0:
        return True
    else:
        return False
"""


def dif_ani(an1, an2):
    zile = 0
    for i in range(an1, an2):
        zile += 365
        if bisect(i):
            zile += 1
    return zile
