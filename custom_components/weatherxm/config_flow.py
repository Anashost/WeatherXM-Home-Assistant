import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_STATION_ID, CONF_DEVICE_INDEX

_LOGGER = logging.getLogger(__name__)

class WeatherXMConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WeatherXM."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            station_id = user_input[CONF_STATION_ID].strip()
            await self.async_set_unique_id(station_id)
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(
                title=f"WeatherXM {station_id}",
                data={
                    CONF_STATION_ID: station_id,
                    CONF_DEVICE_INDEX: user_input.get(CONF_DEVICE_INDEX, 0)
                }
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_STATION_ID): str,
                vol.Optional(CONF_DEVICE_INDEX, default=0): int
            }),
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return WeatherXMOptionsFlow(config_entry)

class WeatherXMOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for WeatherXM."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    CONF_DEVICE_INDEX,
                    default=self.config_entry.options.get(CONF_DEVICE_INDEX, 0)
                ): int
            })
        )