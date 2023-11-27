# TODO: TEMA ex 1, 2, 4

cheie = "cheie"
stanga = "stanga"
dreapta = "dreapta"

nod8 = {cheie: 8, stanga: None, dreapta: None}  # frunza
nod1 = {cheie: 1, stanga: None, dreapta: None}  # frunza
nod7 = {cheie: 7, stanga: None, dreapta: None}  # frunza
nod4 = {cheie: 4, stanga: nod8, dreapta: None}  
nod5 = {cheie: 5, stanga: nod4, dreapta: nod7}

radacina = {cheie: 2, stanga: nod1, dreapta: nod5}


'''
1. Scrieți o funcție care ia un arbore binar și returnează lista nodurilor care au un singur fiu. Ordinea nodurilor în listă va fi cea din traversarea în inordine.
'''

# TODO 1

def list_single_child_node(arbore):
    
    # end
    if arbore is None:
        return []
    
    # radacina
    if arbore[stanga] is None and arbore[dreapta] is None:
        return []
    
    # un singur fiu
    if (arbore[stanga] is not None and arbore[dreapta] is None) or (arbore[stanga] is None and arbore[dreapta] is not None):
        return list_single_child_node(arbore[stanga]) + [arbore[cheie]] + list_single_child_node(arbore[dreapta])

    # doi fii
    if arbore[stanga] is not None and arbore[dreapta] is not None:
        return list_single_child_node(arbore[stanga]) + list_single_child_node(arbore[dreapta])

print("Nodurile cu un singur fiu:", list_single_child_node(radacina))

'''
2. Scrieți o funcție careia un arbore binar și returnează numărul total de noduri din arbore.
'''

# TODO 2

def total_nodes(arbore):
    # end
    if arbore is None:
        return 0

    # continue
    return 1 + total_nodes(arbore[stanga]) + total_nodes(arbore[dreapta])
    
print("Numarul total de noduri este:", total_nodes(radacina))

'''
3. Parcurgerea arborilor oarecare Modificați funcțiile de parcurgere așa încât să funcționeze pe arbori oarecare (fiecare nod are o listă de fii). Folosiți funcții de parcurgere pe liste. Pentru inordine, parcurgeți întâi capul listei, apoi rădăcina și coada listei.
'''

# TODO 3

# arbore oarecare
key = "cheie"
child = "child"
node13 = {key: 13, child: [None]}
node12 = {key: 12, child: [None]}
node11 = {key: 11, child: [None]}
node10 = {key: 10, child: [None]}
node9 = {key: 9, child: [node12, node13]}
node8 = {key: 8, child: [None]}
node7 = {key: 7, child: [node11]}
node6 = {key: 6, child: [None]}
node5 = {key: 5, child: [None]}
node4 = {key: 4, child: [node9, node10]}
node3 = {key: 3, child: [node6, node7, node8]}
node2 = {key: 2, child: [node5]}
node1 = {key: 1, child: [node2, node3]}


def SRD(arbore):
    if arbore is not None:
        # functie externa care parcurge lista
        SRD(arbore[child][0])
        print(arbore[key], end = ', ')
        SRD(arbore[child][1:])
 
#print('Arbore oarecare:', end = ' ')       
#SRD(node1)

'''
4. Tipărire indentată Scrieți o funcție care afișează un arbore binar de întregi în preordine, câte un nod pe linie, precedând valoarea din nod cu un număr de spații egal cu dublul adâncimii la care se află (câte două spații pentru fiecare nivel).
'''

# TODO 4

def spaces(num):
    if num == 0:
        print('', end = '')
    else:
        spaces(num - 1)
    

def RSD(arbore, level = 1):
    if arbore is not None:
        print(arbore[cheie])
        spaces(level)
        RSD(arbore[stanga], level + 1)
        RSD(arbore[dreapta], level + 1)
        
RSD(radacina)
        
'''
5. Eliminarea unui nod Scrieți o funcție care ia ca parametru o valoare și un arbore binar de căutare și returnează arborele din care valoarea a fost eliminată (dacă exista).
'''

# TODO 5





'''
Indicații:

dacă arborele este nevid:
dacă valoarea dată este identică cu cheia rădăcinii atunci am găsit nodul căutat. Procedăm astfel:
dacă nodul este terminal (subarborele stâng și subarborele drept sunt vizi) se va șterge acest nod, iar adresa reținută de părinte pentru el devine None;
dacă numai subarborele stâng este nevid nodul se va șterge, iar adresa reținută de părinte pentru el devine adresa subarborelui stâng;
dacă numai subarborele drept este nevid nodul se va șterge, iar adresa reținută de părinte pentru el devine adresa subarborelui drept;
dacă ambii subarbori sunt nevizi:
se identifică cel mai mare nod din subarborele stâng (cel mai din dreapta nod al subarborelui stâng). Acest nod nu poate avea subarbore drept!
se copiază informația din acest nod în nodul analizat;
nodul identificat este șters. Ștergerea se realizează ca în cazul în care nodul este terminal sau ca în cazul în care nodul are numai subarbore stâng;
dacă valoarea dată este mai mică decât cheia rădăcinii, se continuă căutarea în subarborele stâng;
dacă valoarea dată este mai mare decât cheia rădăcinii, se continuă căutarea în subarborele drept;
dacă arborele este vid:
valoarea căutată nu există în arbore.
'''