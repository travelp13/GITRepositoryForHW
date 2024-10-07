from basedb import BaseDBClass

class Product(BaseDBClass):
    __filename = "products"
   
    def __init__(self):
        super().__init__(self.__filename)

    def get_products(self):
        return self.get_list_data()

    def add_product(self, name:str, category:str, price:float, quantity:int, description:str) -> int:
        id = self.get_next_id()
        product = self.to_dict(id, name, category, price, quantity, description)
        self.append_list_data(product)
        self.save_products()
        return id
    
    def edit_product(self, product_id:int, **kwargs):
        product = self.find_product_by_id(product_id)
        if product:
            product.update(**kwargs)
            self.save_products()
            return product
        return None

    def delete_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            self.get_products().remove(product)
            self.save_products()
            return True
        return False

    def save_products(self):
        data = {
            "last_id": self.get_last_id(),
            "products": self.get_products()
        }
        self.save(data)

    def find_product_by_id(self, product_id) -> dict:
        return next((d for d in self.get_products() if d.get("id") == product_id), None)
    
    def search_products(self, **kwargs):
        result = self.get_products()
        for key, value in kwargs.items():
            if isinstance(value, str):
                value = value.upper()
                result = [d for d in result if isinstance(d.get(key), str) and value in d.get(key).upper()]
            else:
                result = [d for d in result if d.get(key) == value]
        return result

    def to_dict(self, id:int, name:str, category:str, price:float, quantity:int, description:str):
        return {
            "id": id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "description": description
        }
    
    @staticmethod
    def print_products(products:list) -> str:
        for product in products:
            for key, value in product.items():
                print(f"{key}: {value}")
            print("\n")