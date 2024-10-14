# Task1
# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
class MyIterable:
    def __init__(self, value: list):
        self.value = value

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.value):
            raise StopIteration
        else:
            result = self.value[self.index]
            self.index += 1
            return result           
        
my_iterable = MyIterable([1, 2, 3, 4, 5])
for item in my_iterable:
    print(item)

# Task2
# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, 
# додавши методи очищення списку, додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

# Рішення - було додано три нові методи add(), del_(), clear() в іншому клас не змінювався
# Перед початком бажано запустити відладку, для розуміння що зберігається у змінних класу MyList
class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)
    
    #було додано до класу:
    def add(self, new_element: any, new_index : int = None):      
        # Додаємо в кінець якщо індекс не заданий
        if new_index == self._length or new_index == None: 
            self.append(new_element)
            return
        
        # Перевірка на правильність індексу
        if new_index < 0 or new_index > self._length:
            raise IndexError("Індекс списку поза діапазоном")
        
        # Додаємо елемент на потрібну позицію, якщо вона задана
        # Створення елемента списку
        new_node = MyList._ListNode(new_element)

        # Знаходимо поточний елемент (old_node) на цій позиції (будемо рухати його вправо)
        old_node = self._head
        for _ in range(new_index):
            old_node = old_node.next
        
        # Для нового елемента задаємо попередній та наступний елементи
        new_node.next = old_node
        new_node.prev = old_node.prev
        
        if old_node.prev is not None:
            # Якщо новий елемент додається не на початок списку
            # то для попереднього елемента у списку змінюємо елемент на наш новий
            old_node.prev.next = new_node
        else:
            # Інакше оновлюємо перший елемент списку на наш
            self._head = new_node
        
        # Для старого елемента на цій позиції підміняємо попередній елемент на наш новий
        old_node.prev = new_node

        # Змінюємо довжину списку
        self._length += 1

    # Логіка така ж як у add тільки навпаки
    def del_(self, index: int =None):        
        if self._length == 0:
            raise IndexError("Порожній лист")
                
        if index is None:
            index = self._length - 1

        if index < 0 or index >= self._length:
            raise IndexError("Індекс списку поза діапазоном")
        
        # Знаходимо поточний елемент (del_node) на цій позиції (наступні будемо рухати на його місце ліворуч)
        del_node = self._head
        for _ in range(index):
            del_node = del_node.next
            
        # Для попереднього елемента змінюємо значення наступного
        if del_node.prev is not None:
            del_node.prev.next = del_node.next
        else:
            self._head = del_node.next

        # Для наступного елемента змінюємо значення попереднього
        if del_node.next is not None:
            del_node.next.prev = del_node.prev
        else:
            self._tail = del_node.prev

        # Змінюємо довжину списку
        self._length -= 1
        # Повертаємо змінений список
        return del_node.value

    # Очищаємо скинувши змінні
    def clear(self):
        self._head = self._tail = None
        self._length = 0

def main():
    my_list = MyList([1, 2, 3, 4, 5])
    print("add")
    print("Початковий список:\n", my_list)    
    my_list.add(new_element=100, new_index= 2)
    print("Після вставки new_element=100, new_index= 2:\n", my_list)
    my_list.add(new_element="Hello", new_index= 0)
    print("Після вставки: new_index= 0, new_element=Hello:\n", my_list)
    my_list.add(new_element=13)
    print("Після вставки: new_element=13:\n", my_list)

    my_list = MyList([1, 2, 3, 4, 5, 6, 7, 8])
    print("\n\ndel_")
    print("Початковий список:\n", my_list)
    my_list.del_(3)  
    print("Після видалення 3 елемента:\n", my_list)
    my_list.del_()  
    print("Після видалення останнього елемента:\n", my_list)
    my_list.del_(0)  
    print("Після видалення 0 елемента:\n", my_list)

    print("\n\nclear")
    my_list.clear()
    print("Після очищення:", my_list)

main()

# # Task3
# # Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
class MyReverse:
    def __init__(self, value: list):
        self.value = value

    def __iter__(self):
        self.index = len(self.value)
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.value[self.index]

my_list = [1, 2, 3, 4, 5]
reverse_list = MyReverse(my_list)

for item in reverse_list:
    print(item)

# Task4
# Ітератор для розбору словника
# Напиши ітератор, який буде перебирати словник певної структури. 
# Словник містить категорії товарів, де кожна категорія — це ключ, а значенням є список товарів у цій категорії. 
# Ітератор повинен повертати назву категорії та окремо кожен товар з цієї категорії.
# Приклад словника: products = {
#     "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
#     "Одяг": ["Футболка", "Джинси", "Куртка"],
#     "Книги": ["Роман", "Фентезі", "Наукова література"]}
class MyProductIterator:
    def __init__(self, products: dict):
        self.products = products
        
    def __iter__(self):
        #dict products to list of tuple
        self.items = [(key, value) for key, values in self.products.items() for value in values]
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        else:
            category, item = self.items[self.index]
            self.index += 1
            return category, item

products = {
    "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
    "Одяг": ["Футболка", "Джинси", "Куртка"],
    "Книги": ["Роман", "Фентезі", "Наукова література"]
}

products_iter = MyProductIterator(products)

for category, item in products_iter:
    print(f"Категорія: {category}, Товар: {item}")

# Task5
# Бібліотека книг та авторів
# Опис завдання:
# Створи класову структуру для керування бібліотекою. Має бути два основних класи: Author та Book. 
# Клас Author представляє автора з його іменем і списком книг, а клас Book представляє окрему книгу з її назвою.
# Додатково, бібліотека повинна використовувати ітератори для зручної навігації та перегляду книг кожного автора.
# Задача:
# Створи клас Library, який міститиме списки книг та авторів.
# Реалізуй методи для додавання книг та авторів.
# Використовуй ітератор для перебору книг кожного автора.
# Також реалізуйте меню для виклуку кожної лдосутпної операції
class Book:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title

class Author:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.library = {}

    def add_author(self, author: Author):
        self.author_name = str(author)
        if self.author_name not in self.library:
            self.library[self.author_name] = set()

    def add_book(self, author_name: Author, book_title: Book):
        self.add_author(author_name)
        self.book_title = str(book_title)
        self.library[self.author_name].add(self.book_title)

    def __iter__(self):
        #dict products to list of tuple
        self.items = ([(author, book) for author, books in self.library.items() for book in books])
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        else:
            author, book = self.items[self.index]
            self.index += 1
            return author, book
    
    def list_authors(self):
       for author, book in self:
           print (f"Автор: {author} Книга: {book}" )
       
def main():
    library = Library()

    menu = 'Оберіть меню:, 1-Додати автора, 2-Додати книгу, 3-Переглянути авторів та їхні книги, 0-Вихід, '
        
    while True:
        print(("\n  ").join(menu.split(", ")))
        choice = input().strip()

        if choice == '0':
            break

        elif choice == '1':
            author = Author(input("Введіть ім'я автора: "))
            library.add_author(author)
            print(f"Автор '{author}' доданий.")

        elif choice == '2':
            author = Author(input("Введіть ім'я автора: "))
            book = Book(input("Введіть назву книги: "))
            library.add_book(author, book)
            print(f"Книга '{book}' автора '{author}' додана.")

        elif choice == '3':
            print("Список авторів та їх книг:")
            library.list_authors()   

        else:
            print("Невірний вибір, спробуйте ще раз.")

main()