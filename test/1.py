'''
5

5 / 2 - 1
2 / 2 - 0
1 / 2 - 1

'''

def convert_to_binary(number):
    
    if number == 0:
        return []
    
    return convert_to_binary(number // 2)+ [number % 2]

print(convert_to_binary(29))