with open('Codeit/Voca/vocabulary.txt', 'a', encoding="utf-8") as f:
    while True:
        English = input("영어 단어를 입력하세요: ")
        if English == 'q':
            break
        
        korean = input("한국어 뜻을 입력하세요: ")
        if korean == 'q':
            break
        
        f.write('{}: {}\n'.format(English, korean))