# Task1
# Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином, 
# щоб у нього була основна частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс, 
# і модуль представлення, який відповідав би за взаємодію з користувачем. 
# При заміні останнього на інший, який взаємодіє з користувачем в інший спосіб, 
# програма має продовжувати коректно працювати.
from link_handler import LinkHandler
import os

PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'links.db')

def main():
    service = LinkHandler(PATH)
    
    while True:
        print("\n1 - Додати скорочене посилання")
        print("2 - Отримати початкове посилання за скороченою назвою")
        print("3 - Вийти")

        choice = input("Виберіть номер меню: ")

        if choice == '1':
            link = input("Введіть початкове посилання: ")
            short_name = input("Введіть коротку назву: ")
            success, message = service.add_link(link, short_name)
            print(message)
        elif choice == '2':
            short_name = input("Введіть коротку назву: ")
            success, result = service.get_original_link(short_name)
            if success:
                print(f"Початкове посилання: {result}")
            else:
                print(result)
        elif choice == '3':
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()

# Task3
# Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі імена.
from simple_number import is_simple

def main():
    while True:
        value = input("Введіть число для перевірки на простоту або q для виходу: ")

        if value == 'q':
            break

        try:
            number = int(value)
        except ValueError:
            print("Значення має бути цілим числом")
            continue
        
        if is_simple(number):
            print(f"{number} просте число.")
        else:
            print(f"{number} не є простим числом.")

if __name__ == "__main__":
    main()
