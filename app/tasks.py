import math
from string import ascii_lowercase, ascii_uppercase
from random import choice

#Task 1.
def circle_areas_generator():
    for radius in range(10, 101):
        area = math.pi * radius ** 2
        yield area

#Task2
to_emails = ascii_lowercase + ascii_uppercase + "0123456789_"
def email_generator():
    while True:
        first_part = ''.join(choice(to_emails) for x in range(8))
        yield f"{first_part}@mail.ru"

#Task 3
def filter_string(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    return list(filter(lambda x: 10 <= abs(x) <= 99, numbers))
