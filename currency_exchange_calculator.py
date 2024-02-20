import requests


def get_recent_exchange_rate():
    api_version = '1'
    date = 'latest'
    currency_code_from = 'usd'
    currency_code_to = 'eur'
    endpoint = f'currencies/{currency_code_from}/{currency_code_to}.json'
    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{api_version}/{date}/{endpoint}'

    #https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/jpy.json
    #https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/USD/EUR.json

    print("Getting data from ", url)
    response = requests.get(url)
    data = response.json()
    print("the obtained data is ", data)

    if 'date' in data and 'eur' in data:
        return data['eur']
    else:
        return None


print('currency_exchange_calculator.py')
rate = get_recent_exchange_rate()
print(f'Rate is {rate}')
