import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from random import choice
from app.tasks import circle_areas_generator, email_generator, filter_string, to_emails
import random

#Task 1
def area_func(radius: int) -> float:
    """Вспомогательная для parallel_circle_areas"""
    return math.pi * radius ** 2

def parallel_circle_areas():
    radii = range(10, 101)
    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(area_func, radii))
    exec_time = time.perf_counter() - start
    return exec_time

#Task 2
def make_email(_):
    """Вспомогательная для parallel_email_generator"""
    return ''.join(choice(to_emails) for _ in range(8)) + "@mail.ru"

def parallel_email_generator(n=100000):
    start = time.perf_counter()
    with ThreadPoolExecutor() as ex:
        emails = list(ex.map(make_email, range(n)))
    exec_time = time.perf_counter() - start
    return exec_time

#Task 3
def check_number(n: int) -> bool:
    """Вспомогательная для parallel_filter_string"""
    return 10 <= abs(n) <= 99

def parallel_filter_string(numbers_str):
    nums = list(map(int, numbers_str.split()))
    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        mask = list(ex.map(check_number, nums))
    filtered = [n for n, ok in zip(nums, mask) if ok]
    exec_time = time.perf_counter() - start
    return exec_time


#Сравнение производительности
def main():
    start = time.perf_counter()
    list(circle_areas_generator())
    exec_time_base = time.perf_counter() - start
    exec_time_parallel = float(parallel_circle_areas())
    print(f"Площадь круга - обычный: {exec_time_base:.6f}, параллельный: {exec_time_parallel:.6f}, быстрее в {exec_time_base/exec_time_parallel:.6f}")

    gen = email_generator()
    start = time.perf_counter()
    [next(gen) for _ in range(1000)]
    exec_time_base = time.perf_counter() - start
    exec_time_parallel = float(parallel_email_generator(1000))
    print(f"Email - обычный: {exec_time_base:.6f}, параллельный: {exec_time_parallel:.6f}, быстрее в {exec_time_base / exec_time_parallel:.6f}")

    data = ' '.join(str(random.randint(-500, 500)) for _ in range(100000))
    start = time.perf_counter()
    filter_string(data)
    exec_time_base = time.perf_counter() - start
    exec_time_parallel = float(parallel_filter_string(data))
    print(f"Email - обычный: {exec_time_base:.6f}, параллельный: {exec_time_parallel:.6f}, быстрее в {exec_time_base / exec_time_parallel:.6f}")


if __name__ == "__main__":
    main()
