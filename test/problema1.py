import functools as ft

def subset(multime, conditie):
    return ft.reduce(lambda acc, item: acc | {item} if conditie(item) else acc, multime, set())
    

print(subset({1, 3, 4, 8, 9}, lambda x : x > 3))