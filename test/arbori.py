# 10 -> 8 + 2 -> 3 + 5 / 2

key = 'key'
right = 'right'
left = 'left'

node2 = {key: 2, right: None, left: None}
node5 = {key: 5, right: None, left: None}
node3 = {key: 3, right: None, left: None}

node2_upper = {key: 2, right: None, left: node2}
node8 = {key: 8, right: node5, left: node3}

root = {key: 10, right: node8, left: node2_upper}

def check_binary_tree(root):
    
    # frunza
    
    if root[left] is None and root[right] is None:
        return True
    
    # stanga
    
    if root[left] is not None and root[right] is None:
        if root[key] != root[left][key]:
            return False
        else:
            return check_binary_tree(root[left])
        
    # dreapta
    
    if root[left] is None and root[right] is not None:
        if root[key] != root[right][key]:
            return False
        else:
            return check_binary_tree(root[right])
        
    # ambele
    
    if root[left] is not None and root[right] is not None:
        if root[key] != (root[left][key] + root[right][key]):
            return False
        else:
            return check_binary_tree(root[left]) and check_binary_tree(root[right])


print(check_binary_tree(root))