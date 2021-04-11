import random
import string

def get_random_string(length):
    letters = string.ascii_letters
    password = ''.join(random.choice(letters) for i in range(length))
    print("\n길이가", length, "인 임의의 문자열:", password)

get_random_string(8)