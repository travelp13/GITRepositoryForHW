import psycopg2
from collections import namedtuple
from psycopg2.extras import DictCursor
from datetime import datetime


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="admin",
    dbname="hw3",
    cursor_factory=DictCursor
    )

conn.autocommit = True
cur = conn.cursor()

def create_tables():
    query = '''
        CREATE TABLE IF NOT EXISTS BRAND (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS LOCATION (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL,
            ADDRESS VARCHAR(100) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS CAR (
            ID SERIAL PRIMARY KEY,
            BRAND_ID INT NOT NULL,
            MODEL VARCHAR(50) NOT NULL,
            VIN VARCHAR(20) NOT NULL UNIQUE,
            LOCATION_ID INT NOT NULL,
            FOREIGN KEY (BRAND_ID) REFERENCES BRAND (ID),
            FOREIGN KEY (LOCATION_ID) REFERENCES LOCATION (ID)
        );

        CREATE TABLE IF NOT EXISTS MANAGER (
            ID SERIAL PRIMARY KEY,
            FIRST_NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            LOCATION_ID INT NOT NULL,
            PHONE VARCHAR(20) NOT NULL UNIQUE,
            FOREIGN KEY (LOCATION_ID) REFERENCES LOCATION (ID)
        );

        CREATE TABLE IF NOT EXISTS CLIENT (
            ID SERIAL PRIMARY KEY,
            FIRST_NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL,
            PHONE VARCHAR(20) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS "order" (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL UNIQUE,
            ORDER_DATE TIMESTAMP,
            CLIENT_ID INT NOT NULL,
            CAR_ID INT NOT NULL,
            MANAGER_ID INT NOT NULL,
            PRICE NUMERIC(10, 2),
            FOREIGN KEY (CLIENT_ID) REFERENCES CLIENT (ID),
            FOREIGN KEY (CAR_ID) REFERENCES CAR (ID),
            FOREIGN KEY (MANAGER_ID) REFERENCES MANAGER (ID)
        );

        CREATE TABLE IF NOT EXISTS TESTDRIVE (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL UNIQUE,
            TD_DATE TIMESTAMP,
            ADDRESS VARCHAR(100) NOT NULL,
            CLIENT_ID INT NOT NULL,
            MANAGER_ID INT NOT NULL,
            FOREIGN KEY (CLIENT_ID) REFERENCES CLIENT (ID),
            FOREIGN KEY (MANAGER_ID) REFERENCES MANAGER (ID)
        );

        CREATE TABLE IF NOT EXISTS TESTDRIVE_CAR (
            ID SERIAL PRIMARY KEY,
            TESTDRIVE_ID INT NOT NULL,
            CAR_ID INT NOT NULL,
            FOREIGN KEY (TESTDRIVE_ID) REFERENCES TESTDRIVE (ID),
            FOREIGN KEY (CAR_ID) REFERENCES CAR (ID),
            CONSTRAINT UNQ_TESTDRIVE_CAR UNIQUE (TESTDRIVE_ID, CAR_ID)
        );
    '''
    cur.execute(query)

def add_brand(name: str):
    cur.execute('''INSERT INTO brand (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;''', (name,))

def add_location(name: str, address: str):
    cur.execute('''INSERT INTO location (name, address) VALUES (%s,%s) ON CONFLICT (address) DO NOTHING;''', (name, address))

def add_car(brand_id: int, model: str, vin: str,  location_id: int):
    cur.execute('''INSERT INTO car (brand_id, model, vin, location_id) VALUES (%s,%s,%s,%s) ON CONFLICT (vin) DO NOTHING;''', 
                (brand_id, model, vin, location_id))

def add_manager(first_name: str, last_name: str, location_id: int,  phone: str):
    cur.execute('''INSERT INTO manager (first_name, last_name, location_id, phone) VALUES (%s,%s,%s,%s) ON CONFLICT (phone) DO NOTHING;''', 
                (first_name, last_name, location_id, phone))

def add_client(first_name: str, last_name: str, email: str,  phone: str):
    cur.execute('''INSERT INTO client (first_name, last_name, email, phone) VALUES (%s,%s,%s,%s) ON CONFLICT (phone) DO NOTHING;''', 
                (first_name, last_name, email, phone))

def add_order(name: str, order_date: str, client_id: int,  car_id: int, manager_id: int, price: float):
    dt_obj = datetime.strptime(order_date, "%Y-%m-%d %H:%M")
    cur.execute('''INSERT INTO "order" (name, order_date, client_id, car_id, manager_id, price) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (name) DO NOTHING;''', 
                (name, dt_obj, client_id, car_id, manager_id, price))

def add_testdrive(name: str, td_date: str, address: str, client_id: int,  manager_id: int):
    dt_obj = datetime.strptime(td_date, "%Y-%m-%d %H:%M")
    cur.execute('''INSERT INTO testdrive (name, td_date, address, client_id,  manager_id) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (name) DO NOTHING;''', 
                (name, dt_obj, address, client_id, manager_id))
    
def add_testdrive_car(testdrive_id: int,  car_id: int):
    cur.execute('''INSERT INTO testdrive_car (testdrive_id, car_id) VALUES (%s,%s) ON CONFLICT (testdrive_id, car_id) DO NOTHING;''', 
                (testdrive_id, car_id))  

