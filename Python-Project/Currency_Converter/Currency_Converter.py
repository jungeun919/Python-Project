# pip install tkinter - 아직x
# pip install requests

import requests

class Currency_converter:
    rates = {}
    def __init__(self, url):
        data = request.get(url).json()
        # json data에서 요금만 뽑아낸다.
        self.rates = data['rates']

    # 교차곱셈함수 (amount, conversion rates)
    def convet(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currenct != 'EUR':
            amount = amount / self.rates[from_currency]

        # 정밀도를 소수점 이하 두자리로 제한한다.
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format\
            (initial_amount, from_currency, amount, to_currency))

if __name__ == "__main__":
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    c = Currency_converter(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount: "))