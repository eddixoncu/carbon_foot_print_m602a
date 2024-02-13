Temperature = 28


def thermostat_regulator(temperature, low_temp=20, high_temp=27):
    # assert high_temp > low_temp, "High temp must be lower than low temp"
    state = ''
    if temperature < low_temp:
        state = 'Turn on heater'
    elif temperature > high_temp:
        state = 'Turn on cooler'
    # elif low_temp <= temperature <= high_temp:
    else:
        state = 'Do nothing'

    # print(state)
    return state


result = thermostat_regulator(Temperature, 1500, 2700)

print('result is ', result)
