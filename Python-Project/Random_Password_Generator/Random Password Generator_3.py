import random
import string


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNTUATION = string.punctuation

def get_password_length():
    length = int(input("원하는 Password의 길이를 입력하세요: "))
    return length

def password_generator(cbl, length):
    printable = fetch_string_constant(cbl)

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

def combination_choice():
    want_letters = input("Want Letters? (True/False): ")
    want_digits = input("Want Digits? (True/False): ")
    want_punctuation = input("Want Punctuation? (True/False): ")

    try:
        want_letters = eval(want_letters.title())
        want_digits = eval(want_digits.title())
        want_punctuation = eval(want_punctuation.title())
        return [want_letters, want_digits, want_punctuation]

    except NameError as e:
        print()
        print(e)
        print("Invalid value. Use either True or False")

    # return [True, True, True]
    return [want_letters, want_digits, want_punctuation]

def fetch_string_constant(choice_list):
    string_constant = ''
    string_constant += LETTERS if choice_list[0] else ''
    string_constant += NUMBERS if choice_list[1] else ''
    string_constant += PUNTUATION if choice_list[2] else ''
    return string_constant


if __name__ == '__main__':
    length = get_password_length()
    choice_list = combination_choice()
    password = password_generator(choice_list, length)
    print("\n길이가", length, "인 임의의 문자열:", password)