#Task2
def is_palindrome(phrase):
    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    return cleaned_phrase == cleaned_phrase[::-1]

phrase = input("Введіть фразу: ")

if is_palindrome(phrase):
    print("Ця фраза є паліндромом.")
else:
    print("Ця фраза не є паліндромом.")

#Task3
def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    prev1 = 2
    prev2 = 1
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

n = int(input("Введіть кількість сходинок: "))
print(f"Кількість способів піднятися на сходинку {n}: {count_ways(n)}")

#Task4
def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)

a = int(input("Введіть початок проміжку (a): "))
b = int(input("Введіть кінець проміжку (b): "))
print(f"Сума натуральних чисел від {a} до {b}: {sum_range(a, b)}")

#Task 5
import math

def quadratic_equation(a, b, c):
    x1, x2 = None, None
    
    def calc_result(a, b, c):
        nonlocal x1, x2
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
        elif discriminant == 0:
            x1 = x2 = -b / (2*a)
        else:
            pass
    
    calc_result(a, b, c)
    
    return [x1, x2]

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

roots = quadratic_equation(a, b, c)
print(f"Корені рівняння: {roots}")
