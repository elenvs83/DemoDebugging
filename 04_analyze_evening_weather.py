# Данные пришли от внешнего сервиса погоды
weather_response = {
    "city": "Da Nang",
    "forecast": {
        "morning": {"temp": 26, "condition": "Sunny"},
        "day": {"temp": 32, "condition": "Cloudy"},
        "evening": {"condition": "Rainy"}
    }
}


def analyze_evening_weather(data: dict) -> str:
    evening_temp = data["forecast"]["evening"]["temp"]

    if evening_temp > 25:
        return "Вечер будет теплым"
    return "Будет прохладно"


status = analyze_evening_weather(weather_response)
print(status)