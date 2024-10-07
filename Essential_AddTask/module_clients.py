from basedb import BaseDBClass

class Client(BaseDBClass):
    __filename = "clients"
   
    def __init__(self):
        super().__init__(self.__filename)

    def get_clients(self):
        return self.get_list_data()

    def add_client(self, name:str, email:str, phone:str, address:str):
        self.id = self.get_next_id()
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        client = self.to_dict()
        self.append_list_data(client)
        self.save_clients()

    def edit_client(self, client_id, **kwargs):
        client = self.find_client_by_id(client_id)
        if client:
            client.update(**kwargs)
            self.save_clients()
            return client
        return None
    
    def save_clients(self):
        data = {
            "last_id": self.get_last_id(),
            "clients": self.get_clients()
        }
        self.save(data)

    def find_client_by_id(self, client_id):
        return next((d for d in self.get_clients() if d.get("id") == client_id), None)
    
    def search_clients(self, **kwargs):
        result = self.get_clients()
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
    def print_clients(clients:list) -> str:
        for client in clients:
            for key, value in client.items():
                print(f"{key}: {value}")
            print("\n")
