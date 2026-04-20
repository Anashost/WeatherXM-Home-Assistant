import logging
from datetime import timedelta
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.util.dt import utcnow
import aiohttp
import async_timeout

from .const import (
    DOMAIN,
    API_URL,
    CONF_STATION_ID,
    CONF_DEVICE_INDEX,
    SENSOR_TYPES,
    CONDITION_MAP,
    WIND_DIRECTIONS,
    ATTR_TEMPERATURE,
    ATTR_FEELS_LIKE,
    ATTR_HUMIDITY,
    ATTR_ICON,
    ATTR_PRECIPITATION,
    ATTR_PRECIPITATION_ACCUMULATED,
    ATTR_PRESSURE,
    ATTR_UV_INDEX,
    ATTR_WIND_DIRECTION,
    ATTR_WIND_GUST,
    ATTR_WIND_SPEED,
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=300)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up sensors from a config entry."""
    station_id = config_entry.data[CONF_STATION_ID]
    device_index = config_entry.data.get(CONF_DEVICE_INDEX, 0)
    
    coordinator = WeatherXMDataCoordinator(hass, station_id, device_index)
    await coordinator.async_config_entry_first_refresh()
    
    sensors = []
    for sensor_type in SENSOR_TYPES:
        sensors.append(WeatherXMSensor(coordinator, sensor_type, station_id))
        
    async_add_entities(sensors, True)

class WeatherXMDataCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(self, hass, station_id, device_index):
        """Initialize."""
        self.station_id = station_id
        self.device_index = device_index
        self.url = API_URL.format(station_id)
        self.data = {}
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url) as response:
                        data = await response.json()
                        return data[self.device_index]["current_weather"]
        except (aiohttp.ClientError, KeyError, IndexError) as error:
            raise UpdateFailed(f"Error fetching data: {error}") from error

class WeatherXMSensor(CoordinatorEntity, SensorEntity):
    """Representation of a WeatherXM sensor."""
    
    def __init__(self, coordinator, sensor_type, station_id):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_type = sensor_type
        self._station_id = station_id
        self._attr_name = f"WeatherXM {SENSOR_TYPES[sensor_type][0]}"
        self._attr_unique_id = f"{station_id}_{sensor_type}"
        self._attr_device_class = SENSOR_TYPES[sensor_type][2]
        self._attr_native_unit_of_measurement = SENSOR_TYPES[sensor_type][1]

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None
            
        data = self.coordinator.data
        
        if self._sensor_type == "temperature":
            return round(data.get(ATTR_TEMPERATURE, 0), 1)
        elif self._sensor_type == "feels_like":
            return round(data.get(ATTR_FEELS_LIKE, 0), 1)
        elif self._sensor_type == "humidity":
            return round(data.get(ATTR_HUMIDITY, 0), 2)
        elif self._sensor_type == "pressure":
            return round(data.get(ATTR_PRESSURE, 0))
        elif self._sensor_type == "wind_speed":
            return round(data.get(ATTR_WIND_SPEED, 0), 2)
        elif self._sensor_type == "wind_gust":
            return round(data.get(ATTR_WIND_GUST, 0), 2)
        elif self._sensor_type == "wind_direction":
            return data.get(ATTR_WIND_DIRECTION, 0)
        elif self._sensor_type == "wind_direction_cardinal":
            degree = data.get(ATTR_WIND_DIRECTION, 0)
            index = int((degree + 11.25) / 22.5) % 16
            return WIND_DIRECTIONS[index]
        elif self._sensor_type == "precipitation":
            return round(data.get(ATTR_PRECIPITATION, 0), 2)
        elif self._sensor_type == "precipitation_accumulated":
            return round(data.get(ATTR_PRECIPITATION_ACCUMULATED, 0), 2)
        elif self._sensor_type == "uv_index":
            return data.get(ATTR_UV_INDEX, 0)
        elif self._sensor_type in ["condition", "icon", "icon_color"]:
            icon = data.get(ATTR_ICON, "unknown")
            return CONDITION_MAP.get(icon, ("-", "mdi:reload", "grey"))[
                ["condition", "icon", "icon_color"].index(self._sensor_type)
            ]
        return None

    @property
    def extra_state_attributes(self):
        """Return device state attributes."""
        return {
            "station_id": self._station_id,
            "last_update": utcnow().isoformat()
        }