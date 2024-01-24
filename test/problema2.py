def sum_cif_pare(numar):
    if numar == 0:
        return 0
    
    if numar % 2 == 0:
        return numar % 10 + sum_cif_pare(numar // 10)
    
    else:
        return sum_cif_pare(numar // 10)

def sum_cif_pare_list(lista):
    return list(map(sum_cif_pare, [3472, 490, 222222, 111]))

print(sum_cif_pare_list([3472, 490, 222222, 1111]))
