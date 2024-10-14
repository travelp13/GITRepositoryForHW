# Task1
# Створіть клас, який описує книгу. 
# Він повинен містити інформацію про автора, назву, рік видання та жанр. 
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.
class Book:
    def __init__(self, author:str, name:str, year:int, genre:str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
    def __str__(self):
        return (f'Autthor : {self.author}\nBook : {self.name}\nyear : {self.year}\ngenre : {self.genre}')
               
    def __repr__(self):
        return (f"author='{self.author}', name='{self.name}', year={self.year}, genre='{self.genre}'")


book1 = Book('Stephen King', 'Pet Sematary', 1983, 'Horror')
book2 = Book('Arthur Conan Doyle', 'The Memoirs of Sherlock Holmes', 1893, 'Detective fiction')
print (str(book1))
print (repr(book1))
print("***********************************")
print (str(book2))
print (repr(book2))

# Task2
# Створіть клас, який описує відгук до книги. 
# Додайте до класу книги поле – список відгуків. 
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.
class Review:
    def __init__(self, reviewer:str, text:str, rating:int):
        self.reviewer = reviewer
        self.text = text
        self.rating = rating

    def __str__(self):
        return (f"Reviewer : {self.reviewer}\nRating : {self.rating}/5\nReview : {self.text}\n")

class Book:
    def __init__(self, author:str, name:str, year:int, genre:str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews = []
    def __str__(self):
        all_reviews = "\n".join(str(review) for review in self.reviews)
        return (f'Autthor : {self.author}\nBook : {self.name}\nyear : {self.year}\ngenre : {self.genre}'
                f"Reviews:\n{'No reviews yet' if not self.reviews else all_reviews}")
    def __repr__(self):
        return (f"author='{self.author}', name='{self.name}', year={self.year}, genre='{self.genre}'")
    def add_review(self, review:Review):
        self.reviews.append(review)

book1 = Book('Stephen King', 'Pet Sematary', 1983, 'Horror')
book2 = Book('Arthur Conan Doyle', 'The Memoirs of Sherlock Holmes', 1893, 'Detective fiction')

review1 = Review("Ivan", "Super book.", 5)
review2 = Review("Olga", "Sometimes boring.", 4)

book1.add_review(review1)
book1.add_review(review2)


print ((book1))
print("***********************************")
print ((book2))

# Task4
# Створіть клас, який описує автомобіль. 
# Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу, 
# і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, manufacturer:str, model:str, year:int, price:float):
        self.manufacturer = manufacturer
        self.model = model      
        self.year = year        
        self.price = price      

    def __str__(self):
        return f"Manufacturer : {self.manufacturer}\nModel : {self.model}\nYear : {self.year}\nPrice : ${self.price}"

class CarDealer:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car {car} has been sold.")
        else:
            print(f"There is no such car {car}.")

    def __str__(self):
        all_cars = "\n".join(str(car) for car in self.cars)
        return f"Dealer : {self.name}\nCars:\n{'No cars' if not self.cars else all_cars}"

car1 = Car("Toyota", "Camry", 2020, 24000.99)
car2 = Car("Honda", "Civic", 2019, 22000)
car3 = Car("Volvo", "S90", 2021, 35000.99)

dealership = CarDealer("Best Cars")
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)

print(dealership)
print("***********************************")
dealership.sell_car(car2)
dealership.sell_car(car2)

