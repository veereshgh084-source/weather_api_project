# import requests
# city=input("Enter city name ;   ")
# url="https://geocoding-api.open-meteo.com/v1/search"                                #API ENDPOINT
# params={                                                                            #SENDS CITY NAMES AS QUERY PARAMETERS
#     "name":city,
#     "count":1,
#     "language":"en",
#     "format":"json"
# }
# response=requests.get(url,params=params)
# data=response.json()
# print(data)



import requests
city=input("enter city name :     ")
geo_url="https://geocoding-api.open-meteo.com/v1/search"
geo_params={
    "name":city,
    "count":1,
    "language":"en",
    "format":"json"
}
geo_response=requests.get(geo_url,params=geo_params)
geo_data=geo_response.json()

latitude=geo_data["results"][0]["latitude"]
longitude=geo_data["results"][0]["longitude"]

weather_url="https://api.open-meteo.com/v1/forecast"
weather_params={
    "latitude":latitude,
    "longitude":longitude,
    "current":"temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
}

weather_response=requests.get(weather_url,params=weather_params)
weather_data=weather_response.json()
current=weather_data["current"]         # WE STORE THE CURRENT DICT IN A VARIABLE
print("\n CURRENT WEATHER")
print("------------------")
print(f"city :  {city}\nTEMP :  {current["temperature_2m"]}C\nHUMIDITY : {current["relative_humidity_2m"]}\nWINDSPEED:  {current["wind_speed_10m"]}\nWTH CODE :  {current["weather_code"]}")