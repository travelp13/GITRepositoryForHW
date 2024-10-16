# Task1
# Створіть прості словники та конвертуйте їх у JSON. 
# Збережіть JSON у файлі та спробуйте завантажити дані з файлу.
import json, os

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"countries_data.json") 

countries_data = {
    "Ukraine": {
        "capital": "Kyiv",
        "continent": "Europe",
        "landmarks": ["St. Sophia's Cathedral", "Kyiv Pechersk Lavra", "Independence Square"]
    },
    "Japan": {
        "capital": "Tokyo",
        "continent": "Asia",
        "landmarks": ["Mount Fuji", "Tokyo Tower", "Fushimi Inari Shrine"]
    },
    "Brazil": {
        "capital": "Brasilia",
        "continent": "South America",
        "landmarks": ["Christ the Redeemer", "Sugarloaf Mountain", "Iguazu Falls"]
    },
    "Australia": {
        "capital": "Canberra",
        "continent": "Australia",
        "landmarks": ["Sydney Opera House", "Great Barrier Reef", "Uluru"]
    },
    "Canada": {
        "capital": "Ottawa",
        "continent": "North America",
        "landmarks": ["CN Tower", "Banff National Park", "Niagara Falls"]
    },
    "Egypt": {
        "capital": "Cairo",
        "continent": "Africa",
        "landmarks": ["Pyramids of Giza", "The Sphinx", "The Egyptian Museum"]
    },
    "France": {
        "capital": "Paris",
        "continent": "Europe",
        "landmarks": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"]
    },
    "India": {
        "capital": "New Delhi",
        "continent": "Asia",
        "landmarks": ["Taj Mahal", "Red Fort", "Qutub Minar"]
    },
    "Mexico": {
        "capital": "Mexico City",
        "continent": "North America",
        "landmarks": ["Chichen Itza", "Teotihuacan", "Frida Kahlo Museum"]
    },
    "South Africa": {
        "capital": "Pretoria",
        "continent": "Africa",
        "landmarks": ["Table Mountain", "Kruger National Park", "Robben Island"]
    }
}

with open(file_name, "w") as file:
    json.dump(countries_data, file, indent=4)

with open(file_name, "r") as file:
    loaded_data = json.load(file)

print(loaded_data)



# Task2
# Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH. 
# Спробуйте здійснити пошук вмісту за створеним документом XML, ускладнюючи свої запити 
# та додаючи нові елементи, якщо буде потрібно.

# З бібліотекою XML
import os
import xml.etree.ElementTree as ET

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "orders.xml")

tree = ET.parse(file_name)
root = tree.getroot()

print("Кореневий елемент:", root.tag)

# Пройдемося по всіх замовленнях і виведемо інформацію
for order in root.findall('order'):
    order_id = order.get('id')
    client_name = order.find('client/firstName').text + " " + order.find('client/lastName').text
    delivery_type = order.find('delivery').get('type')

    print(f"\nЗамовлення ID: {order_id}")
    print(f"Клієнт: {client_name}")
    print(f"Тип доставки: {delivery_type}")

    print("Продукти:")
    for product in order.findall('products/product'):
        product_name = product.find('name').text
        product_price = product.find('price').text
        print(f" - {product_name}: ${product_price}")

# #######################################################################       

# # З бібліотекою LXML
import os
from lxml import etree

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "orders.xml")

with open(file_name, 'r') as file:
    tree = etree.parse(file)

root = tree.getroot()

# 1. Отримати всі замовлення
orders = tree.xpath('//order')
print(f"Кількість замовлень: {len(orders)}")

# 2. Отримати імена всіх клієнтів
client_names = tree.xpath('//client/firstName/text()')
print("\nІмена клієнтів:", client_names)

# 3. Отримати всі замовлення з доставкою типу "Courier"
courier_orders = tree.xpath('//order[delivery/@type="Courier"]')
print(f"\nЗамовлення з доставкою 'Courier': {len(courier_orders)}")

# 4. Отримати всі продукти з ціною більше ніж 500
expensive_products = tree.xpath('//product[price > 500]/name/text()')
print("\nПродукти з ціною більше ніж 500:", expensive_products)

