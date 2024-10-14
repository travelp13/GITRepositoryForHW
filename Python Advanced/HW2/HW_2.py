# Task1
# Вивчіть основні поняття, розглянуті в уроці, а також особливості роботи з HTTP-протоколами в Python, використовуючи бібліотеки urllib та requests.
import urllib.request
import requests

url = 'https://google.com.ua'

# Відправка GET-запиту
response = urllib.request.urlopen(url)
# Читання відповіді
data = response.read()
# Виведення отриманих даних
print(data)


# Відправка GET-запиту
response = requests.get(url)
# Отримання статусу запиту
print(response.status_code)
# Отримання тексту відповіді
print(response.text)


# Task6
# Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та обробити відповіді. 
# Необхідно попрактикуватися з urllib та бібліотекою requests. Рекомендується спочатку спробувати виконати запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests.
import urllib.request
import urllib.parse

def urllib_get(url):
    with urllib.request.urlopen(url) as response:
        status_code = response.getcode()
        headers = response.getheaders()
        body = response.read().decode('utf-8')
        
        print(f"GET Запит: {url}")
        print(f"Статус-код: {status_code}")
        print("Заголовки:")
        for header in headers:
            print(f"  {header[0]}: {header[1]}")
        print("Тіло відповіді:")
        print(body)

def urllib_post(url, data):
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_encoded)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        headers = response.getheaders()
        body = response.read().decode('utf-8')
        
        print(f"POST Запит: {url}")
        print(f"Статус-код: {status_code}")
        print("Заголовки:")
        for header in headers:
            print(f"  {header[0]}: {header[1]}")
        print("Тіло відповіді:")
        print(body)

url_get = "https://jsonplaceholder.typicode.com/posts"
urllib_get(url_get)

url_post = "https://jsonplaceholder.typicode.com/posts"
data_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
urllib_post(url_post, data_post)


import requests

def requests_get(url):
    response = requests.get(url)
    print(f"GET Запит: {url}")
    print(f"Статус-код: {response.status_code}")
    print("Заголовки:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    print("Тіло відповіді:")
    print(response.text)

def requests_post(url, data):
    response = requests.post(url, data=data)
    print(f"POST Запит: {url}")
    print(f"Статус-код: {response.status_code}")
    print("Заголовки:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    print("Тіло відповіді:")
    print(response.text)

url_get = "https://jsonplaceholder.typicode.com/posts"
requests_get(url_get)

url_post = "https://jsonplaceholder.typicode.com/posts"
data_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
requests_post(url_post, data_post)


# Task8
# Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний). 
# Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та друкувати на консоль статус-код, заголовки та тіло відповіді.
import requests

def http_client(url, method, data=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=data)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data)
        else:
            print(f"Невідомий метод: {method}. Використовуйте 'GET' або 'POST'.")
            return

        print(f"Статус-код: {response.status_code}")
        print("Заголовки:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print("Тіло відповіді:")
        print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка: {e}")

url = "https://jsonplaceholder.typicode.com/posts"
method = "GET"
http_client(url, method)

url_post = "https://jsonplaceholder.typicode.com/posts"
method_post = "POST"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
http_client(url_post, method_post, data)
