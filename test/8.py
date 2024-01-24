
cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"

nod8 = {cheie: 8, stanga: None, dreapta: None}  # frunza
nod1 = {cheie: 1, stanga: None, dreapta: None}  # frunza
nod7 = {cheie: 7, stanga: None, dreapta: None}  # frunza
nod4 = {cheie: 4, stanga: nod8, dreapta: None}  
nod5 = {cheie: 5, stanga: nod4, dreapta: nod7}

radacina = {cheie: 2, stanga: nod1, dreapta: nod5}

# TODO 1. Scrieți o funcție care ia un arbore binar și returnează lista nodurilor care au un singur fiu. Ordinea nodurilor în listă va fi cea din traversarea în inordine

# pre , in , post - RSD, SRD, SDR

def print_SRD(root):
    if root is not None:
        print_SRD(root[stanga])
        print(root[cheie])
        print_SRD(root[dreapta])


def list_single_node_child(root):
    if root is None:
        return []
    
    if root[stanga] is None and root[dreapta] is None:
        return []
    
    if root[stanga] is not None and root[dreapta] is not None:
        return list_single_node_child(root[stanga]) + list_single_node_child(root[dreapta])
    
    return list_single_node_child(root[stanga]) + [root[cheie]] +list_single_node_child(root[dreapta])

print(list_single_node_child(radacina))


# TODO 2. Scrieți o funcție careia un arbore binar și returnează numărul total de noduri din arbore.


def total_nodes(root):
    if root is None:
        return 0
    
    return total_nodes(root[stanga]) + total_nodes(root[dreapta]) + 1


print(total_nodes(radacina))
