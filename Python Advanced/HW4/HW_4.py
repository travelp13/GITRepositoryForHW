# Task1
# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
from datetime import datetime
import os, sqlite3

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"transactions.db") 

db = sqlite3.connect(file_name)
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trnxinfo TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
);
''')

def add_transaction(trnxinfo: str, amount: float, date: str):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        cur.execute('''
        INSERT INTO transactions (trnxinfo, amount, date)
        VALUES (?, ?, ?);
        ''', (trnxinfo, amount, date))
        db.commit()
    except ValueError:
        print ("Невірний формат дати (YYYY-MM-DD)")

add_transaction("Кава", 51, "2024-10-18")
add_transaction("Метро", 8, "2024-10-17")
add_transaction("АТБ", 514.12, "2024-10-17")

# Task3
#Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.
cur.execute('''
CREATE TABLE IF NOT EXISTS transactionclass (
    id INTEGER PRIMARY KEY,
    trnxname TEXT NOT NULL
);
''')

try:
    cur.execute('''
        INSERT INTO transactionclass
        VALUES (1, 'Витрата');
        ''')
    cur.execute('''       
        INSERT INTO transactionclass
        VALUES (2, 'Дохід');
        ''')                                            
    db.commit()
except sqlite3.IntegrityError:
    pass

cur.execute('''PRAGMA foreign_keys = OFF;''')

try:
    cur.execute('''
    ALTER TABLE transactions ADD transaction_type_id INTEGER REFERENCES transactionclass(id);
    ''')
except sqlite3.OperationalError:
    pass

cur.execute('''
    UPDATE transactions
       SET transaction_type_id = 1
     WHERE transaction_type_id IS NULL;
    ''')
db.commit()

cur.execute('''PRAGMA foreign_keys = ON;''')

# Task2
# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних. 
def add_trnx(trnxinfo: str, amount: float, date: str, transaction_type_id: int):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        cur.execute('''
        INSERT INTO transactions (trnxinfo, amount, date, transaction_type_id)
        VALUES (?, ?, ?, ?);
        ''', (trnxinfo, amount, date, transaction_type_id))
        db.commit()
    except (ValueError, TypeError) :
        print ("Невірний формат дати (YYYY-MM-DD)")

def get_all_transactions():
    cur.execute('SELECT t.id, t.trnxinfo, t.amount, l.trnxname, t.date FROM transactions t, transactionclass l WHERE t.transaction_type_id = l.id;')
    transactions = cur.fetchall()
    if transactions:
        print("ID | Призначення | Сума | Тип | Час")
        print("----------------------------------------")
        for transaction in transactions:
            print(f"{transaction[0]} | {transaction[1]} | {transaction[2]} грн | {transaction[3]} | {transaction[4]}")

# Task 4
# Створіть агрегатні функції для підрахунку загальної кількості витрат i прибуткiв за місяць. 
# Забезпечте відповідний інтерфейс користувача.
def get_debit_trnx(month: str):
    try:
        cur.execute('''
        SELECT SUM(amount) FROM transactions
         WHERE transaction_type_id = 1 AND strftime('%Y-%m', date) = ?;
        ''', (month, ))
        result = cur.fetchone()
        print(result)
        return result[0] if result[0] else 0
    except sqlite3.Error as e:
        print(f"Помилка: {e}")

def get_credit_trnx(month: str):
    try:
        cur.execute('''
        SELECT SUM(amount) FROM transactions
         WHERE transaction_type_id = 2 AND strftime('%Y-%m', date) = ?
        ''', (month,))
        result = cur.fetchone()
        return result[0] if result[0] else 0
    except sqlite3.Error as e:
        print(f"Помилка: {e}")

def main():
    menu = '\nОберіть меню:, 1-Додати транзакцію, 2-Показати всі транзакції, 3-Показати витрати за місяць, 4-Показати дохід за місяць, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choice = input()
        try:
            if choice == "0":
                break         

            elif choice == '1':
                trnxinfo = input("Введіть призначення: ")
                amount = float(input("Введіть суму: "))
                transaction_type = int(input("Тип транзакції (1 - Витрата; 2 - Дохід): "))
                if transaction_type not in (1, 2):
                    print("Невірний тип транзакції")
                    continue
                date = input("Введіть дату (YYYY-MM-DD): ")
                add_trnx(trnxinfo, amount, date, transaction_type)

            elif choice == '2':
                get_all_transactions()

            elif choice == '3':
                month = input("Введіть місяць у форматі YYYY-MM: ")
                amount = get_debit_trnx(month)
                print(f"Загальні витрати за {month}: {amount} грн")

            elif choice == '4':
                month = input("Введіть місяць у форматі YYYY-MM: ")
                amount = get_credit_trnx(month)
                print(f"Загальний дохід за {month}: {amount} грн")

            else:
                print("Невірний вибір")

        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

main()

db.close()


#Task 5
# Create an Exchange Rates To USD db using API Monobank (api.monobank.ua). Do requests via request lib, parse results, write it into db. (3 examples required)
# Example:
# Table - Exchange Rate To USD:
# id (INT PRIMARY KEY) - 1, 2, 3, ...
# currency_name (TEXT) - UAH
# currency_value (REAL) - 39.5
# current_date (DATETIME) - 10/22/2022 7:00 PM
import requests
import sqlite3, os
from datetime import datetime

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),"currency_rates.db") 

def create_table():
    db = sqlite3.connect(file_name)
    cur = db.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rate_to_usd (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT NOT NULL,
            currency_value REAL NOT NULL,
            current_date DATETIME NOT NULL
        )
    ''')

    db.commit()
    return db, cur

def get_curr_rate_from_api():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error getting data")
        return None
    
    return response.json()

def parse_rates(data):
    currency_map = {
        840: 'USD', 
        978: 'EUR',  
        980: 'UAH',
    }
    
    rates = []
    
    for rate in data:
        if rate['currencyCodeB'] == 840:
            currency_name = currency_map.get(rate['currencyCodeA'], 'Unknown')
            currency_value = rate.get('rateBuy') or rate.get('rateCross', 0)
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            rates.append((currency_name, currency_value, current_date))
    
    return rates

def insert_rate(cur, conn, rates):
    cur.executemany('''
        INSERT INTO exchange_rate_to_usd (currency_name, currency_value, current_date)
        VALUES (?, ?, ?)
    ''', rates)
    conn.commit()

def main():
    db, cur = create_table()
    
    data = get_curr_rate_from_api()
    
    if data:
        rates = parse_rates(data)
      
        insert_rate(cur, db, rates)
    
    db.close()

if __name__ == '__main__':
    main()
