import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser') # u.content에 대해서 html 파싱하겠다.
    title = soup.find(class_ = "firstHeading").text
    print(title)
    print("Do you want to view it? (Y/N)")
    ans = input()

    if ans.lower() == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break

    elif ans.lower() == "n":
        print("Trying Again")
        continue

    else:
        print("Wrong Choice")
        break