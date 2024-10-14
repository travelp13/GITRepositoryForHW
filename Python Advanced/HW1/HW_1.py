# Task2
# Напишіть декоратор, який буде заміряти час виконання для наданої функції.
import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper

@execution_time
def some_function():
    print("Start")
    time.sleep(2)
    print("End")

some_function()

# Task3
# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, 
# використовуючи для цього три наведені в тексті заняття функції — без кешу, з кешем довільної довжини, 
# з кешем з модулю functools з максимальною кількістю 10 елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.

# Task4 
# За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів. 
from functools import lru_cache

@execution_time
def fibonacci(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

cache = {}

@execution_time
def fibonacci_custom_cache(n):
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n)
    cache[n] = result
    return result

@execution_time
@lru_cache(maxsize=10)
def fibonacci_lru_10(n):
    result = fibonacci(n)
    return result

@execution_time
@lru_cache(maxsize=16)
def fibonacci_lru_16(n):
    result = fibonacci(n)
    return result

print(fibonacci(25))
print(fibonacci_custom_cache(25))
print(fibonacci_lru_10(25))
print(fibonacci_lru_16(25))

# Task5
# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def power(func):
    def wrapper(numbers):
        result = []
        for n in numbers:
            if n % 2 != 0:
                result.append(n**2)
        return result
    return wrapper

@power
def get_numbers(numbers):
    return numbers

result = get_numbers(list_numbers)
print(result)

# Task6
# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.
def fibonacci_filter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for number in result:
            if number % 2 == 0:
                yield number
    return wrapper

@fibonacci_filter
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 25
result = fibonacci_generator(n)

print(list(result))

# Task7
# Створіть звичайну функцію множення двох чисел. Створіть карированну функцію множення двох чисел. 
# Частково застосуйте її до одного аргументу, до двох аргументiв.
def multiply(a, b):
    return a * b

print(multiply(5, 10))

def cur_multiply(a):
    def inner(b):
        return a * b
    return inner

multiply_5 = cur_multiply(5)
result = multiply_5(10)

print(result)

result = cur_multiply(7)(3)
print(result)