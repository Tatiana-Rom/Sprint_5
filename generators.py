import random
import string

def generate_email():

    name = "tatiana"
    surname = "rom"
    cohort = "27"
    random_num = random.randint(100, 999)  
    return f"{name}_{surname}_{cohort}_{random_num}@yandex.ru"

def generate_password(min_length=6, max_length=100):

    chars = string.ascii_letters + string.digits
    length = random.randint(min_length, max_length)  
    return ''.join(random.choice(chars) for _ in range(length))