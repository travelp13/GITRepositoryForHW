from basedb import BaseDBClass

class Warehouse(BaseDBClass):
    __filename = "warehouses"
   
    def __init__(self):
        super().__init__(self.__filename)

    def get_warehouses(self) -> list:
        return self.get_list_data()

    def add_warehouse(self, name:str, address:str, capacity:int):
        self.id = self.get_next_id()
        self.name = name
        self.address = address
        self.capacity = capacity
        self.products = []
        warehouse = self.to_dict()
        self.append_list_data(warehouse)
        self.save_warehouses()
    
    def edit_warehouse(self, warehouse_id:int, **kwargs):
        warehouse = self.find_warehouse_by_id(warehouse_id)
        if warehouse:
            warehouse.update(**kwargs)
            self.save_warehouses()
            return warehouse
        return None
    
    def edit_product_quantity(self, product_id:int, quantity:int):
        for warehouse in self.get_warehouses():
            warehouse_id = warehouse["id"]   
            warehouse_products = self.get_warehouse_products(warehouse_id)
            product = next((p for p in warehouse_products if p.get("id") == product_id), None)
            if product:
                product['quantity'] = quantity
        self.save_warehouses()
    
    def add_product_to_warehouse(self, warehouse_id:int, product_id:int, quantity:int):
        warehouse = self.find_warehouse_by_id(warehouse_id)
        if warehouse:
            warehouse_products = self.get_warehouse_products(warehouse_id)
            warehouse_products.append({'id': product_id, 'quantity': quantity})
        self.save_warehouses()
        
    def delete_product(self, product_id:int):
        for wh in self.get_warehouses():
            for product in self.get_warehouse_products(wh["id"]):
                 if product.get("id") == product_id:
                     self.get_warehouse_products(wh["id"]).remove(product)
        self.save_warehouses()
    
    def save_warehouses(self):
        data = {
            "last_id": self.get_last_id(),
            "warehouses": self.get_warehouses()
        }
        self.save(data)

    def find_warehouse_by_id(self, warehouse_id:int) -> dict:
        return next((d for d in self.get_warehouses() if d.get("id") == warehouse_id), None)
    
    def get_warehouse_products(self, warehouse_id:int) -> list:
        return self.find_warehouse_by_id(warehouse_id).get("products", [])
         
    def get_total_quantity(self, warehouse_id:int) -> int:
        total_quantity = 0
        for product in self.get_warehouse_products(warehouse_id):
            total_quantity += product["quantity"]
        return total_quantity         
    
    def get_free_space(self, warehouse_id:int) -> int:
        warehouse = self.find_warehouse_by_id(warehouse_id)
        if warehouse:
            total_quantity = self.get_total_quantity(warehouse_id)
            return warehouse["capacity"] - total_quantity
        return None
    
    def to_dict(self):
        return self.__dict__