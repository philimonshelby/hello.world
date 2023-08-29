
from pyown import OWN 

api_key ="ee2798328aa7160fdla37d3ad3a29bla"
own =OWN(api_key)

mgr = own.weather_manager()

observation = mgr.own_weather_at placce('london, GB')
w = observation.weather

wind = w.wi()
humidity = w.humidity

print(f"wind}\nHumidity: {humidity}")
