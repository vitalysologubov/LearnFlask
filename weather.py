import requests


def weather_by_city(city_name):
    """Получение данных о погоде через api"""

    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '3ed5e69458684dfb99d182659201509',
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }

    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
        weather = result.json()

        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError) as error:
                    print(f'Ошибка получения погоды: {error}.')
                    return False
    except (requests.RequestException, ValueError):
        return False

    return False
