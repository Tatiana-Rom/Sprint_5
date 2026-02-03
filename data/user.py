import random

class PersonData:
    user_name = 'Татьяна'
    login = f"tatiana_rom_27_575@yandex.ru"
    password = f"978673346"
    
class ValidData:
    user_name = 'Татьяна'
    login = f"tatiana_rom_27_{random.randint(100, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(100, 999)}"
