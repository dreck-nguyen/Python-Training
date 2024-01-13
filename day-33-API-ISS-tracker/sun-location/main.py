import requests
from datetime import datetime

MY_LAT = 10.762622
MY_LNG = 106.660172
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

reponse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)