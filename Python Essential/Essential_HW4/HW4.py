# Task2
# Напишіть програму-калькулятор, яка підтримує такі операції: 
# додавання, віднімання, множення, ділення та піднесення до ступеня. 
# Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних, 
# діленні на нуль та зведенні нуля в негативний степінь.
class Calculator:
    def adding (self, value1: float, value2: float):
        return (value1+value2)

    def subtraction (self, value1: float, value2: float):
        return (value1-value2)

    def multiply(self, value1: float, value2: float):
        return (value1*value2)

    def division(self, value1: float, value2: float):
        try:
            return (value1/value2)
        except ZeroDivisionError:
            return ("На нуль ділити не можна!")

    def power(self, value1: float, value2: float):
        try:
            return (value1**value2)
        except ZeroDivisionError:
            return ("Не можна зводити нуль у негативний ступінь!")

def main():
    def print_result(result: float):
        print(f"Результат: {str(result)}\n")

    menu = 'Оберіть меню:, 1-Додавання, 2-Віднімання, 3-Множення, 4-Поділ, 5-Ступінь числа, 0-Вихід, '
    calc = Calculator()
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        user_choise = input().strip()

        if user_choise == "0":
            break

        if user_choise not in ("1", "2", "3", "4", "5"):
            print("Немає такого пункту меню, виберіть ще раз:")
            continue
        else:
            try:
                value1 = float(input("Введи перше число: "))
                value2 = float(input("Введи друге число: "))
            except ValueError:
                print("Значення має бути числом!")
                continue

        try:
            match int(user_choise):
                case 1 : print_result(calc.adding(value1, value2))
                case 2 : print_result(calc.subtraction(value1, value2))
                case 3 : print_result(calc.multiply(value1, value2))
                case 4 : print_result(calc.division(value1, value2))
                case 5 : print_result(calc.power(value1, value2))
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

main()

# Task3
# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи. 
# Конструктор має генерувати виняток, якщо вказано неправильні дані. 
# Введіть список працівників із клавіатури. 
# Виведіть усіх співробітників, які були прийняті після цього року.
import datetime

class Employee:  
    def __init__(self, first_name: str, last_name: str, unit: str, start_work_year: int):
        self.first_name = str()
        self.last_name = str()
        self.unit = str()
        self.start_work_year = int()
        
        YEAR_OF_COMPANY_FOUNDATION = int(2013)
        current_year = datetime.datetime.now().year

        try:
            if len(first_name.strip()) < 1 or len(last_name.strip()) < 1:
                raise ValueError("Ім'я та прізвище мають бути більше 1 символу!")
            if not unit.strip():
                raise ValueError("Відділ не може бути порожнім!")
            if start_work_year < YEAR_OF_COMPANY_FOUNDATION or start_work_year > current_year:
                raise ValueError(f"Рік має бути в проміжку {YEAR_OF_COMPANY_FOUNDATION} та {current_year}!")
            
            self.first_name = first_name
            self.last_name = last_name
            self.unit = unit
            self.start_work_year = start_work_year
        except Exception as e:
            print(f"{str(e)}")

    def __str__(self) -> str:
        return f"Ім'я:{self.first_name}, прізвище: {self.last_name}, відділ: {self.unit}, рік початку роботи: {self.start_work_year}"

def main():
    employees = []
    menu = 'Оберіть меню:, 1-Додати співробітника, 2-Показати співробітників, 0-Вихід, '
           
    while True:
        print(("\n  ").join(menu.split(", ")))
        user_choise = input().strip()

        if user_choise == "0":
            break
        elif user_choise == "1":
            first_name = input("Введіть ім'я співробітника: ").strip()
            last_name = input("Введіть прізвище співробітника: ").strip()
            unit = input("Введіть відділ співробітника: ").strip()
            try:
                start_work_year = int(input("Введіть рік початку роботи співробітника: ").strip())
            except ValueError:
                print(f"Рік має бути числом!")
                continue       

            employee = Employee(first_name, last_name, unit, start_work_year)

            if employee.first_name:
                print(f"Співробітника додано. {employee}")
                employees.append(employee)
        elif user_choise == "2":
            try:
                user_year = int(input("Введіть рік початку роботи: ").strip())
            except ValueError:
                print("Рік має бути числом!")
                continue
            for employee in employees:
                if employee.start_work_year > user_year:
                    print(employee)
        else:
            print("Немає такого пункту меню, виберіть ще раз:")
            
main()

# Task4 
# Опишіть свій клас винятку. 
# Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення, 
# і перехопіть цей виняток під час виклику функції.
class MyError(Exception):
    def __init__(self, error):
        super().__init__(error)

def check_error(value):
    if value == "123":
        raise MyError("помилка")
    
def main():
    try:
        value = input("Введіть значення: ")
        check_error(value)
    except MyError as e:
        print(f"{e}")

main()

# Task5 
# Створіть програму спортивного комплексу, у якій передбачене меню: 
# 1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 
# 4 - вартість тренування. Дані зберігати у словниках. 
# Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню. 
# Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
class CoachNotExist(Exception):
    def __init__(self, surname):
        super().__init__(f"Тренера з таким прізвищем '{surname}' не знайдено")

sports = {
    1: "Футбол",
    2: "Баскетбол",
    3: "Хокей",
    4: "Бокс"
}

coaches = {
    "Шевченко": "Футбол",
    "Лінь": "Баскетбол",
    "Гриценко": "Хокей",
    "Кличко": "Бокс"
}

schedules = {
    "Футбол": "Понеділок, Середа, П'ятниця: 17:00-20:00",
    "Баскетбол": "Вівторок, Четвер: 18:00-21:00",
    "Хокей": "Середа, П'ятниця: 19:00-21:30",
    "Бокс": "Понеділок, Четвер: 18:30-20:30"
}

prices = {
    "Футбол": "200 грн",
    "Баскетбол": "50 грн",
    "Хокей": "100 грн",
    "Бокс": "150 грн"
}

def find_coach_by_surname(surname):
    try:
        if surname not in coaches:
            raise CoachNotExist(surname)
        return f"Тренер {surname} веде {coaches[surname]}"
    except CoachNotExist as e:
        return str(e)
    
def main():
    menu = 'Оберіть меню:, 1-Перелік видів спорту, 2-Команда тренерів, 3-Розклад тренувань, 4-Вартість тренування, 5-Пошук тренера за прізвищем, 0-Вихід, '
    while True:
        print(("\n  ").join(menu.split(", ")))
        user_choise = input().strip()

        if user_choise == "0":
            break
        elif user_choise == '1':
            for sport in sports.values():
                print(f"- {sport}")
        elif user_choise == '2':
            for surname, sport in coaches.items():
                print(f"{surname}: {sport}")
        elif user_choise == '3':
            for sport, time in schedules.items():
                print(f"{sport}: {time}")
        elif user_choise == '4':
            for sport, price in prices.items():
                print(f"{sport}: {price}")
        elif user_choise == '5':
            surname = input("Введіть прізвище тренера для пошуку: ")
            result = find_coach_by_surname(surname)
            print(result)
        else:
            print("Немає такого пункту меню, виберіть ще раз:")

main()