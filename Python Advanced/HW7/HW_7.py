# Task1 
# Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень вихідного масиву. 
# Додайте анотацію типів для вхідних і вислідних значень функції. 
from typing import List

def to_str (numbers: List[int]) -> List[str]:
    return [str(number) for number in numbers]

ls = to_str((1,2,3))
print(ls)


# Task2
# Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
# Клас Directory має мати такі поля:
# ·        назва (name типу str);
# ·        батьківська тека (root типу Directory);
# ·        список файлів (список типу files, який складається з екземплярів File);
# ·        список підтек (список типу sub_directories, який складається з екземплярів Directory). 
# Клас Directory має мати такі поля:
# ·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root для приймального екземпляра);
# ·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root. Метод також видаляє теку зі списку sub_directories);
# ·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас File нижче);
# ·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory. Метод видаляє файл зі списку files). 

# Клас File має мати такі поля:
# ·        назва (name типу str);
# ·        тека (Directory типу Directory). 

from typing import List, Optional

class File:
    def __init__(self, name: str, directory: Optional["Directory"] = None):
        self.name: str = name
        self.directory: Optional["Directory"] = directory


class Directory:
    def __init__(self, name: str, root: Optional["Directory"] = None):
        self.name: str = name
        self.root: Optional["Directory"] = root
        self.files: List[File] = []
        self.sub_directories: List["Directory"] = []

    def add_sub_directory(self, sub_directory: "Directory") -> None:
        sub_directory.root = self
        self.sub_directories.append(sub_directory)

    def remove_sub_directory(self, sub_directory: "Directory") -> None:
        if sub_directory in self.sub_directories:
            sub_directory.root = None
            self.sub_directories.remove(sub_directory)

    def add_file(self, file: File) -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        if file in self.files:
            file.directory = None
            self.files.remove(file)

root_directory = Directory(name="root")

sub_directory1 = Directory(name="sub1")
root_directory.add_sub_directory(sub_directory1)

sub_directory2 = Directory(name="sub2")
root_directory.add_sub_directory(sub_directory2)

print([sub_dir.name for sub_dir in root_directory.sub_directories])

root_directory.remove_sub_directory(sub_directory1)

print([sub_dir.name for sub_dir in root_directory.sub_directories])

file1 = File(name="file1.txt")
sub_directory2.add_file(file1)

print([file.name for file in sub_directory2.files])

sub_directory2.remove_file(file1)

print([file.name for file in sub_directory2.files])

# Task3
# Використовуючи модуль sqlite3 та модуль smtplib, реалізуйте реальне додавання користувачів до бази. 
# Мають бути реалізовані такі функції та класи:
# ·  клас користувача, що містить у собі такі методи: get_full_name (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»), 
#      get_short_name (формату ПІБ: «Петров І. С.»), get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date); 
#      метод __str__ (повертає ПІБ та дату народження);
# ·  функція реєстрації нового користувача (приймаємо екземпляр нового користувача та відправляємо email на пошту користувача з листом подяки).
# ·  функція відправлення email з листом подяки.
# ·  функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.

# Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти. 
# Під час штатного запуску програми вона має відправляти повідомлення на вашу реальну поштову скриньку (необхідно налаштувати SMTP, 
# використовуючи доступи від провайдера вашого email-сервісу).

# Приклад налаштування SMTP для сервісу Gmail: https://support.google.com/mail/answer/7126229?hl=ru


import sqlite3, os
import smtplib
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional


class User:
    def __init__(self, first_name: str, last_name: str, middle_name: str, email: str, birthday: date):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.email = email
        self.birthday = birthday

    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self) -> int:
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def __str__(self) -> str:
        return f"{self.get_full_name()} ({self.birthday})"

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"my.db") 

def create_db():
    with sqlite3.connect(file_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            middle_name TEXT,
                            email TEXT UNIQUE NOT NULL,
                            birthday TEXT NOT NULL
                          )''')
        conn.commit()

def register_user(user: User):
    with sqlite3.connect(file_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (first_name, last_name, middle_name, email, birthday)
                          VALUES (?, ?, ?, ?, ?)''', 
                          (user.first_name, user.last_name, user.middle_name, user.email, user.birthday.isoformat()))
        conn.commit()
    send_email(user)


def send_email(user: User):
    sender_email = "pavel.t.mail@gmail.com"
    receiver_email = user.email
    password = ''  # замініть на 16-значний пароль для додатку

    message = MIMEMultipart("alternative")
    message["Subject"] = "Дякуємо за реєстрацію!"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"Шановний {user.get_full_name()},\n\nДякуємо за реєстрацію!"
    html = f"""\
    <html>
      <body>
        <p>Шановний {user.get_full_name()},<br>
           Дякуємо за реєстрацію!
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Лист подяки надіслано на {receiver_email}")


def find_users(name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None) -> List[User]:
    with sqlite3.connect(file_name) as conn:
        cursor = conn.cursor()
        query = "SELECT first_name, last_name, middle_name, email, birthday FROM users WHERE 1=1"
        params = []

        if name:
            query += " AND first_name = ?"
            params.append(name)
        if last_name:
            query += " AND last_name = ?"
            params.append(last_name)
        if email:
            query += " AND email = ?"
            params.append(email)

        cursor.execute(query, params)
        rows = cursor.fetchall()

        users = [User(first_name=row[0], last_name=row[1], middle_name=row[2], email=row[3], birthday=date.fromisoformat(row[4])) for row in rows]
        return users

if __name__ == "__main__":
    create_db()

    new_user = User("Ігор", "Петров", "Сергійович", "travel.p84@gmail.com", date(1984, 5, 4))

    register_user(new_user)

    found_users = find_users(last_name="Петров")
    for user in found_users:
        print(user)
