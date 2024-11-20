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
        
        <a href="/orders/done/">Сторінка виконаних замовлень</a><br>
        <a href="/orders/canceled/">Сторінка скасованих замовлень</a><br>        
        <hr>
        """        
        response = func(request)
        return HttpResponse(response.content.decode() + base_links)
    return wrapper

@links
def all_orders(request):
    return HttpResponse("<h1>Список всіх замовлень</h1>")

@links
def done_orders(request):
    return HttpResponse("<h1>Список виконаних замовлень</h1>")

@links
def canceled_orders(request):
    return HttpResponse("<h1>Список скасованих замовлень</h1>")
