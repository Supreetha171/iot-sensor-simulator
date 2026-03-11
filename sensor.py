import random
import time
import requests

API_KEY = "AU12KG77XGOND4A7"

while True:
    temperature = random.randint(20,35)
    humidity = random.randint(40,80)

    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperature}&field2={humidity}"

    requests.get(url)

    print("Sent -> Temp:", temperature, "Humidity:", humidity)

    time.sleep(15)
