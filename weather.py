

import  requests
API_KEY = "13a4e8c5b5bafeefd7cda87477f8d013"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city name: ")
request_URL = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_URL)

if (response.status_code == 200):
    data = response.json()

    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15,2)

    print("Weather: ",weather.capitalize())
    print("Temperature: ", temperature, " Celcius")

else:
    print("Enter a different city name!")



