import requests
import pandas as pd

def get_weather_data(lat, lon):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&daily=temperature_2m_max,precipitation_sum"
        f"&timezone=auto"
    )

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temperature": data["daily"]["temperature_2m_max"],
        "precipitation": data["daily"]["precipitation_sum"]
    })

    return df