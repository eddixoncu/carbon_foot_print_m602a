import random
def try_basic_exception():
    number1 = int(input('Enter a number '))
    number2 = int(input('Enter another number '))
    return number1/number2

class GreatThanThresholdError (Exception):
    pass
def random_number_exception():
    threshold = 0.1
    rand = random.random()
    if  rand < threshold:
        raise GreatThanThresholdError

    number3 = float(input('enter a float number'))
    if  number3 < threshold:
        raise GreatThanThresholdError

class TooHotException(Exception):
    def __init__(self, temperature, message = 'Temperature is too high'):
        self.temperature = temperature
        self.message = message
        super().__init__(self.message)
def use_raise():
    temperature = int (input('enter a temperature value: '))
    if temperature >=100:
        raise TooHotException(100 , f'{temperature} degrees is too damn hot')

def main():
    print('Exceptions')
    try:
        ans = try_basic_exception()
        print('the expected result is ',ans)
        #random_number_exception()
        #use_raise()
    except ZeroDivisionError :
        print('Cannot divide by Zero')
    except ValueError :
        print('Incorrect number format')
    except GreatThanThresholdError:
        print('this is a GreatThanThresholdError')
    except TooHotException as the:
        print ('Too hot exception has occurred ', the)
    except Exception as gen_exception:
        print (type(gen_exception))
        print('Error: ',gen_exception)



if __name__ == "__main__":
    main()