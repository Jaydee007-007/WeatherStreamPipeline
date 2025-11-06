import requests
import time
import pandas as pd
from kafka import KafkaProducer
from json import dumps


def kafka_producer():
    producer = KafkaProducer(bootstrap_servers=['18.234.23.127:9116'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))

    API_KEY = ""  # MY API key
    cities = ["New York", "Los Angeles", "Miami"]

    t_end = time.time() + 60 * 1
    while time.time() < t_end:
        df_stream = pd.DataFrame(columns=["City", "Temperature", "Timestamp"])
        new_rows = []

        for city in cities:
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {'q': city, 'appid': API_KEY, 'units': 'imperial'}
            response = requests.get(url, params=params)
            weather = response.json()

            new_row = {
                "City": city,
                "Temperature": weather['main']['temp'],
                "Timestamp": time.time()
            }
            new_rows.append(new_row)

        if new_rows:
            df_stream = pd.concat([df_stream, pd.DataFrame(new_rows)], ignore_index=True)

        producer.send('WeatherData', value=df_stream.to_json())
        time.sleep(1)

    print("done producing")


kafka_producer()