# 5. Пройдемося по всіх замовленнях і виведемо інформацію
for order in orders:
    order_id = order.get('id')
    client_name = order.xpath('client/firstName/text()')[0] + " " + order.xpath('client/lastName/text()')[0]
    delivery_type = order.xpath('delivery/@type')[0]

    print(f"\nЗамовлення ID: {order_id}")
    print(f"Клієнт: {client_name}")
    print(f"Тип доставки: {delivery_type}")

    # Продукти у замовленні
    products = order.xpath('products/product')
    print("Продукти:")
    for product in products:
        product_name = product.xpath('name/text()')[0]
        product_price = product.xpath('price/text()')[0]
        print(f" - {product_name}: ${product_price}")



# Task3
# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. 
# Зареєструйте створені діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.

import csv, os

file_name1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),"1.csv") 
file_name2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),"2.csv") 

# Реєстрація першого діалекту
csv.register_dialect(
    'my_dialect_1',
    delimiter=';',           # Розділювач полів - крапка з комою
    quotechar='"',           # Текст обмежується подвійними лапками
    escapechar='\\',         # Екрануючий символ - бекслеш
    doublequote=True,        # Подвоювати лапки, якщо всередині тексту
    skipinitialspace=True,   # Ігнорувати пробіли після роздільника
    lineterminator='\n',      # Розділювач рядків - новий рядок
    quoting=csv.QUOTE_MINIMAL # Цитувати лише, коли необхідно
)

# Використання першого зареєстрованого діалекту для запису CSV
with open(file_name1, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='my_dialect_1')
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John Doe', '28', 'New York'])
    writer.writerow(['Jane Smith', '34', 'San Francisco'])

# Реєстрація другого діалекту
csv.register_dialect(
    'my_dialect_2',
    delimiter=',',           # Розділювач полів - кома
    quotechar="'",           # Текст обмежується одинарними лапками
    escapechar='\\',         # Екрануючий символ - бекслеш
    doublequote=False,       # Не подвоювати лапки
    skipinitialspace=True,   # Ігнорувати пробіли після роздільника
    lineterminator='\r\n',    # Розділювач рядків - новий рядок (Windows)
    quoting=csv.QUOTE_ALL    # Цитувати всі значення
)

# Використання другого зареєстрованого діалекту для запису CSV
with open(file_name2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='my_dialect_2')
    writer.writerow(['Product', 'Price', 'Quantity'])
    writer.writerow(['Apple', '0.5', '100'])
    writer.writerow(['Banana', '0.3', '150'])

# Читання CSV за допомогою першого діалекту
with open(file_name1, newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='my_dialect_1')
    for row in reader:
        print(row)

# Читання CSV за допомогою другого діалекту
with open(file_name2, newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='my_dialect_2')
    for row in reader:
        print(row)



