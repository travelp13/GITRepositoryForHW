# Task1
# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
def my_generator(lst: list):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_generator(my_list):
    print(i)

# Task2
# Виведіть із списку чисел список квадратів парних чисел. 
# Використовуйте 2 варіанти рішення: генератор та цикл
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_generator(lst: list):
    for i in lst:
        if i % 2 == 0:
            yield i**2

result_list = my_generator(my_list)
print(list(result_list))

# Цикл
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = []

for num in my_list:
    if num % 2 == 0:
        result_list.append(num**2)

print(result_list)


def even_squares(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num ** 2
