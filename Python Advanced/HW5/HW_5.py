# Task1
# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread, 
# і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на ThreadPoolExecutor. 
# Як приклади використовуйте останні значення, від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def run_threads(numbers: list):
    threads = []
    results = []

    def worker(n):
        results.append(factorial(n))

    start_time = time.time()
    for number in numbers:
        thread = threading.Thread(target=worker, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return results, end_time - start_time

def run_thread_pool(numbers: list):
    results = []

    def worker(n):
        return factorial(n)

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(worker, numbers))

    end_time = time.time()
    return results, end_time - start_time

min_n = 0     
max_n = 20 
numbers = list(range(min_n, max_n + 1))

thread_results, thread_time = run_threads(numbers)
print("Thread results:", thread_results)
print("Threads time:", thread_time)


pool_results, pool_time = run_thread_pool(numbers)
print("ThreadPoolExecutor results:", pool_results)
print("ThreadPoolExecutor time:", pool_time)

#Task 2
# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!». 
# Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. 
# Якщо файл є, то відкриває його і шукає рядок «Wow!». За наявності цього рядка закриває файл і генерує подію, 
# а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу. 
# Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. 
# Створіть файл руками та перевірте виконання програми.
import os
import time
import threading
from colorama import Fore, init

init(autoreset=True)

event = threading.Event()

def check_file(filename):
    while True:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                print(Fore.YELLOW + f"Знайдено файл {filename}")
                for row in f:
                    if 'Wow!' in row:
                        print(Fore.GREEN +"Знайдено рядок Wow!")
                        event.set()
                        return
            print(Fore.RED + "Wow! не знайдено")
            time.sleep(5)
        else:
            print(Fore.RED + f"Файл {filename} не знайдено")
            time.sleep(5)

def delete_file(filename):
    event.wait()
    if os.path.exists(filename):
        os.remove(filename)
        print(Fore.BLUE + f"Файл {filename} видалено")
    else:
        print(Fore.RED + f"Файл {filename} не знайдено")


def main():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test.txt") 

    checking_thread = threading.Thread(target=check_file, args=(filename,))
    deleting_thread = threading.Thread(target=delete_file, args=(filename,))

    checking_thread.start()
    deleting_thread.start()

    checking_thread.join()
    deleting_thread.join()

main()