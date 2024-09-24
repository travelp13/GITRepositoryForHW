# Task1
# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел. Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.
import random, os

PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'numbers.txt')

def gen_numbers(count: int):
    with open(PATH, 'w') as file:
        for _ in range(count):
            rdm = random.uniform(0, 100)
            file.write(f"{rdm}\n")

def main():
    gen_numbers(10000)

    try:
        with open(PATH, 'r') as file:
            numbers = file.readlines()
            numbers = [float(num.strip()) for num in numbers]
            print(f"Сума дорівнює: {sum(numbers)}")
    except FileNotFoundError:
        print(f"Файл '{PATH}' не знайдено.")

main()

# Task2
# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так, 
# щоб він зберігав базу посилань на диску і не «забув» при перезапуску. 
# За бажанням можете ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html), 
# який у даному випадку буде дуже зручним та спростить виконання завдання.
import shelve, os

PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'links.db')

def add_link(original_link, short_name, db):
    if short_name in db:
        print("Ця коротка назва вже використовується.")
    else:
        db[short_name] = original_link
        print(f"Посилання '{original_link}' було скорочене до '{short_name}'.")

def get_original_link(short_name, db):
    if short_name in db:
        return db[short_name]
    else:
        return "Коротка назва не знайдена."

def main():
    with shelve.open(PATH) as db:
        while True:
            print("\n1 - Додати скорочене посилання")
            print("2 - Отримати початкове посилання за скороченою назвою")
            print("3 - Вийти")

            choice = input("Виберіть номер меню: ")

            if choice == '1':
                link = input("Введіть початкове посилання: ")
                short_name = input("Введіть коротку назву: ")
                add_link(link, short_name, db)
            elif choice == '2':
                short_name = input("Введіть коротку назву: ")
                link = get_original_link(short_name, db)
                print(f"Початкове посилання: {link}")
            elif choice == '3':
                print("Вихід із програми.")
                break
            else:
                print("Невірний вибір")

main()

# Task3
# Створіть список товарів в інтернет-магазині. 
# Серіалізуйте його за допомогою pickle та збережіть у JSON.
import pickle, json, os

products = {
    "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
    "Одяг": ["Футболка", "Джинси", "Куртка"],
    "Книги": ["Роман", "Фентезі", "Наукова література"]}

PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'products')

with open(f'{PATH}.pkl', 'wb') as file:
    pickle.dump(products, file)

with open(f'{PATH}.pkl', 'rb') as file:
    open_products = pickle.load(file)

with open(f'{PATH}.json', 'w', encoding='utf-8') as file:
    json.dump(open_products, file, ensure_ascii=False, indent=4)

