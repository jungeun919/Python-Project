import datetime
import os
import time
import random
import webbrowser


print(os.path.isfile("Python-Project/Alarm_Clock/youtube_alarm_videos.txt"))
with open("Python-Project/Alarm_Clock/youtube_alarm_videos.txt", "r") as alarm_file:
	print(alarm_file.read())


if not os.path.isfile("Python-Project/Alarm_Clock/youtube_alarm_videos.txt"):
	print('Creating "youtube_alarm_videos.txt"...')
	os.mkdir("Python-Project/Alarm_Clock/youtube_alarm_videos.txt")
	with open("Python-Project/Alarm_Clock/youtube_alarm_videos.txt", "w") as alarm_file:
		alarm_file.write("https://www.youtube.com/watch?v=gdZLi9oWNZg")


def check_alarm_input(alarm_time):
	# 사용자가 유효한 알람 시간을 입력했는지 확인한다.
	if len(alarm_time) == 1: # [Hour]
		if alarm_time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(alarm_time) == 2: # [Hour:Minute]
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0:
			return True
	elif len(alarm_time) == 3: # [Hour:Minute:Second]
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0 and \
		   alarm_time[2] < 60 and alarm_time[2] >= 0:
			return True
	return False


while True:
	alarm_input = input("알람 시간을 설정하세요 (HH:MM or HH:MM:SS): ")
	try:
		alarm_time = [int(n) for n in alarm_input.split(":")]
		if check_alarm_input(alarm_time):
			break
		else:
			raise ValueError
	except ValueError:
		print("ERROR: [HH:MM] / [HH:MM:SS] 형식으로 입력하세요.")


# 알람 시간을 [H : M] 또는 [H : M : S]에서 초로 변환한다.
seconds_hms = [3600, 60, 1]
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# 현재 시간을 초 단위로 가져온다.
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = alarm_seconds - current_time_seconds

if time_diff_seconds < 0:
	time_diff_seconds += 86400

print("남은 시간: %s" % datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)
print("Wake Up")

with open("Python-Project/Alarm_Clock/youtube_alarm_videos.txt", "r") as alarm_file:
	videos = alarm_file.readlines()

webbrowser.open(random.choice(videos))