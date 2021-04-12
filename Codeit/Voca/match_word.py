with open('Codeit/Voca/vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.split(": ")
        English, korean = data[0], data[1].strip() # \n 제거
        
        guess = input(f'{korean}: ')
        if guess == English:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(English))