from django.shortcuts import render
import requests, json
from django.http import HttpResponse

def index(request):
    url = 'http://localhost:5000/'

    try:

        if request.method == 'POST':
            lat = request.POST['lat']
            long = request.POST['long']
            req_data = request.POST.dict()

            temps = []
            if req_data.get('noaa'):
                r = requests.get(url + f'noaa?latlon={lat},{long}')
                data = r.json()
                temps.append(data['today']['current']['fahrenheit'])

            if req_data.get('wdc'):
                r = requests.post(url + f'weatherdotcom', json={"lat":33.3,"lon":44.4})
                data = r.json()
                temps.append(data['query']['results']['channel']['condition']['temp'])

            if req_data.get('accu'):
                r = requests.get(url + f'accuweather?latitude={lat}&longitude={long}')
                data = r.json()
                temps.append(data['simpleforecast']['forecastday'][0]['current']['fahrenheit'])

            total = 0
            for temp in temps:
                total += int(temp)

            avg_temp = (total/len(temps))

            weather = {
                'temperature' : avg_temp
            }
            context = {'weather': weather}

            return render(request, 'weather/index.html', context=context)
    except:
        return HttpResponse('Invalid Input!')
    return render(request, 'weather/index.html')
