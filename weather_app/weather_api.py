import requests

def get_weather_data(city_name):
    api_key = '4d9c618d771fa4ae35ec552478ee6861'  # Zastąp 'your_api_key' własnym kluczem API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=pl'
    response = requests.get(url)
    data = response.json()
    return data

