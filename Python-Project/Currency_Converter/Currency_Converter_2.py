# https://medium.com/@soumyabrataroy/creating-currency-converter-python-6a15b4e69fbb
# https://colab.research.google.com/drive/1MMhHoEqPm7JcJSeNep5E2RCYGnzXLzCA?usp=sharing#scrollTo=g323f4jUiRtj

import requests

def currency_converter_1():
        old_or_latest = input("Do you want the latest or historical value?\nif latest, please type 'latest' or else type historical value in '%Y-%m-%d' format:\t")
        base_URL_new = 'https://api.exchangeratesapi.io/'+old_or_latest 
    
        
        response = requests.get(base_URL_new, params='base=USD')
           
        if response.status_code == 200:
            data,base_value, Date = response.json().items()
            print('Available Currency\n>>', data[1].keys())
            desired_currency = input("Please provide the INR or other currency value\n>>>")
            print(f'{desired_currency}:{data[1][desired_currency]} | base:{base_value[1]} | date:{Date[1]}')

            convert = input('Do you want to convert the '+ desired_currency+ ' value to USD?\t  yes or no: ')
            if convert == 'yes':
                value = float(input("value\n>>>"))
                USD_value = value/float(data[1][desired_currency])
                print(f'The value is:\t ${USD_value}')
            else:
                print("\nThank you")
        else:
            print ("\nPlease give the correct data")
    
currency_converter_1()