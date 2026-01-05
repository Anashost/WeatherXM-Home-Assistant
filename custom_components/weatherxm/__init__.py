"""WeatherXM Integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    # forward to the sensor platform using the new plural API
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # unload the sensor platform
    result = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    if result:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return result