def create_data():
    create_tables()

    add_brand("Toyota")
    add_brand("Mersedes")
    add_brand("BMW")
    add_brand("Volvo")
    add_brand("Honda")

    add_location("Main Branch", "123 Main St")
    add_location("Uptown  Branch", "789 Uptown Blvd")

    add_car(1, "Corolla", "JT12345VIN001", 1)
    add_car(1, "Corolla", "KS12345VIN002", 2)
    add_car(1, "Corolla", "KS12DD5VIN002", 2)
    add_car(2, "A-Class v177", "MS12DDHHSADN2", 1)
    add_car(2, "EQS v297 2024", "MS12DDFHSADN2", 1)
    add_car(2, "C-Class", "MS12DLHHSADN2", 2)
    add_car(3, "X5", "BMW2DD5VIN002", 1)
    add_car(3, "X6", "BMW2DD5VIN007", 2)
    add_car(3, "X3", "BMW2DD5VIN009", 2)
    add_car(4, "S90", "VOL2DD5VIN012", 1)
    add_car(4, "XC90", "VOL2DD5VIN004", 1)
    add_car(4, "V90", "VOL2DD5VIN019", 2)
    add_car(5, "Accord", "HON2DD5VIN012", 1)
    add_car(5, "CR-V", "HON2DD5VIN004", 1)
    add_car(5, "Civic", "HON2DD5VIN019", 2)

    add_manager("Nick", "Saon", 1, "4445556667")
    add_manager("Adriana", "Kalm", 1,  "4445556668")
    add_manager("Nick", "York", 2, "4445556669")
    add_manager("Alice", "Lee", 2, "4445556665")

    add_client("John", "Doe", "john.doe@example.com", "1234567890")
    add_client("Jane", "Smith", "jane.smith@example.com", "2345678901")
    add_client("Robert", "Brown", "robert.brown@example.com", "3456789012")
    add_client("Emily", "Davis", "emily.davis@example.com", "4567890123")
    add_client("Michael", "Wilson", "michael.wilson@example.com", "5678901234")
    add_client("Sophia", "Moore", "sophia.moore@example.com", "6789012345")

    add_order("O-1", "2024-05-15 14:30",1,10,1,56789.21)
    add_order("O-2", "2024-05-17 9:30",1,1,1,90152.99)
    add_order("O-3", "2024-05-22 11:00",1,14,1,28465)
    add_order("O-4", "2024-05-23 10:00",2,4,2,80000)
    add_order("O-5", "2024-05-23 15:00",3,9,3,118000)
    add_order("O-6", "2024-05-24 13:00",4,15,4,48500)
    add_order("O-7", "2024-05-25 18:00",5,13,2,55000)
    add_order("O-8", "2024-05-27 9:00",6,14,2,28465)
    add_order("O-9", "2024-05-28 10:25",4,3,3,25000)
    add_order("O-10", "2024-05-28 17:00",5,6,3,78900)

    add_testdrive("T-1", "2024-04-30 14:30", "123 Main St", 1, 1)
    add_testdrive("T-2", "2024-05-05 17:00", "123 Main St", 6, 2)
    add_testdrive("T-3", "2024-05-07 10:30", "789 Uptown Blvd", 5, 4)

    add_testdrive_car(1,10)
    add_testdrive_car(1,11)
    add_testdrive_car(1,14)
    add_testdrive_car(2,4)
    add_testdrive_car(2,6)
    add_testdrive_car(3,8)
    add_testdrive_car(3,9)

create_data()

def get_all_orders():
    query = '''
        SELECT
            O.NAME,
            O.ORDER_DATE,
            O.PRICE,
            C.FIRST_NAME || ' ' || C.LAST_NAME AS CLIENT_NAME,
            B.NAME || ' ' || R.MODEL AS CAR,
            M.FIRST_NAME || ' ' || M.LAST_NAME AS MANAGER_NAME
        FROM
            "order" O,
            CLIENT C,
            CAR R,
            BRAND B,
            MANAGER M
        WHERE
            O.CLIENT_ID = C.ID
            AND R.ID = O.CAR_ID
            AND B.ID = R.BRAND_ID
            AND O.MANAGER_ID =M.ID
        ORDER BY
            O.ORDER_DATE
    '''
    cur.execute(query)
    return cur.fetchall()

def get_all_testdrives():
    query = '''
        SELECT
            T.NAME,
            T.TD_DATE,
            C.FIRST_NAME || ' ' || C.LAST_NAME AS CLIENT_NAME,
            B.NAME || ' ' || R.MODEL AS CAR,
            M.FIRST_NAME || ' ' || M.LAST_NAME AS MANAGER_NAME
        FROM
            TESTDRIVE_CAR TC,
            TESTDRIVE T,
            CLIENT C,
            CAR R,
            BRAND B,
            MANAGER M
        WHERE
            TC.TESTDRIVE_ID = T.ID
            AND T.CLIENT_ID = C.ID
            AND R.ID = TC.CAR_ID
            AND B.ID = R.BRAND_ID
            AND T.MANAGER_ID = M.ID
        ORDER BY
            T.TD_DATE
    '''
    cur.execute(query)
    return cur.fetchall()

for order in get_all_orders():
    print(f"Order Name: {order['name']}")
    print(f"Order Date: {order['order_date']}")
    print(f"Price: {order['price']}")
    print(f"Client Name: {order['client_name']}")
    print(f"Car: {order['car']}")
    print(f"Manager Name: {order['manager_name']}")
    print("=" * 40)

for order in get_all_testdrives():
    print(f"Testdrive Name: {order['name']}")
    print(f"Testdrive Date: {order['td_date']}")
    print(f"Client Name: {order['client_name']}")
    print(f"Car: {order['car']}")
    print(f"Manager Name: {order['manager_name']}")
    print("=" * 40)
