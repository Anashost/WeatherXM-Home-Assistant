"""WeatherXM Constants."""
DOMAIN = "weatherxm"
CONF_STATION_ID = "station_id"
CONF_DEVICE_INDEX = "device_index"

API_URL = "https://api.weatherxm.com/api/v1/cells/{}/devices"

ATTR_TEMPERATURE = "temperature"
ATTR_FEELS_LIKE = "feels_like"
ATTR_HUMIDITY = "humidity"
ATTR_ICON = "icon"
ATTR_PRECIPITATION = "precipitation"
ATTR_PRECIPITATION_ACCUMULATED = "precipitation_accumulated"
ATTR_PRESSURE = "pressure"
ATTR_UV_INDEX = "uv_index"
ATTR_WIND_DIRECTION = "wind_direction"
ATTR_WIND_GUST = "wind_gust"
ATTR_WIND_SPEED = "wind_speed"

SENSOR_TYPES = {
    "temperature": ("Temperature", "°C", "temperature"),
    "feels_like": ("Feels Like", "°C", "temperature"),
    "humidity": ("Humidity", "%", "humidity"),
    "pressure": ("Pressure", "hPa", "pressure"),
    "wind_speed": ("Wind Speed", "m/s", None),
    "wind_gust": ("Wind Gust", "m/s", None),
    "wind_direction": ("Wind Direction", "°", None),
    "wind_direction_cardinal": ("Wind Direction Cardinal", None, None),
    "precipitation": ("Precipitation", "mm/h", "precipitation_intensity"),
    "precipitation_accumulated": ("Daily Precipitation", "mm", "precipitation"),
    "uv_index": ("UV Index", None, None),
    "condition": ("Condition", None, None),
    "icon": ("Icon", None, None),
    "icon_color": ("Icon Color", None, None),
}

CONDITION_MAP = {
    "partly-cloudy-night": ("Partly cloudy", "mdi:weather-night-partly-cloudy", "blue-grey"),
    "partly-cloudy-day": ("Partly cloudy", "mdi:weather-partly-cloudy", "white"),
    "cloudy-night": ("Cloudy", "mdi:weather-night-partly-cloudy", "blue-grey"),
    "cloudy-day": ("Cloudy", "mdi:weather-cloudy", "white"),
    "sunny": ("Sunny", "mdi:weather-sunny", "yellow"),
    "drizzle": ("Rainy", "mdi:weather-pouring", "blue"),
    "rainy": ("Rainy", "mdi:weather-pouring", "blue"),
    "rain": ("Rainy", "mdi:weather-pouring", "blue"),
    "unavailable": ("-", "mdi:reload", "grey"),
    "Unavailable": ("-", "mdi:reload", "grey"),
    "unknown": ("-", "mdi:reload", "grey"),
    "Unknown": ("-", "mdi:reload", "grey"),
}

WIND_DIRECTIONS = [
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N'
]