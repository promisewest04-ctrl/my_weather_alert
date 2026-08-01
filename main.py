import time

import requests
import os

BOT_TOKEN = os.environ.get("BOT")
CHAT_ID = os.environ.get("CHAT_ID")

WEATHER_API_KEY = os.environ.get("WA_API_KEY")
api_url = "http://api.weatherapi.com/v1/current.json?"

params = {
    "key": WEATHER_API_KEY,
    "q": "4.8100, 6.9600"
}

RAIN_CODE = [
    1240, 1063, 1180, 1183, 1186, 1189, 1192, 1195, 1243, 1246, 1273, 1276
]
CACHE_FILE = "last_code.txt"

def get_last_code():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as r:
            content = r.read().strip()
            if content.isdigit():
                return int(content)
    return None


def save_current_code(num):
    with open(CACHE_FILE, "w") as f:
        f.write(str(num))

def telegram_alert(message_alert):
    url = f"https://api.telegram.org/bot{BOT}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message_alert
    }
    res = requests.post(url=url, json=payload)
    print(f"Message sent successfully!!")

def check_weather():
    try:
        response = requests.get(api_url, params=params)

        """Getting the rain code for the current time and knowing it forecast"""
        code = response.json()['current']['condition']
        current_code = code['code']

        last_code = get_last_code()

        if current_code != last_code:
            print(f"Weather condition change from {last_code} to {code['code']}")
            if current_code in RAIN_CODE:
                telegram_alert(code['text'])
            else:
                telegram_alert(code['text'])
            save_current_code(current_code)
        else:
            telegram_alert(f"No weather change. still {code['text']}")
    except Exception as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    print("Starting continuous weather monitoring")

    CHECK_INTERVAL = 300

    while True:
        check_weather()
        time.sleep(CHECK_INTERVAL)



