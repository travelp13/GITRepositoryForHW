from basedb import BaseDBClass


class Order(BaseDBClass):
    __filename = "orders"
    __statuses = {1 : "New", 2 : "Confirmed", 3 : "Sent", 4 : "Delivered", 5 : "Cancelled"}
   
    def __init__(self):
        super().__init__(self.__filename)

    def get_orders(self):
        return self.get_list_data()

    def add_order(self, client_id:int, products: list) -> float:
        id = self.get_next_id()
        total_amount = self.get_total_amount(products)
        order = self.to_dict(id, client_id, products, total_amount)
        self.append_list_data(order)
        self.save_orders()
        return total_amount

    @staticmethod
    def get_total_amount(products: list):        
        total_amount = 0
        for product in products:
            total_amount += product["price"]*product["quantity"]
        return round(total_amount,2)
    
    @classmethod
    def get_status_by_id(cls, status):
        if len(cls.__statuses) >= status:
            return cls.__statuses[status]
        
    def change_status(self, order_id:int, status:int):
        new_status = self.__statuses[status]
        order = self.find_order_by_id(order_id)
        if order and new_status:
            order['status'] = new_status
            self.save_orders()

    def get_order_products(self, order_id:int) -> list:
        return self.find_order_by_id(order_id).get("products", [])

    def save_orders(self):
        data = {
            "last_id": self.get_last_id(),
            "orders": self.get_orders()
        }
        self.save(data)

    def find_order_by_id(self, order_id):
        return next((d for d in self.get_orders() if d.get("id") == order_id), None)
    
    def search_orders(self, **kwargs):
        result = self.get_orders()
        for key, value in kwargs.items():
            if isinstance(value, str):
                value = value.upper()
                result = [d for d in result if isinstance(d.get(key), str) and value in d.get(key).upper()]
            else:
                result = [d for d in result if d.get(key) == value]
        return result
    
    def to_dict(self, id:int, client_id:int, products: list, total_amount: float):
        return {
            "id": id,
            "client_id": client_id,
            "products": products,
            "total_amount": total_amount,
            "status": "New"
        }
    
    @staticmethod
    def print_orders(orders:list) -> str:
        for order in orders:
            for key, value in order.items():
                print(f"{key}: {value}")
            print("\n")