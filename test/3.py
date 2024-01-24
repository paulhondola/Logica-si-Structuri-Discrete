def create_dict(key_list, value_list):
    
    if(key_list == [] or value_list == []):
        return {}
    
    return {key_list[0] : value_list[0]} | create_dict(key_list[1:], value_list[1:])


print(create_dict([1, 18, 118], [0, 1, 1, 1]))