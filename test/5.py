from functools import reduce

"""
b) Implementați o funcție care construiește lista cifrelor unui număr care satisfac o condiție dată ca parametru sub forma unei funcții cu tipul int -> bool.
"""

def make_digit_list(number, condition):
    if number == 0:
        lista = [0]
    
    def aux(aux_num):
        
        if aux_num == 0:
            return []
        
        return aux(aux_num // 10) + [aux_num % 10]
    
    lista = aux(number)
    
    return list(filter(condition, lista))
        
print(make_digit_list(352252515588720, lambda x: x > 3))


def make_digit_list_reduce(number, condition):
    
    return reduce(lambda acc, item: acc + [int(item)] if condition(int(item)) else acc, str(number), [])

print(make_digit_list_reduce(352252515588720, lambda x: x > 3))
    


"""
c) Invers, dată fiind o listă de cifre, construiți numărul format doar din cifrele care respectă o condiție (dată ca parametru funcție cu tipul int -> bool). Rezolvați problema direct, recursiv, și apoi prin folosirea lui filter (selectarea cifrelor) cu reduce (pentru construirea numărului).
"""

def make_number(lista, condition, number = 0):
    
    if lista == []:
        return number
    
    return make_number(lista[1:], condition, 10 * number + lista[0]) if condition(lista[0]) else make_number(lista[1:], condition, number)
    
print(make_number([3, 5, 2, 2, 5, 2, 5, 0, 5, 5, 8, 8, 7, 2, 0], lambda x: x > 3))




# TODO 2

"""
2. Implementați funcția fromto care generează lista numerelor întregi dintr-un interval dat, scrieți o funcție care creează lista tuturor întregilor dintr-un interval dat, divizibili cu o valoare dată d.
Indicație: Găsiți cel mai mare număr divizibil din interval, și continuați pas cu pas.
"""

# [1 - 20] -> div cu o valoare


def from_to(front, back, divizor):
    
    def find_smallest_div(number):
        if number % divizor == 0:
            return number
            
        return find_smallest_div(number + 1)
    
    
    def generate_list(iterator):
        if iterator > back:
            return []
    
        return [iterator] + generate_list(iterator + divizor)
        
    return generate_list(find_smallest_div(front))
    
    
print(from_to(7, 100, 13))


# TODO 3
"""
3. a) Implementați funcția nth care returnează al n-lea element dintr-o listă.
b) Implementați o funcție firstn care returnează o listă cu primele n elemente dintr-o listă dată.
"""

def return_nth(lst, n):
    return lst[n]

def return_first_nth(lst, n, index = 0):
    if index == n:
        return []

    return [lst[index]] + return_first_nth(lst, n, index + 1)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 6
print(return_first_nth(lst, n))
print(lst[:n])


# TODO 7

"""
7. Implementați funcțiile split și combine care transformă o listă de perechi într-o pereche de liste, și invers.
Ex: split([ (1,2), (3,4), 5,6)]) -> ([1,3,5], [2,4,6])  

combine([1,3,5], [2,4,6]) -> [ (1,2), (3,4), 5,6) ]
"""

def split(lst):
    return (reduce(lambda acc, pair: acc + [pair[0]], lst, []) ,reduce(lambda acc, pair: acc + [pair[1]], lst, []))

print( split ( [ (1,2), (3,4), (5,6) ] ) )


def zip_list(lst):
   return list(zip(lst[0], lst[1]))
    
def combine(lst):
    
    def aux(lst0, lst1):
        if lst0 == []:
            return []
        
        return [(lst0[0], lst1[0])] + aux(lst0[1:], lst1[1:])
    
    return aux(lst[0], lst[1])

    
print( combine ( ([1,3,5], [2,4,6]) ) )


# TODO 13

"""
13. Scrieți o funcție care desparte o listă în două liste a căror lungime diferă cu cel mult 1, 
punând alternativ câte un element în fiecare din liste. (Funcția va returna o pereche de liste).
"""

#  [1, 3, 5, 7, 9] [2, 4, 6, 8]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def skip_list(lst, lst0 = [], lst1 = []):
    
    if len(lst) == 0:
        return lst0, lst1
    
    elif len(lst) == 1:
        lst0.append(lst[0])
        return lst0, lst1
        
    else:
        lst0.append(lst[0])
        lst1.append(lst[1])
        return skip_list(lst[2:])
    
print(skip_list(lst))