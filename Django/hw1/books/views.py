from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def links(func):
    def wrapper(request: HttpRequest):
        base_links = """
        <hr>
        <a href="/">Головна сторінка</a><br>
        <a href="/books/">Сторінка книг</a><br>
        <a href="/authors/">Сторінка авторів</a><br>
        <a href="/orders/">Сторінка замовлень</a><br><br><br>
        
        <a href="/books/top/">Сторінка топових книг</a><br>
        <a href="/books/free/">Сторінка безкоштовних книг</a><br>
        <a href="/books/top/free/">Сторінка найкращих безкоштовних книг</a><br>
        <a href="/books/oldschool/">Сторінка класичних книг</a><br>        
        <hr>
        """        
        response = func(request)
        return HttpResponse(response.content.decode() + base_links)
    return wrapper

@links
def all_books(request: HttpRequest):
    return HttpResponse("<h1>Список всіх книг</h1>")

@links
def top_books(request: HttpRequest):
    return HttpResponse("<h1>Список топових книг</h1>")

@links
def free_books(request: HttpRequest):
    return HttpResponse("<h1>Список безкоштовних книг</h1>")

@links
def top_free_books(request: HttpRequest):
    return HttpResponse("<h1>Список найкращих безкоштовних книг</h1>")

@links
def oldschool_books(request: HttpRequest):
    return HttpResponse("<h1>Список класичних книг</h1>")
