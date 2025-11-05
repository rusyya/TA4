import math
from string import ascii_lowercase, ascii_uppercase
from random import choice

#Task 1.
def circle_areas_generator():
    for radius in range(10, 101):
        area = math.pi * radius ** 2
        yield area

circle_gen = circle_areas_generator()
for a in range(5):
    area = next(circle_gen)
    print(f"{area:.2f}")

#Task2
to_emails = ascii_lowercase + ascii_uppercase + "0123456789_"
def email_generator():
    while True:
        first_part = ''.join(choice(to_emails) for x in range(8))
        yield f"{first_part}@mail.ru"

email_gen = email_generator()
for y in range(7):
    print(next(email_gen))

#Task 3
def filter_string():
    numbers = list(map(int, input().split()))
    filtered_numbers = list(filter(lambda x: 10 <= x <= 99, numbers))
    print(*filtered_numbers)
filter_string()