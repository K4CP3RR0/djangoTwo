from weather_api import get_weather_data

def display_weather_data(weather_data):
    # Wyświetl dane pogodowe w przyjazny dla użytkownika sposób
    print('Informacje pogodowe:')
    print('---------------------')
    print(f'Miasto: {weather_data["name"]}')
    print(f'Temperatura: {weather_data["main"]["temp"]} C')
    print(f'Wilgotność: {weather_data["main"]["humidity"]} %')
    print(f'Ciśnienie: {weather_data["main"]["pressure"]} hPa')
    print(f'Opis pogody: {weather_data["weather"][0]["description"]}')

def main():
    city_name = input('Podaj miasto: ')
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()