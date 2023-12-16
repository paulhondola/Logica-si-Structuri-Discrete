import re

'''
Tema: 
Scrie o expresie regulată pentru a valida un număr de telefon. Regulile sunt: 
Numărul de telefon poate să conțină caracterele: 0-9, "-", "(", ")" și poate începe cu "+". 
Dacă numărul de telefon începe cu "+", trebuie să urmeze cel puțin un caracter numeric. 
Numărul de telefon trebuie să aibă între 8 și 15 caractere (inclusiv).
'''

def validate_phone_number(phone_number):
    pattern = r"^((\+[0-9]+)?[0-9\-\,]){8,15}$"
    return re.match(pattern, phone_number) is not None

phone_number1 = "+40721234567"
phone_number2 = "0721234567"
phone_number3 = "0721-234-567"
phone_number4 = "+40-721-234-567"
phone_number5 = "0721-234567"
phone_number6 = "0721-2345678"
phone_number7 = "0721-234-567-89"
phone_number8 = "0721-234-567-890"
phone_number9 = "0721-234-567-8901"
phone_number10 = "0721-234-567-89012"


lst = [phone_number1, phone_number2, phone_number3, phone_number4, phone_number5, phone_number6, phone_number7, phone_number8, phone_number9, phone_number10]

for phone_number in lst:
    print(validate_phone_number(phone_number))
