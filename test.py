import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)
city = input("天気を調べたい都市を入力してください。 例：一関市 ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ja&units=metric"

response = requests.get(url)
print(response)

if response.status_code == 200:
    weather_data = response.json()
    print(weather_data['weather'][0]['main'])
    print(weather_data['weather'][0]['description'])
    print(f"{weather_data['main']['temp']}℃")

else:
    print("データを取得できませんでした")
    print(response.text)

