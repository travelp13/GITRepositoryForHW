from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def home(request: HttpRequest):
    return HttpResponse("""
        <h1>Головна сторінка</h1>
        <a href="/books/">Сторінка книг</a><br>
        <a href="/authors/">Сторінка авторів</a><br>
        <a href="/orders/">Сторінка замовлень</a>
    """)
