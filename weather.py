import requests

def get_weather(city="Delhi"):
    try:
        # free API (no key needed for simple demo version)
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)

        print("\n🌦️ Weather Update:")
        print(response.text)

    except Exception as e:
        print("Weather fetch failed:", e)