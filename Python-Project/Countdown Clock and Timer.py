# 사용자가 타이머를 설정하며, 시간이 되면 앱이 알려준다.

# [python 문법, 정리]
# divmod는 ()분을 초단위로 계산한다. 몫과 나머지를 한번에 구할 수 있다.
# timeformat을 통해 분과 초를 인쇄한다.
# 사용종료 = '\r'에 인쇄된 다음 라인이 이전을 덮어씌운다. \r :해당 줄의 처음으로 이동한다.
# time.sleep()는 일정 시간동안 프로세스를 일시정지한다. (실수 단위도 가능)


import time

def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Finish CountDown!")

t = int(input("Enter the time in seconds: "))

countdown(t)