# multimea divizorilor unui numar

def div_list(number, div = 1):
    
    if div == number:
        return set()
    
    return {div} | div_list(number, div + 1) if number % div == 0 else div_list(number, div + 1)


print(div_list(15))