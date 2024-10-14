import shelve, os

class LinkHandler:
    def __init__(self, path: str):
        self.path = path

    def add_link(self, original_link: str, short_name: str):
        with shelve.open(self.path) as db:
            if short_name in db:
                return False, "Ця коротка назва вже використовується"
            else:
                db[short_name] = original_link
                return True, f"Посилання '{original_link}' було скорочене до '{short_name}'"

    def get_original_link(self, short_name: str):
        with shelve.open(self.path) as db:
            if short_name in db:
                return True, db[short_name]
            else:
                return False, "Коротка назва не знайдена"
