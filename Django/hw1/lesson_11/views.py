from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def lesson_1_1(request: HttpRequest):
    return HttpResponse("""
        <p>Hello World!</p>
        <p>Django є одним з найбільших framework на Python</p>
        <hr>
    """)

def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello World!</h1>")