import re
from module_products import Product
from module_orders import Order
from module_warehouses import Warehouse
from module_clients import Client
from module_reports import Report

product = Product()
client  = Client()
order = Order()
warehouse = Warehouse()
report = Report(warehouse, product, order)

####### Checks #######
def is_negative(value):
    if value < 0:
        raise ValueError("Число не може бути менше нуля!")
    return value
    
def to_int(value):
    try:
        return is_negative(int(value))
    except ValueError:
        raise ValueError("Значення має бути числом!")

def to_float(value):
    try:
        return is_negative(float(value))
    except ValueError:
        raise ValueError("Значення має бути числом!")
    
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email) is not None:
        return email
    else:
        raise ValueError("Некоректний email!")
    
def is_valid_phone(phone):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if re.match(pattern, phone) is not None:
        return phone
    else:
        raise ValueError("Некоректний телефон!")

####### Warehouses functions #######
def add_warehouse(name:str, address:str, capacity:int):
    warehouse.add_warehouse(name, address, capacity)

def edit_warehouse(product_id:int, **kwargs) -> dict:
    prod = product.find_product_by_id(product_id)
    if prod:
        edit_warehouse = warehouse.edit_warehouse(product_id, **kwargs)
        return edit_warehouse   
    else:
        raise ValueError("WarehouseID not found")
    
def add_product_to_warehouse(warehouse_id:int, product_id:int, quantity:int):
    wh = warehouse.find_warehouse_by_id(warehouse_id)
    prod = product.find_product_by_id(product_id)
    if prod and wh:
        warehouse.add_product_to_warehouse(warehouse_id, product_id, quantity)
    else:
        raise ValueError("WarehouseID or ProductID not found")

def edit_product_quantity(product_id:int, quantity:int):
    prod = product.find_product_by_id(product_id)
    if prod:
        warehouse.edit_product_quantity(product_id, quantity)
        product.edit_product(product_id, quantity = quantity)
    else:
        raise ValueError("ProductID not found")
    
def show_warehouses():
    for wh in warehouse.get_warehouses():
        print(f"Id: {wh["id"]} Name: {wh["name"]} Address: {wh["address"]}")

def show_warehouse_info(warehouse_id:int):
    wh = warehouse.find_warehouse_by_id(warehouse_id)
    if wh:        
        products_quantity = warehouse.get_total_quantity(warehouse_id)
        free_space = warehouse.get_free_space(warehouse_id)
        print (f"Name: {wh["name"]}\nAddress: {wh["address"]}\nCapacity: {wh["capacity"]}\nProducts:")
        print (f"Total quantity: {products_quantity}\nFree space: {free_space}")
        for prod in warehouse.get_warehouse_products(warehouse_id):
            print (f"  - {product.find_product_by_id(prod["id"])["name"]} - {prod["quantity"]} units")
    else:
        raise ValueError("WarehouseID not found")

####### Products functions #######
def add_product(name:str, category:str, price:float, quantity:int, description:str, warehouse_id:int):
    wh = warehouse.find_warehouse_by_id(warehouse_id)
    if wh:
        free_space = warehouse.get_free_space(warehouse_id)
        if free_space >= quantity:
            product_id = product.add_product(name, category, price, quantity, description)
            add_product_to_warehouse(warehouse_id, product_id, quantity)
        else:
            raise ValueError("The quantity of products exceeds the available space in the warehouse")
    else:
        raise ValueError("WarehouseID not found")

def edit_product(product_id:int, **kwargs) -> dict:
    prod = product.find_product_by_id(product_id)
    if prod:
        quantity = kwargs.get("quantity", None)
        if quantity:
            edit_product_quantity(product_id, quantity)            
        edit_product = product.edit_product(product_id, **kwargs)
        return edit_product   
    else:
        raise ValueError("ProductID not found")

def delete_product(product_id):
    if product.delete_product(product_id):
        warehouse.delete_product(product_id)
    else:
        raise ValueError("ProductID not found")
    
