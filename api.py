import requests

def get_weather(latitude, longitude):
    # Fetch current weather data from Open-Meteo
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities using their coordinates
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

# Added coordinates for Nigerian cities
abuja_temp = get_weather(9.06, 7.50)   # Abuja: 9.06° N, 7.50° E
lagos_temp = get_weather(6.45, 3.39)   # Lagos: 6.45° N, 3.39° E

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")         
print(f"Abuja: {abuja_temp}°C")         
print(f"Lagos: {lagos_temp}°C")         
