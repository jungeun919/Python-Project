import random

random_voca = {}
with open('Codeit/Voca/vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.split(": ")
        English, korean = data[0], data[1].strip()
        random_voca[English] = korean # random_voca dict에 추가

while True:
    keys = list(random_voca.keys()) # English
    index = random.randint(0, len(keys) - 1)

    English = keys[index]
    korean = random_voca[English]

    guess = input(f'{korean}: ')
    if guess == 'q':
        break
    elif guess == English:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(English))