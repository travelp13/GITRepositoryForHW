from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpRequest

def index(request: HttpRequest, city:str):
    weather_data = {}
    api_key = '6061bf4e0eeb5494490640b1bb75fb21'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
    else:
        weather_data = {'error': 'City not found'}
    
    context = {
        'weather': weather_data
    }

    return render(request, 'weather_app/index.html', context)