def search_products(**kwargs):
    return product.search_products(**kwargs)

def search_products_menu():
    product_id = input("Введіть ID продукту або 'Enter' щоб пропустити: ")
    name = input("Введіть назву продукту або 'Enter' щоб пропустити: ")
    category = input("Введіть назву категорії або 'Enter' щоб пропустити: ")
    price = input("Введіть ціну продукту або 'Enter' щоб пропустити: ")
    quantity = input("Введіть кількість продукту або 'Enter' щоб пропустити: ")
    description = input("Введіть опис продукту або 'Enter' щоб пропустити: ")
    params = dict()
    if product_id:
        params["id"] = to_int(product_id)
    if name:
        params["name"] = name
    if category:
        params["category"] = category
    if price:
        params["price"] = to_float(price)
    if quantity:
        params["quantity"] = to_int(quantity)
    if description:
        params["description"] = description
    if params:
        print("Знайдені продукти:\n")
        result = search_products(**params)
        product.print_products(result)

####### Orders functions #######
def add_order(client_id:int, products: list):
    cl = client.find_client_by_id(client_id)
    if cl:
        total_amount = order.add_order(client_id, products)
        for prod in products:
            product_id = prod["product_id"]
            pr = product.find_product_by_id(product_id)
            new_quantity = pr["quantity"] - prod["quantity"]
            edit_product(product_id, quantity = new_quantity)
        print(f"Загальна сума замовлення: {total_amount}")
    else:
        raise ValueError("ClientID not found")

def change_status(order_id:int, status:int):
    ord = order.find_order_by_id(order_id)
    if ord:
        if order.get_status_by_id(status):
            order.change_status(order_id, status)            
        else:
            raise ValueError("Status not found")
    else:
        raise ValueError("OrderID not found")

def search_orders(**kwargs):
    return order.search_orders(**kwargs)

def search_orders_menu():
    order_id = input("Введіть ID замовлення або 'Enter' щоб пропустити: ")
    client_id = input("Введіть ID клієнта або 'Enter' щоб пропустити: ")
    status = input("Введіть статус замовлення (1-New, 2-Confirmed, 3-Sent, 4-Delivered, 5-Cancelled) або 'Enter' щоб пропустити: ")
    params = dict()
    if order_id:
        params["id"] = to_int(order_id)
    if client_id:
        params["client_id"] = to_int(client_id)
    if status:
        status = to_int(status)
        status_name = order.get_status_by_id(status)
        if status_name:
            params["status"] = status_name
        else:
            raise ValueError("Status not found")
    if params:
        print("Знайдені замовлення:\n")
        result = search_orders(**params)
        order.print_orders(result)

####### Clients functions #######
def add_client(name:str, email:str, phone:str, address:str):
    client.add_client(name, email, phone, address)

def edit_client(client_id:int, **kwargs) -> dict:
    cl = client.find_client_by_id(client_id)
    if cl:
        edit_client = client.edit_client(client_id, **kwargs)
        return edit_client   
    else:
        raise ValueError("ClientID not found")

def get_client_orders(client_id:int):
    cl = client.find_client_by_id(client_id)
    if cl:
        result = search_orders(client_id = client_id)
        order.print_orders(result)
    else:
        raise ValueError("ClientID not found")

def search_clients(**kwargs):
    return client.search_clients(**kwargs)

def search_clients_menu():
    client_id = input("Введіть ID клієнта або 'Enter' щоб пропустити: ")
    name = input("Введіть ім'я клієнта або 'Enter' щоб пропустити: ")
    email = input("Введіть email клієнта або 'Enter' щоб пропустити: ")
    pnohe = input("Введіть телефон клієнта або 'Enter' щоб пропустити: ")
    address = input("Введіть адрес клієнта або 'Enter' щоб пропустити: ")
    params = dict()
    if client_id:
        params["id"] = to_int(client_id)
    if name:
        params["name"] = name
    if email:
        params["email"] = email
    if pnohe:
        params["pnohe"] = pnohe
    if address:
        params["address"] = address
    if params:
        print("Знайдені клієнти:\n")
        result = search_clients(**params)
        client.print_clients(result)

