# Task2
# Створити клас Contact з полями surname, name, age, mob_phone, email. 
# Додати методи get_contact, sent_message. 
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. 
# Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__. 
# Роздрукувати інформацію на екрані.
class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Контакт: {self.surname} {self.name}, Вік: {self.age}, Телефон: {self.mob_phone}, Email: {self.email}"

    def send_message(self, message):
        return f"Надіслано повідомлення '{message}' на телефон {self.mob_phone}"

class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"Контакт: {self.surname} {self.name}, Вік: {self.age}, Робота: {self.job}, Телефон: {self.mob_phone}"

contact = Contact("Шевченко", "Ольга", 30, "+380501234567", "olga@gmail.com")
update_contact = UpdateContact("Старченко", "Петро", 35, "+380671234567", "petro@gmai.com", "Програміст")

print(contact.get_contact())
print(contact.send_message("Привіт"))

print(update_contact.get_message())

print(contact.__dict__)
print(update_contact.__dict__)

print(Contact.__base__)
print(UpdateContact.__bases__)

# Task3
# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). 
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

# hasattr - Перевіряє, чи має об'єкт певний атрибут. Якщо атрибут існує — повертає True, інакше — False.
print("hasattr:")
print(hasattr(contact, "job"))
print(hasattr(update_contact, "job"))

# getattr - Отримує значення атрибуту. Якщо атрибут не існує, можна передати значення за замовчуванням
print("getattr:")
print(getattr(contact, "job", "default"))
print(getattr(update_contact, "job", "default"))

# setattr - Встановлює нове значення для атрибуту. Якщо атрибут не існує, він буде створений.
print("setattr:")
print(setattr(contact, "job", "new_value"))
print(setattr(update_contact, "job", "new_value"))
print(getattr(contact, "job", "default"))
print(getattr(update_contact, "job", "default"))

# delattr - Видаляє атрибут з об'єкта. Якщо атрибут не існує, виникає помилка AttributeError.
print("delattr:")
try:
    print(delattr(contact, "phone"))
except Exception as e:
    print (e)
try:
    print(delattr(update_contact, "phone"))
except Exception as e:
    print (e)

print(getattr(contact, "job", "default"))
print(getattr(update_contact, "job", "default"))

# Task4
# Використовуючи код з завдання 2, створити 2 екземпляри обох класів. 
# Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) 
# та issubclass() – для перевірки і визначення класу-нащадка.

# isinstance(obj, class): Перевіряє, чи є об'єкт obj екземпляром класу class або його нащадка.
print (isinstance (update_contact, Contact))
print (isinstance (contact, UpdateContact))

# issubclass(subclass, superclass): Перевіряє, чи є клас subclass нащадком класу superclass
print (issubclass (UpdateContact, Contact))
print (issubclass (Contact, UpdateContact))

# Task5
# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах. 
# Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.
print(Contact.__dict__)
print(UpdateContact.__dict__)
print(contact.__dict__)
print(update_contact.__dict__)

delattr(contact, "job")
delattr(update_contact, "job")

print(Contact.__dict__)
print(UpdateContact.__dict__)
print(contact.__dict__)
print(update_contact.__dict__)

# Task6
# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.
for method in dir(Contact):
    print(method)

for method in dir(UpdateContact):
    print(method)