# Task4
# Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу. 
# Поле «додаткові  характеристики матеріалу» має зберігати у собі масив, кожен елемент якого є кортежем із двох значень: перше – назва характеристики, а друге – її значення.
import sqlite3
import os

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"materials.db") 
db = sqlite3.connect(file_name)
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight REAL NOT NULL,
    height REAL NOT NULL,
    add_characteristics TEXT NOT NULL
)
''')

def add_material(weight, height, add_characteristics):
    add_characteristics_str = ','.join([f"{name}:{value}" for name, value in add_characteristics])

    print (add_characteristics_str)
    
    cur.execute('''
    INSERT INTO materials (weight, height, add_characteristics)
    VALUES (?, ?, ?)
    ''', (weight, height, add_characteristics_str))
    db.commit()

def get_materials():
    cur.execute('SELECT * FROM materials')
    rows = cur.fetchall()
    materials = []
    for row in rows:
        add_characteristics = [tuple(characteristic.split(':')) for characteristic in row[3].split(',')]
    
        materials.append({
            'id': row[0],
            'weight': row[1],
            'height': row[2],
            'additional_features': add_characteristics
        })
    return materials

add_material(10.5, 20, [('колір', 'червоний'), ('матеріал', 'метал')])
add_material(15, 25.3, [('колір', 'синій'), ('матеріал', 'пластик')])
add_material(11.3, 7, [('колір', 'чорний'), ('матеріал', 'метал')])
add_material(10, 7.4, [('колір', 'білий'), ('матеріал', 'пластик')])

materials = get_materials()
for material in materials:
    print(material)

# Task5
# Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, 
# яка рахує середнє значення ваги всіх матеріалів вислідної вибірки й округляє значення до цілого. 
def get_avg_weight():
    cur.execute('SELECT ROUND(AVG(weight)) FROM materials')
    avg_weight = cur.fetchone()[0]
    return avg_weight if avg_weight is not None else 0

avg_weight = get_avg_weight()
print(avg_weight)

# Task6 
# Для таблиці «матеріалу» з завдання 4 створіть функцію користувача, 
# яка приймає необмежену кількість полів і повертає їх конкатенацію.
def fnc_concat_fields(*fields):
    return ', '.join(fields)

db.create_function("fnc_concat_fields", -1, fnc_concat_fields)

cur.execute('SELECT fnc_concat_fields("Вага: " || weight, " Висота: " || height) FROM materials')
results = cur.fetchall()

for result in results:
    print(result[0])

db.close()



# Task7
# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль. 
# Файл має містити такі стовпчики: імена, прізвища, дати народження та місто проживання. 
# Реалізуйте можливості перезапису цього файлу, додавання нових рядків до наявного файлу, 
# рядкового читання з файлу та конвертації всього вмісту у формати XML та JSON.
import csv
import json
import xml.etree.ElementTree as ET
import os

def write_to_csv(file_name: str, data: list, mode: str):
    with open(file_name, mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if mode == 'w':
            writer.writerow(['Ім\'я', 'Прізвище', 'Дата народження', 'Місто проживання']) 
        for row in data:
            writer.writerow(row)

def read_from_csv(file_name: str):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        return [row for row in reader]

def convert_to_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def convert_to_xml(data, xml_file):
    root = ET.Element('people')
    for row in data:
        person = ET.SubElement(root, 'person')
        ET.SubElement(person, 'first_name').text = row[0]
        ET.SubElement(person, 'last_name').text = row[1]
        ET.SubElement(person, 'date_of_birth').text = row[2]
        ET.SubElement(person, 'city').text = row[3]

    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

def main():
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.csv")
    json_file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.json")
    xml_file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.xml")

    menu = '\nОберіть меню:, 1-для запису, 2-для додавання, 3-для читання, 4-для конвертації в JSON, 5-для конвертації в XML, 0-Вихід, '
    
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()

        if choise == "0":
                break
        
        elif choise == '1':
            data = []
            num_rows = int(input("Скільки записів ви хочете додати? "))
            for _ in range(num_rows):
                first_name = input("Введіть ім'я: ")
                last_name = input("Введіть прізвище: ")
                date_of_birth = input("Введіть дату народження (ДД.ММ.РРРР): ")
                city = input("Введіть місто проживання: ")
                data.append([first_name, last_name, date_of_birth, city])
            write_to_csv(file_name, data, mode='w')
        
        elif choise == '2':
            data = []
            num_rows = int(input("Скільки записів ви хочете додати? "))
            for _ in range(num_rows):
                first_name = input("Введіть ім'я: ")
                last_name = input("Введіть прізвище: ")
                date_of_birth = input("Введіть дату народження (ДД.ММ.РРРР): ")
                city = input("Введіть місто проживання: ")
                data.append([first_name, last_name, date_of_birth, city])
            write_to_csv(file_name, data, mode='a') 

        elif choise == '3':
            if os.path.exists(file_name):
                data = read_from_csv(file_name)
                for row in data:
                    print(row)
            else:
                print("Файл не знайдено")

        elif choise == '4': 
            if os.path.exists(file_name):
                data = read_from_csv(file_name)
                convert_to_json(data, json_file_name)
                print("Дані успішно конвертовані в JSON.")
            else:
                print("Файл не знайдено.")

        elif choise == '5': 
            if os.path.exists(file_name):
                data = read_from_csv(file_name)
                convert_to_xml(data, xml_file_name)
                print("Дані успішно конвертовані в XML.")
            else:
                print("Файл не знайдено")

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