####### Reports functions #######
def get_warehouse_report():
    report.get_warehouse_report()

def get_most_popular_products():
    report.get_most_popular_products()


####### Menus #######
def warehouse_menu():
    menu = '\nОберіть меню:, 1-Додати склад, 2-Редагувати склад, 3-Редагувати кількість товар на складі, 4-Показати склади, 5-Показати інформацію про склад, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()
        try:
            if choise == "0":
                break
            elif choise == "1":
                name = input("Введіть назву складу: ")
                address = input("Введіть адресу складу: ")
                capacity = to_int(input("Введіть місткість складу: "))
                add_warehouse(name, address, capacity)
            elif choise == "2":
                warehouse_id = to_int(input("Введіть ID складу: "))    
                name = input("Введіть назву складу або 'Enter' щоб пропустити: ")
                address = input("Введіть адресу складу або 'Enter' щоб пропустити: ")
                capacity = input("Введіть місткість складу або 'Enter' щоб пропустити: ")
                params = dict()
                if name:
                    params["name"] = name
                if address:
                    params["address"] = address
                if capacity:
                    params["capacity"] = to_int(capacity)               
                if params:
                    edits = edit_warehouse(warehouse_id, **params)
                    print(edits)
            elif choise == "3":
                product_id = to_int(input("Введіть ID продукту: "))
                quantity = to_int(input("Введіть кількість продукту: "))
                edit_product_quantity(product_id, quantity)
            elif choise == "4":
                show_warehouses()
            elif choise == "5":
                warehouse_id = to_int(input("Введіть ID складу: "))
                show_warehouse_info(warehouse_id)
            else:
                print("Немає такого пункту меню, виберіть ще раз:")
                continue
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

def product_menu():
    menu = '\nОберіть меню:, 1-Додати продукт, 2-Редагувати продукт, 3-Видалити продукт, 4-Шукати продукт, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()
        try:
            if choise == "0":
                break
            elif choise == "1":
                name = input("Введіть назву продукту: ")
                category = input("Введіть назву категорії: ")
                price = to_float(input("Введіть ціну продукту: "))
                quantity = to_int(input("Введіть кількість продукту: "))
                description = input("Введіть опис продукту: ")
                warehouse_id = to_int(input("Введіть ID складу: "))
                add_product(name, category, price, quantity, description, warehouse_id)
            elif choise == "2":
                product_id = to_int(input("Введіть ID продукту: "))
                name = input("Введіть назву продукту або 'Enter' щоб пропустити: ")
                category = input("Введіть назву категорії або 'Enter' щоб пропустити: ")
                price = input("Введіть ціну продукту або 'Enter' щоб пропустити: ")
                quantity = input("Введіть кількість продукту або 'Enter' щоб пропустити: ")
                description = input("Введіть опис продукту або 'Enter' щоб пропустити: ")
                params = dict()
                if name:
                    params["name"] = name
                if category:
                    params["category"] = category
                if price:
                    params["price"] = to_float(price)
                if quantity:
                    params["quantity"] = to_int(quantity)
                if description:
                    params["description"] = description
                if params:
                    edits = edit_product(product_id, **params)
                    print(edits)
            elif choise == "3":
                product_id = to_int(input("Введіть ID продукту: "))
                delete_product(product_id)
            elif choise == "4":
                search_products_menu()
            else:
                print("Немає такого пункту меню, виберіть ще раз:")
                continue
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

