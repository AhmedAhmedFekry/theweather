from django.shortcuts import render
import requests
# Create your views here.
url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'cairo'


def index(request):
    apikey = url + city
    response = requests.get(apikey)
    content = response.json()
    city_weather = {
        'temperature': content['main']['temp'],
        'description': content['weather'][0]['description'],
        'icon': content['weather'][0]['icon'],
    }
    return render(request, 'weather.html', {
        'city_weather': city_weather,
        'city': city
    })
