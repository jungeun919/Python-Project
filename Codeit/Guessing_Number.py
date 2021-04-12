import random

ANSWER = random.randint(1, 20)
NUM_TRIES = 4

guess = -1
tries = 0

while ANSWER != guess and NUM_TRIES > tries:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(tries)))
    tries += 1
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")
        
if ANSWER == guess:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))