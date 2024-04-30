currency_rates = {
    "USD2EUR", 0.9376,
    "EUR2USD", 1.0666,
    "EUR2GBP", 0.8608,
    "GBP2EUR", 1.1616,
    "COP2EUR", 0.000239,
    "EUR2COP", 4179.4313
}

def perform_conversion (exchange_code):
    from_currency = exchange_code.split('2')[0]
    to_currency = exchange_code.split('2')[1]
    amount = int(input(f'How many {from_currency} do you wish convert? '))
    new_amount = amount * exchange_code[exchange_code]
    print(f'{from_currency} {amount} are {to_currency} {new_amount}')
def main():
    print('Currency')
    idx = 1


if __name__ == "__main__":
    main()