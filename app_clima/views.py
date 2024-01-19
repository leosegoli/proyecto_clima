from django.shortcuts import render
import requests

def index(request):
    return render(request, 'app_clima/index.html')

def clima(request):
    if request.method == 'POST':
        ciudad = request.POST['ciudad']
        api_key = 'c63127b33e8de053debfec4d66ff52fc' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
        response = requests.get(url)
        datos_clima = response.json()

        if response.status_code == 200:
            temperatura = datos_clima['main']['temp']
            descripcion = datos_clima['weather'][0]['description']
            return render(request, 'app_clima/clima.html', {'ciudad': ciudad, 'temperatura': temperatura, 'descripcion': descripcion})
        else:
            mensaje_error = f'Error al obtener datos del clima para {ciudad}.'
            return render(request, 'app_clima/error.html', {'mensaje_error': mensaje_error})

