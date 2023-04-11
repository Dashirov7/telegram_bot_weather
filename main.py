import requests
from pprint import pprint
from config import open_weather_token



def get_weather(city, open_weather_token):

    try:
        r=requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}"
        )

        data=r.json()
        #pprint(data)

        city=data["name"]
        cur_weather=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
       # cloudiness = data["main"]["cloudiness"]


        print[f"Погода в городе: {city}\n температура: {cur_weather}\n влажность: {humidity}\n" \
              f"скорость ветра: {wind}\n "]

    except Exception as ex:

         print(ex)
         print("Проверьте название города")

def main():

    city=input("Введите город")
    get_weather(city,open_weather_token)

if __name__=='__main__':
    main()

