# Task1
# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
def my_generator(lst: list):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_generator(my_list):
    print(i)

# # Task2
# # Виведіть із списку чисел список квадратів парних чисел. 
# # Використовуйте 2 варіанти рішення: генератор та цикл
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

# Task3
# Напишіть функцію-генератор для отримання n перших простих чисел.
def get_simple_num():
    numbers = list(range(2,10001))
    simple_numbers = []

    for number in numbers:
        if number in (2, 3, 5, 7):
            simple_numbers.append(number)
        elif number > 10 and number%10 in (1, 3, 7, 9):
            if number%3 != 0 and number%7 !=0 and number%number**0.5 !=0:
                simple_numbers.append(number)

    notsimple_numbers = []
    rng = round(len(simple_numbers)/2)+1

    for number in simple_numbers:
        for not_simple in simple_numbers[0:rng]:
            if number%not_simple == 0 and number != not_simple:
                notsimple_numbers.append(number)

    for number in simple_numbers:
        if number in notsimple_numbers:
            simple_numbers.remove(number)
    
    return simple_numbers

simple_numbers = get_simple_num()

def my_generator(n):
    number = 0
    count = 0
    while count < n:
        if number in simple_numbers:
            yield number
            count += 1
        number += 1

n = 20
for simple_number in my_generator(n):
    print(simple_number)