def order_menu():
    menu = '\nОберіть меню:, 1-Оформлення нового замовлення, 2-Оновлення статусу, 3-Шукати замовлення, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()
        try:
            if choise == "0":
                break
            elif choise == "1":
                client_id = to_int(input("Введіть ID клієнта: "))
                products = []
                while True:
                    new_order_menu = '\nОберіть меню:, 1-Шукати товар, 2-Додати товар до замовлення, 0-Зберегти замовлення, '
                    print(("\n  ").join(new_order_menu.split(", ")))
                    choise = input()
                    if choise == "0":
                        break
                    elif choise == "1":
                        search_products_menu()
                    elif choise == "2":
                        product_id = to_int(input("Введіть ID продукту: "))
                        quantity = to_int(input("Введіть кількість продукту: "))
                        prod = product.find_product_by_id(product_id)
                        if prod:
                            if prod["quantity"] >= quantity:
                                products.append(
                                {
                                    "product_id": product_id,
                                    "name": prod["name"],
                                    "price": prod["price"],
                                    "quantity": quantity
                                })
                            else:
                                print("Кількість товару на складі менша, ніж ви намагаєтеся замовити")                                
                        else:
                            print("Товар не знайдено, повторіть замовлення")
                    else:
                        print("Немає такого пункту меню, виберіть ще раз:")
                        continue
                if products:
                    add_order(client_id, products)
                else:
                    print("Список товарів для замовлення порожній!")
            elif choise == "2":
                order_id = to_int(input("Введіть ID замовлення: "))
                status = to_int(input("Введіть статус замовлення (1-New, 2-Confirmed, 3-Sent, 4-Delivered, 5-Cancelled): "))
                change_status(order_id, status)
            elif choise == "3":
                search_orders_menu()
            else:
                print("Немає такого пункту меню, виберіть ще раз:")
                continue
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

def client_menu():
    menu = '\nОберіть меню:, 1-Додати клієнта, 2-Редагувати дані клієнта, 3-Перегляд історії замовлень, 4-Шукати клієнтів, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()
        try:
            if choise == "0":
                break
            elif choise == "1":
                name = input("Введіть ім'я клієнта: ")
                email = is_valid_email(input("Введіть email клієнта: "))
                pnohe = is_valid_phone(input("Введіть телефон клієнта: "))
                address = input("Введіть адрес клієнта: ")
                add_client (name, email, pnohe, address)
            elif choise == "2":
                client_id = to_int(input("Введіть ID клієнта: "))
                name = input("Введіть ім'я клієнта або 'Enter' щоб пропустити: ")
                email = input("Введіть email клієнта або 'Enter' щоб пропустити: ")
                pnohe = input("Введіть телефон клієнта або 'Enter' щоб пропустити: ")
                address = input("Введіть адрес клієнта або 'Enter' щоб пропустити: ")
                params = dict()
                if name:
                    params["name"] = name
                if email:
                    params["email"] = is_valid_email(email)
                if pnohe:
                    params["pnohe"] = is_valid_phone(pnohe)
                if address:
                    params["address"] = address
                if params:
                    edits = edit_client(client_id, **params)
                    print(edits)
            elif choise == "3":
                client_id = to_int(input("Введіть ID клієнта: "))
                get_client_orders(client_id)
            elif choise == "4":
                search_clients_menu()
            else:
                print("Немає такого пункту меню, виберіть ще раз:")
                continue
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

def report_menu():
    menu = '\nОберіть меню:, 1-Звіт про склади, 2-Звіт про популярні продукти, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()
        try:
            if choise == "0":
                break
            elif choise == "1":
                get_warehouse_report()
            elif choise == "2":
                get_most_popular_products()
            else:
                print("Немає такого пункту меню, виберіть ще раз:")
                continue
        except Exception as e:
            print(f"Щось пішло не так( {e.__class__}: {e}")

def main_menu():
    menu = 'Оберіть меню:, 1-Управління складами, 2-Управління продуктами, 3-Управління замовленнями, 4-Управління клієнтами, 5-Звітність, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choise = input()

        if choise == "0":
            break
        elif choise == "1":
            warehouse_menu()
        elif choise == "2":
            product_menu()
        elif choise == "3":
            order_menu()
        elif choise == "4":
            client_menu()
        elif choise == "5":
            report_menu()
        else:
            print("Немає такого пункту меню, виберіть ще раз:")
            continue

if __name__ == "__main__":
    main_menu()
