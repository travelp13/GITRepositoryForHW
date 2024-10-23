# Task1 
# Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database, 
# використовуючи стандартну бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp. 
# Кроки, які мають бути залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200. 
# Перевірте хід виконання програми на >3 ресурсах і перегляньте послідовність запису логів в обох варіантах 
# і порівняйте результати. Для двох видів завдань використовуйте різні файли для логування, 
# щоби порівняти отриманий результат. 

import requests
import sqlite3, os
import aiohttp
import asyncio

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs.db") 

db = sqlite3.connect(file_name)
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS requests_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    message TEXT
)
''')
db.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS aiohttp_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    message TEXT
)
''')
db.commit()

def add_requests_log (message: str):
    cur.execute('INSERT INTO requests_logs (message) VALUES (?)', (message,))
    db.commit()

def add_aiohttp_log (message: str):
    cur.execute('INSERT INTO aiohttp_log (message) VALUES (?)', (message,))
    db.commit()    

urls = [
    "https://www.ukr.net",
    "https://www.dgt.es/inicio/",
    "https://www.mfat.govt.nz/en/countries-and-regions/europe/ukraine",
    "https://www.cnn.com",
    "https://www.globo.com",
    "https://www.clarin.com",
    "https://www.bbc.com",
    "https://www.dw.com",
    "https://www.sina.com.cn",
    "https://www.news24.com",
    "https://www.abc.net.au/news"
]

def get_requests_content(url):
    add_requests_log(f"{url} : запит до адреси")
    response = requests.get(url)
    if response.status_code == 200:
        add_requests_log(f"{url} : відповідь 200")
    else:
        add_requests_log(f"{url} : помилка {response.status_code}")
    return response.content

async def get_aiohttp_content(url):
    add_aiohttp_log(f"{url} : запит до адреси")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                add_aiohttp_log(f"{url} : відповідь 200")
            else:
                add_aiohttp_log(f"{url} : помилка {response.status}")
            return await response.text()

for url in urls:
    get_requests_content(url)

async def aiohttp_main():
    tasks = [get_aiohttp_content(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(aiohttp_main())

def select_logs():
    cur.execute('''SELECT 'requests' as type, t.id, t.timestamp, t.message FROM requests_logs t ORDER BY t.id;''')
    data = cur.fetchall()
    if data:
        print("Бібліотека| ID |  Час  | Повідомлення")
        print("----------------------------------------")
        for data in data:
            print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")
    print("---------------------------------------------------------------------")
    cur.execute('''SELECT 'aiohttp' as type, t.id, t.timestamp, t.message FROM aiohttp_log t ORDER BY t.id;''')
    data = cur.fetchall()
    if data:
        print("Бібліотека| ID |  Час  | Повідомлення")
        print("----------------------------------------")
        for data in data:
            print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")

select_logs()

db.close()