import functools

"""
MULTIMI
Scrieți o funcție care primește o listă de șiruri de caractere și returnează o mulțime conținând literele unice din toate șirurile.

Input: ['apple', 'banana', 'cherry']; Output: {'a', 'b', 'c', 'e', 'h', 'l', 'n', 'p', 'r', 'y'}
"""

# TODO: exercitiu

def unique_letters(lst):
    if len(lst) == 0:
        return set()
    
    def include_letters_in_set(text):
        if len(text) == 0:
            return set()

        return {text[0]} | include_letters_in_set(text[1:])
        
    return include_letters_in_set(lst[0]) | unique_letters(lst[1:])

print("Lista de caractere:", unique_letters(['apple', 'banana', 'cherry']))


# set ('ana') = {'a', 'n'}
"""
DICTIONARE
Scrieți o funcție care primește o funcție și un dicționar și returnează maximul valorilor funcției pentru toate intrările dicționarului.
Funcția-parametru are ca argumente cheia și valoarea unei intrări, și poate returna valori arbitrare. 
Folosiți reduce pentru parcurgere, și max (definită implicit pentru orice tip) pentru a 
compara valorile returnate de funcția parametru.
"""
# TODO: exercitiu

my_dict = {
    'key1' : 1,
    'key2' : 2,
    'key3' : 3,
    'key4' : 4,
    'key5' : 5,
    'key6' : 6,
}

def random_func(dict_item):
    key, value = dict_item
    return 2 * value - 7


def max_func_value(my_dict, function):
    return max(functools.reduce(lambda acc, item: acc | {function(item)}, my_dict.items(), set()))


print('Max -> mapped dict',max_func_value(my_dict, random_func))

"""
ARBORI

Definiti un arbore binar cu valori intregi pozitive, apoi scrieti o functie care:
 A. calculeaza suma tuturor nodurilor din arbore.
 B. calculeaza maximul tuturor nodurilor din arbore.
"""

# TODO: exercitiu

key = 'key'
left = 'left'
right = 'right'

node7 = {key: 7, left: None, right: None}
node4 = {key: 4, left: None, right: node7}
node6 = {key: 6, left: None, right: None}
node5 = {key: 5, left: None, right: None}
node2 = {key: 2, left: node5, right: node6}
node1 = {key: 1, left: node2, right: node4}


def list_binary_tree_nodes(tree):
    if tree is None:
        return set()
    else:
        return {tree[key]} | list_binary_tree_nodes(tree[left]) | list_binary_tree_nodes(tree[right])
    
def sum_binary_tree(tree):
    return sum(list_binary_tree_nodes(tree))

def max_binary_tree(tree):
    return max(list_binary_tree_nodes(tree))


print('Sum ->', sum_binary_tree(node1))
print('Max ->', max_binary_tree(node1))

 
 
#########################################################################################################

lst = [6, 5, 8, 1, 7, 10, 2, 9, 3, 4]


# generate binary tree from lst

def generate_binary_tree(lst):
    tree = {key: lst[0], left: None, right: None}
    
    for i in range(1, len(lst)):
        current_node = tree
        while True:
            if current_node[key] > lst[i]:
                if current_node[left] is None:
                    current_node[left] = {key: lst[i], left: None, right: None}
                    break
                else:
                    current_node = current_node[left]
            else:
                if current_node[right] is None:
                    current_node[right] = {key: lst[i], left: None, right: None}
                    break
                else:
                    current_node = current_node[right]
    
    return tree

def SRD(tree):
    if tree is not None:
        SRD(tree[left])
        print(tree[key], end = ', ')
        SRD(tree[right])
    
    
print(SRD(generate_binary_tree(lst)))
        