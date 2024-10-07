from basedb import BaseDBClass


class Order(BaseDBClass):
    __filename = "orders"
    __statuses = {1 : "New", 2 : "Confirmed", 3 : "Sent", 4 : "Delivered", 5 : "Cancelled"}
   
    def __init__(self):
        super().__init__(self.__filename)

    def get_orders(self):
        return self.get_list_data()

    def add_order(self, client_id:int, products: list) -> float:
        self.id = self.get_next_id()
        self.client_id = client_id
        self.products = products
        self.total_amount = self.get_total_amount(products)
        self.status = "New"
        order = self.to_dict()
        self.append_list_data(order)
        self.save_orders()

    @staticmethod
    def get_total_amount(products: list):        
        total_amount = 0
        for product in products:
            total_amount += product["price"]*product["quantity"]
        return total_amount
    
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

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def print_orders(orders:list) -> str:
        for order in orders:
            for key, value in order.items():
                print(f"{key}: {value}")
            print("\n")