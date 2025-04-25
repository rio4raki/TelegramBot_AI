import requests
import configparser

class SearchWeather:
    def __init__(self):
        self.config = configparser.ConfigParser()
        with open('config.ini', 'r', encoding='utf-8') as f:
            self.config.read_file(f)
        self.api_key = self.config.get('WeatherAPI', 'Key')
        self.city_code = self.config.get('WeatherAPI', 'CityCode')
        self.base_url = 'https://restapi.amap.com/v3/weather/weatherInfo'

    def get_weather(self, city_code, extensions='base'):
        params = {
            'key': self.api_key,
            'city': city_code,
            'extensions': extensions,
            'output': 'JSON'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def get_current_weather(self, city_code):
        data = self.get_weather(city_code, 'base')
        if data['status'] != '1':
            return "天气查询失败，请检查城市代码或API配置"
        live = data['lives'][0]
        return f"实时气温 {live['temperature']}° 天气：{live['weather']} {live['winddirection']}风 {live['windpower']}级 湿度：{live['humidity']}%"

    def get_forecast_weather(self, city_code):
        return self.get_weather(city_code, 'all')