# 4. Implementați funcția standard partition care ia ca parametri o funcție booleană f și o mulțime s și returnează o pereche de mulțimi, cu elementele din s care satisfac, respectiv nu satisfac funcția f.

# Input: lambda x: x % 2 == 0, {1, 2, 3, 4}; Output: ({2, 4}, {1, 3})

# TODO 4

import functools

def standard_partition(mul, condition):
    multime1 = functools.reduce(lambda acc, item: acc | {item} if condition(item) else acc, mul, set())
    multime2 = mul - multime1
    return multime1, multime2      
    
print("Standard partition:", standard_partition({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, lambda x: x % 2 == 0))


# 5. Scrieți o funcție care ia o lista de mulțimi (de exemplu, de șiruri), și returnează reuniunea (variantă: intersectia) mulțimilor.

# Input: [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]; Output: reuniune: {1, 2, 3, 4, 5, 6, 7}; intersectie: {3}

# TODO 5

lst = [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]

def reuniune(lst):
    if len(lst) == 0:
        return set()
    else:
        return set(lst[0]) | reuniune(lst[1:])

print("Reuniune:", reuniune(lst))

def intersectie(lst):
    if len(lst) == 0:
        return set()
    else:
        return set(lst[0]) & intersectie(lst[1:])

print("Intersectie:", intersectie(lst))

# 6. Scrieți o funcție care returnează mulțimea cifrelor unui număr. Scrieți apoi altă funcție care ia o mulțime de numere și returnează reuniunea/intersecția dintre mulțimile cifrelor lor.

# Input: {1234, 123, 127}; Output: reuniune: {1, 2, 3, 4, 7}; intersectie: {1, 2}

# TODO 6

mul = {1234, 123, 127}

def make_set_decimals(num):
    if num == 0:
        return {0}
    else:
        def f_aux(aux):
            if aux == 0:
                return set()
            else:
                return {aux % 10} | f_aux(aux // 10)
    
        return f_aux(num); 

def reunion_decimals(my_set):
    return functools.reduce(lambda acc, item: acc | make_set_decimals(item), my_set, set()) 
     
def intersection_decimals(my_set):
    my_universe = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}           
    return functools.reduce(lambda acc, item: acc & make_set_decimals(item), my_set, my_universe) 
     
print("Reunion:", reunion_decimals(mul))
print("Intersection:", intersection_decimals(mul))
