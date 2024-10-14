# Task1
# Створіть клас Editor, який містить методи view_document та edit_document. 
# Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. 
# Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. 
# Викликайте методи перегляду та редагування документів.
class Editor:
    def view_document(self) -> None:
        print ("Перегляд документа доступний")

    def edit_document(self) -> None:
        print("Редагування документів недоступне для безкоштовної версії!`")

class ProEditor(Editor):   
    def edit_document(self) -> None:
        print("Можеш редагувати документ!")

def main():
    license = input("Введи ліцензійний ключ: ")
    
    if license == '1234':
        editor = ProEditor()
    else:
        editor = Editor()
    
    editor.view_document()
    editor.edit_document()

main()

# Task2
# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. 
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. 
# Викличте метод натискання на кнопку.
class GraphicObject:
    def create(self) -> None:
        print("Створення графічного об'єкта")

class Rectangle(GraphicObject):
    def __init__(self, width:int, height:int) -> None:
        self.width = width
        self.height = height
    
    def create(self) -> None:
        super().create()
        print(f"Прямокутник: ширина {self.width}, висота {self.height}")

class ObjectOnClick:
    def on_click(self) -> None:
        print("Натискання миші")

class Button(Rectangle, ObjectOnClick):
    def __init__(self, width:int, height:int, btn_name:str) -> None:
        super().__init__(width, height)
        self.btn_name = btn_name
    
    def create(self) -> None:
        super().create()
        print(f"Кнопка: {self.btn_name}")

    def on_click(self) -> None:
        print(f"Кнопка {self.btn_name} натиснута")

button = Button(10, 20, "Enter")

button.create()
button.on_click()

# Task3
# Створіть ієрархію класів із використанням множинного успадкування. 
# Виведіть на екран порядок вирішення методів для кожного класу. 
# Поясніть, чому лінеаризація даних класів виглядає саме так.
class Main:
    def print_something(self) -> None:
        print("Клас Main")

class Branch(Main):
    def print_something(self) -> None:
        print("Клас Branch від Main")

class Branch2(Main):
    def print_something(self) -> None:
        print("Клас Branch2 від Main")

class Branch3(Branch2):
    def print_something(self) -> None:
        print("Клас Branch3 від Branch2")

class Branch4(Branch,Branch3):
    def print_something(self) -> None:
        print("Клас Branch4 від Branch та Branch3")

print("\nBranch4 mro:")
print(Branch4.mro())

print("\nBranch3 mro:")
print(Branch3.mro())

print("\nBranch2 mro:")
print(Branch2.mro())

print("\nBranch1 mro:")
print(Branch.mro())

print("\nMain mro:")
print(Main.mro())

branch4 = Branch4()
branch4.print_something()

# Task5
# Використовуючи код example_10, створіть статичний метод класу  ( для створення використовуйте декоратор @staticmethod ), 
# метод має приймати вік людини та перевіряти чи досягла вона повноліття, метод має повертати True або False
class Human:
    def __init__(self, surname:str, name:str, age:int) -> None:
        self.surname = surname
        self.name = name
        self.age = age

    def print_info(self) -> None:
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult(age:int) -> bool:
        return age >= 18

somebody = Human("Olga", "Unknown", 33)

somebody.print_info()
if somebody.is_adult(somebody.age):
    print("The person has reached adulthood.")
else:
    print("The person has not yet reached adulthood.")

# Task6
# Використовуючи код example_10, створіть класовий метод ( для створення використовуйте декоратор @classmethod ). 
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття, для вирішення
# задачі використовуйте статичний метод створенний в завданні 5
class Human:
    adualts = 0
    def __init__(self, surname:str, name:str, age:int) -> None:
        self.surname = surname
        self.name = name
        self.age = age
        if self.is_adult(age):
            Human.adualts += 1

    def print_info(self) -> None:
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult(age:int) -> bool:
        return age >= 18
    
    @classmethod
    def count_adults(cls) -> int:
        return cls.adualts

somebody1 = Human("Olga", "Unknown", 33)
somebody2 = Human("Ivan", "Unknown", 16)
somebody3 = Human("Alex", "Unknown", 45)

somebody1.print_info()
somebody2.print_info()
somebody3.print_info()

print(f"Кількість людей, які досягли повноліття: {Human.count_adults()}")

# Task7
# Створіть ієрархію класів транспортних засобів. 
# У загальному класі опишіть загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм. 
# Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.
class Transport:
    def __init__(self, brand:str, model:str, year:int, price:float) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"Бренд: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}, Ціна: {self.price}"

class Car(Transport):
    def __init__(self, brand:str, model:str, year:int, price:float, body_style:str, fuel_type:str) -> None:
        super().__init__(brand, model, year, price)
        self.body_style = body_style
        self.fuel_type = fuel_type
    
    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}, Тип кузова: {self.body_style}, Тип палива: {self.fuel_type}"

class Aircraft(Transport):
    def __init__(self, brand:str, model:str, year:int, price:float, seats:int, wingspan:int) -> None:
        super().__init__(brand, model, year, price)
        self.seats = seats
        self.wingspan = wingspan
    
    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}, Кількість місць: {self.seats}, Розмах крила: {self.wingspan} м."
    
car = Car("Honda", "Accord", 2020, 30000, "Седан", "Бензин")
aircarft = Aircraft("Boeing", "737", 2018, 45000000, 195, 66)

print(car)
print(aircarft)
