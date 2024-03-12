import math
import random
import datetime
def calculate_circle_area (radius):
    return math.pi * (radius**2)

def calculate_random_area():
    radius = random.randint(1,99999)
    return calculate_circle_area(radius)


def print_current_date():
    print(f"current time is {datetime.datetime.now().time()}")
    print(f"current date is {datetime.date.today()}")
