import re

def normalize_phone(phone_number):
    # delete all symbols without +
    phone_number = re.sub(r'\D', '', phone_number)

    # check the prefix + 
    if not phone_number.startswith('+'):
        # check the prefix '38'
        if not phone_number.startswith('380'):
            #add the prefix
            phone_number = '380' + phone_number[1:]
        else:
            phone_number = '+' + phone_number

    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
