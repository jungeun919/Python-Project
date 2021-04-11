import random
import string


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNTUATION = string.punctuation

def get_password_length():
    length = int(input("원하는 Password의 길이를 입력하세요: "))
    return length

def password_generator(length):
    printable = f'{LETTERS}{NUMBERS}{PUNTUATION}'

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

password_length = get_password_length()
password = password_generator(password_length)

print("\n길이가", password_length, "인 임의의 문자열:", password)