def convert_to_binary(number):
    if number == 0:
        return ''
    
    return convert_to_binary(number // 2) + str(number % 2)

print(convert_to_binary(29))