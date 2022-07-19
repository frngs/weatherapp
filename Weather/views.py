import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid= "db90e87ad8b37a955590a09721877dd9"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" +appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities= City.objects.all()

    all_cities = []

    try:
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            city_info={
                'city': city.name,
                'temp': res["weather"][0]["icon"]
            }
            all_cities.append(city_info)
    except KeyError:
        pass


    context={'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
