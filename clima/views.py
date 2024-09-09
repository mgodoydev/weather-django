import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import WeatherQuery

# Create your views here.

def get_weather(city):
    api_key = settings.OPENWEATHER_API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    try:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.json()
    except ValueError:
        # Si la respuesta no es JSON, maneja el error
        return None
    
    if data.get('cod') == 200:
        weather = {
            'city': data['name'],
            'temperature': float(data['main']['temp']),
            'description': data['weather'][0]['description']
        }
        # Crear una nueva entrada en la base de datos
        WeatherQuery.objects.create(
            city=weather['city'],
            temperature=weather['temperature'],
            description=weather['description']
        )
        
        return weather
    else:
        return None

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        return redirect('weather_results', city=city)
    return render(request, 'index.html')

def weather_results(request, city):
    weather = get_weather(city)  # Llama a la función que obtiene el clima
    return render(request, 'weather_results.html', {'weather': weather})
