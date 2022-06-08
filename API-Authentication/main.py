import requests

# YOUR API REQUEST SITE HERE
OWM_Endpoint = "---------------------------------------" #EXAMPLE:"https://api.openweathermap.org/data/2.5/onecall"

# YOUR API KEY HERE
api_key = "-----------------------------------------------------------------------------------------"

weather_params = {
    "lat": 41.008240,  # YOUR LOCATION HERE
    "lon": 28.978359,  # YOUR LOCATION HERE
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_hourly = weather_data["hourly"]
weather_slice = weather_hourly[:12]

is_rainy = False

for i in weather_slice:
    conditon_code = int(i['weather'][0]["id"])
    if 600 < conditon_code < 800:
        is_rainy = True

if is_rainy:
    print("Take umbrella")
else:
    print("dont take umbralle")

# OLD METHOD
# for i in range(0, 12):
#     if 600 < weather_hourly[i]['weather'][0]["id"] < 800:
#         print("take umbrella")
#     print(weather_hourly[i]['weather'][0]["main"])
