class Report():
    def __init__(self, warehouse: object, product: object, order: object) -> None:
        self.warehouse = warehouse
        self.product = product
        self.order = order

    def get_warehouse_report(self):        
        for wh in self.warehouse.get_warehouses():
            warehouse_id = wh["id"]
            products_quantity = self.warehouse.get_total_quantity(warehouse_id)
            free_space = self.warehouse.get_free_space(warehouse_id)
            print(f"Id: {wh["id"]}\nName: {wh["name"]}\nAddress: {wh["address"]}\nCapacity: {wh["capacity"]}")
            print (f"Total quantity: {products_quantity}\nFree space: {free_space}\nProducts:")
            for prod in self.warehouse.get_warehouse_products(warehouse_id):
                print (f"  - {self.product.find_product_by_id(prod["id"])["name"]} - {prod["quantity"]} units")
            print("\n")
    
    def get_most_popular_products(self):
        products = {}
        for order in self.order.get_orders():
            if order["status"] == "Delivered":
                for product in order["products"]:
                    product_name = product["name"]
                    product_quantity = product["quantity"]
                    if product_name in products:
                        products[product_name] += product_quantity
                    else:
                        products[product_name] = product_quantity

        sorted_products = dict(sorted(products.items(), key=lambda item: item[1], reverse=True))
        for product, count in sorted_products.items():
            print(f"{product} - {count}")