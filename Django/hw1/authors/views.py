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
        
        <a href="/authors/top/">Сторінка топових авторів</a><br>
        <a href="/authors/ukraine/">Сторінка українських авторів</a><br>
        <a href="/authors/usa/">Сторінка американських авторів</a><br>
        <a href="/authors/top/ukraine/">Сторінка найкращих українських авторів</a><br>        
        <hr>
        """        
        response = func(request)
        return HttpResponse(response.content.decode() + base_links)
    return wrapper

@links
def all_authors(request: HttpRequest):
    return HttpResponse("<h1>Список всіх авторів</h1>")

@links
def top_authors(request: HttpRequest):
    return HttpResponse("<h1>Список топових авторів</h1>")

@links
def ukrainian_authors(request: HttpRequest):
    return HttpResponse("<h1>Список українських авторів</h1>")

@links
def american_authors(request: HttpRequest):
    return HttpResponse("<h1>Список американських авторів</h1>")

@links
def top_ukrainian_authors(request: HttpRequest):
    return HttpResponse("<h1>Список найкращих українських авторів</h1>")