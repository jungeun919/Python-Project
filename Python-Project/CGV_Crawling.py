from bs4 import BeautifulSoup
import requests

url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0074&date=20210411'
html = requests.get(url)
# print(html.text)

# bs4로 cgv 상영시간표 영화 제목 크롤링하기
print("[CGV movie-title crawling]")
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())
print()

# imax 영화 예매 오픈 여부, 예매 오픈된 imax 영화 제목 크롤링하기
print("[CGV imax-movie-title crawling]")

imax = soup.select_one('span.imax')
if (imax):
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(title + " IMAX 예매가 열렸습니다.")
else:
    print("IMAX 예매가 아직 열리지 않았습니다.")