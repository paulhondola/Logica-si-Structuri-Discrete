from functools import reduce

# TODO 4. Implementați funcția standard partition care ia ca parametri o funcție booleană f și o mulțime s și returnează o pereche de mulțimi, cu elementele din s care satisfac, respectiv nu satisfac funcția f.

# Input: lambda x: x % 2 == 0, {1, 2, 3, 4}; Output: ({2, 4}, {1, 3})

def standard_partition(multime, condition):
    
    partition = reduce(lambda acc, item: acc | {item} if condition(item) else acc, multime, set())
    return partition, multime - partition

print(standard_partition({1, 2, 3, 4}, lambda x: x % 2))



# TODO 5. Scrieți o funcție care ia o lista de mulțimi (de exemplu, de șiruri), și returnează reuniunea (variantă: intersectia) mulțimilor.

# Input: [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]; Output: reuniune: {1, 2, 3, 4, 5, 6, 7}; intersectie: {3}

def reuniune(lst):
    return reduce(lambda acc, multime: acc.union(multime), lst, set())

print(reuniune([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))


# TODO 6. Scrieți o funcție care returnează mulțimea cifrelor unui număr. Scrieți apoi altă funcție care ia o mulțime de numere și returnează reuniunea/intersecția dintre mulțimile cifrelor lor.

# Input: {1234, 123, 127}; Output: reuniune: {1, 2, 3, 4, 7}; intersectie: {1, 2}

def reuniune2(multime):
    return reduce(lambda acc, item: acc.union(map(lambda x: int(x), set(str(item)))), multime, set())

print(reuniune2({1234, 123, 127}))