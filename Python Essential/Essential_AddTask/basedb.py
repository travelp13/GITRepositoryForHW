import os, json

class BaseDBClass:
    __filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),f"Data\\")
    __permitted_filenames = ["warehouses", "products", "orders", "clients"]
    __list_data = []
    __last_id = 0
    __filename = ''

    def __init__(self, filename) -> None:
        if not self.__list_data:
            self.set_filename(filename)
            data = self.load()
            self.set_list_data(data.get(f"{self.__filename}", []))
            self.set_last_id(data.get("last_id", 0))

    @classmethod
    def set_last_id(cls, id: int):
        cls.__last_id = id

    @classmethod
    def set_list_data(cls, list_data: dict):
        cls.__list_data = list_data

    @classmethod
    def set_filename(cls, filename: str):
        if filename not in cls.__permitted_filenames:            
            raise ValueError("Unknown data file")
        else:
            cls.__filename = filename
    
    @classmethod
    def append_list_data(cls, data: dict):
        cls.__list_data.append(data)

    @classmethod
    def get_last_id(cls):
        return cls.__last_id

    @classmethod
    def get_next_id(cls):
        cls.__last_id += 1
        return cls.__last_id  

    @classmethod
    def get_list_data(cls):
        return cls.__list_data
    
    @classmethod
    def save(cls, data):
        with open(os.path.join(cls.__filepath,f"{cls.__filename}.json"), 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=True)

    @classmethod    
    def load(cls):
        try:
            with open(os.path.join(cls.__filepath,f"{cls.__filename}.json"), 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = dict()
            cls.save(data)
        return data