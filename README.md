# 🌤️ Telegram Weather Alert Bot

An automated Python script that monitors real-time weather conditions using WeatherAPI and sends instant alerts to a Telegram Bot whenever the weather condition changes or rain is detected. Automatically scheduled and hosted via GitHub Actions.

---

## 🚀 Features

* 📡 Live Monitoring: Fetches real-time weather data for specified coordinates.
* 🧠 Smart Caching: Tracks condition changes using a local last_code.txt cache file to prevent duplicate spam messages.
* 📩 Telegram Notifications: Sends instant notifications directly to your phone.
* ⏰ Automated Scheduling: Runs continuously on a background interval via GitHub Actions.

---

## 🛠️ Tech Stack

* Language: Python 3.11+
* APIs Used: WeatherAPI, Telegram Bot API
* Libraries: requests
* Automation: GitHub Actions

---

## ⚙️ Environment Secrets

To run this project locally or on GitHub Actions, you need to set up the following keys:

| Key | Description |
| :--- | :--- |
| BOT_TOKEN | Your Telegram Bot token from @BotFather |
| CHAT_ID | Your Telegram personal/chat ID |
| WEATHER_API_KEY | API Key from WeatherAPI.com |

---

## 💻 Local Setup

1. Clone the repository:
   `bash
   git clone [https://github.com/your-username/my_weather_alert.git](https://github.com/your-username/my_weather_alert.git)
   cd my_weather_alert