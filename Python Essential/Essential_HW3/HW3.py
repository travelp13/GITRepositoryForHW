# Task1
# Створіть клас, який описує автомобіль. 
# Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
class Car:
    def __init__(self, brand: str, model: str, year: int, color: str, body_type: str, price: float, vin: str, owner_name: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.body_type = body_type
        self.price = price
        self.__vin = None
        self.__owner_name = None
        self.set_vin(vin)
        self.set_owner_name(owner_name)
    
    def set_vin(self, vin: str):
        if len(vin) > 10:
            self.__vin = vin
        else:
            print("VIN номер не може бути менше 10 символів")
    
    def get_vin(self) -> str:
        return self.__vin
    
    def set_owner_name(self, owner_name: str):
        if len(owner_name) > 2:
            self.__owner_name = owner_name
        else:
            print("Ім'я клієнта не може бути менше 2 символів")

    def get_owner_name(self) -> str:
        return self.__owner_name
    
car1 = Car("Honda", "Accord", 2020, "Black", "Sedan", 30999, "KQ159956ZXD8", "Yulia")
print (f"VIN: {car1.get_vin()}")
print (f"Owner: {car1.get_owner_name()}")

# Task2
# Створіть 2 класи мови, наприклад, англійська та іспанська. 
# В обох класів має бути метод greeting(). Обидва створюють різні привітання. 
# Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).
class English:
    def greeting(self):
        print("Hello my friend!")

class Spanish:
    def greeting(self):
        print("¡Hola mi amigo!")

def hello_friend(lang1: English, lang2: Spanish):
    lang1.greeting()
    lang2.greeting()

english = English()
spanish = Spanish()
hello_friend(english, spanish)

# Task3
# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості.
# Ознайомтеся з декоратором property у Python.
# Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.
class Temperature:
    def __init__(self,):
        self.__celsius = float(0)

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, degrees: float):
        self.__celsius = degrees

    @property
    def fahrenheit(self):
        return round((self.__celsius * 1.8 + 32), 2)

    @fahrenheit.setter
    def fahrenheit(self, degrees):
        self.__celsius = round((degrees - 32) / 1.8, 2)

temperature = Temperature()
temperature.fahrenheit = 100.4
print(f"Температура в Цельсіях: {temperature.celsius}")
print(f"Температура в Фаренгейтах: {temperature.fahrenheit}") 

temperature.celsius = 25.6
print(f"Температура в Цельсіях: {temperature.celsius}")
print(f"Температура в Фаренгейтах: {temperature.fahrenheit}") 

# Task4
# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно 
# "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.
class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")

class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")

Base.method()
Child.method()

# Task5
# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. 
# Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами. 
# В результаті повинно з’явитися зображення. Перегляньте їх.
from PIL import Image, ImageDraw

class Shape:    
    def __init__(self, width: int, back_color: tuple):
        self.back_color = back_color
        self.width = width
        self.im = Image.new('RGB', (width, width), back_color)
        self.draw = ImageDraw.Draw(self.im)

    def erase(self):
        self.im = Image.new('RGB', (self.width, self.width), self.back_color)
        self.draw = ImageDraw.Draw(self.im)

    def save(self, path: str):
        print("Background was created")
        return self.im.save(path, quality=95)
        
class Paraboloid(Shape):
    def __init__(self):
        self.__BLACK = (0, 0, 0)
        self.__width = 1000
        super().__init__(self.__width, self.__BLACK)        
        
    def draw_paraboloid(self):
        color_r = 230
        color_g = 3
        color_b = 150
        center = self.width/2
        x_start_left = center
        x_start_right = center
        y_start = self.width-100
        for step in range(0, 100):
            x = step
            y = x * x + x
            x += step * 10
            y = self.width - 100 - y
            if y < 100:
                break
            self.draw.line([(x_start_left, y_start), (center - x, y)], (color_r - step * 3, color_g + step * 3, color_b + step * 3))
            self.draw.line([(x_start_right, y_start), (center + x, y)], (color_r - step * 3, color_g + step * 3, color_b + step * 3))
            if step > 0:
                self.draw.ellipse([(center - x, y - step * 2), (center + x, y + step * 2)], outline = (color_r - step * 3, color_g + step * 3, color_b + step * 3))

            x_start_left = center-x
            x_start_right = center+x
            y_start = y

        self.im.show()

    def save(self, path: str):
        super().save(path)
        
class Cone(Shape):
    def __init__(self):
        self.__BLACK = (0, 0, 0)
        self.__width = 500
        super().__init__(self.__width, self.__BLACK)

    def draw_cone(self):
        color_r = 230
        color_g = 3
        color_b = 150
        center = self.width/2
        x_start_left = center
        x_start_right = center
        y_start = self.width-100
        for step in range(0, 100):
            x = step
            y = x
            y = self.width - 100 - y
            self.draw.line([(x_start_left, y_start), (center - x, y)], (color_r - step, color_g + step, color_b + step))
            self.draw.line([(x_start_right, y_start), (center + x, y)], (color_r - step, color_g + step, color_b + step))
            x_start_left = center-x
            x_start_right = center+x
            y_start = y

        self.draw.ellipse([(x_start_left, y_start - 20), (x_start_right, y_start + 20)], outline = (color_r - 200 * 3, color_g + 200 * 3, color_b + 200 * 3))
        self.im.show()

    def save(self, path: str):
        super().save(path)

paraboloid = Paraboloid()
paraboloid.draw_paraboloid()
paraboloid.save("d:\ITVDN\paraboloid.png")


cone = Cone()
cone.draw_cone()
cone.save("d:\ITVDN\cone.png")