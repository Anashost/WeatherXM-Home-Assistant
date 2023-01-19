# WeatherXM-Home-Assistant
Extract weather data from any weatherXM station via api calls in Home Assistant.

![Alt text](imgs/ha-img1.png "link")

# This implementation will create the following sensors:
* weather condition (sunny, cloudy, partly cloudy, rainy).
* temperature
* temperature real feel
* humidity
* wind speed kmh - mh
* wind gust kmh - mh
* pressure hpa
* wind direction
* wind direction cardinal
* precipitation
* uv_index
* icon 
* icon color

# How it works?
* navigate to [WeatheXM Explorer](https://explorer.weatherxm.com/).
* pick the station you want.
* in the website url copy the highlighted text after the # (in yellow).

![Alt text](imgs/link.png "link")

* replace the (*****) with the text you copied.

  https://api.weatherxm.com/api/v1/cells/*****/devices

  we need this url for the api call.
* now paste the folowing [code](sensors.yaml) to your **sensors.yaml** and replace the url in line 3 with yours.
<details>
  <summary> yaml code (Click to expand)</summary>
  
* paste this code to your **sensors.yaml**
  
  ```
 - platform: rest
  name: "weatherxm_sensor"
  resource: https://api.weatherxm.com/api/v1/cells/*****/devices
  scan_interval: 300
  value_template: "{{ value_json.value }}"
  json_attributes_path: $.[0].current_weather
  json_attributes:
    - temperature
    - feels_like
    - humidity
    - icon  
    - precipitation
    - pressure
    - uv_index
    - wind_direction
    - wind_gust
    - wind_speed

- platform: template
  sensors:
    weatherxm_temperature:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'temperature')|round(2)}}"
      device_class: temperature
      unit_of_measurement: "°C"

- platform: template
  sensors:
    weatherxm_feels_like:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'feels_like')|round(2)}}"
      device_class: temperature
      unit_of_measurement: "°C"

- platform: template
  sensors:
    weatherxm_humidity:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'humidity')|round(2)}}"
      device_class: humidity
      unit_of_measurement: "°%"

- platform: template
  sensors:
    weatherxm_wind_speed_kmh:
      value_template: "{{ (state_attr('sensor.weatherxm_sensor', 'wind_speed') |float * 3.6) |round(2) }}"
      unit_of_measurement: "km/h"

- platform: template
  sensors:
    weatherxm_wind_gust_kmh:
      value_template: "{{ (state_attr('sensor.weatherxm_sensor', 'wind_gust') |float * 3.6) |round(2) }}"
      unit_of_measurement: "km/h"

- platform: template
  sensors:
    weatherxm_wind_speed_mph:
      value_template: "{{ (state_attr('sensor.weatherxm_sensor', 'wind_speed') |float / 1.60934) |round(2) }}"
      unit_of_measurement: "mph"
 
- platform: template
  sensors:
    weatherxm_wind_gust_mph:
      value_template: "{{ (state_attr('sensor.weatherxm_sensor', 'wind_gust') |float / 1.60934) |round(2) }}"
      unit_of_measurement: "mph"
      
- platform: template
  sensors:
    weatherxm_wind_direction:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'wind_direction')}}"
      unit_of_measurement: "°"

- platform: template
  sensors:
    weatherxm_pressure_hpa:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'pressure')|round(0)}}"
      device_class: pressure
      unit_of_measurement: "°hPa"
      
- platform: template
  sensors:
    weatherxm_wind_direction_cardinal:
      value_template: >
          {% set direction = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','N'] %}
          {% set degree = states('sensor.weatherxm_wind_direction')|float %}
            {{ direction[((degree+11.25)/22.5)|int] }}

- platform: template
  sensors:
    weatherxm_precipitation:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'precipitation')}}"
      device_class: precipitation_intensity
      unit_of_measurement: "mm/h"

- platform: template
  sensors:
    weatherxm_uv_index:
      value_template: "{{ state_attr('sensor.weatherxm_sensor', 'uv_index')}}"
      unit_of_measurement: "UV Index"

- platform: template
  sensors:
    weatherxm_weather_condition:
      value_template: >
          {% set state = state_attr('sensor.weatherxm_sensor', 'icon') %}
          {% if state == 'partly-cloudy-night' %} Partly cloudy
          {% elif state == 'partly-cloudy-day' %} Partly cloudy
          {% elif state == 'cloudy-night' %} Cloudy
          {% elif state == 'cloudy-day' %} Cloudy
          {% elif state == 'sunny' %} Sunny
          {% elif state == 'drizzle' %} Rainy
          {% elif state == 'rainy' %} Rainy
          {% elif state == 'unavailable' %} -
          {% elif state == 'Unavailable' %} -
          {% elif state == 'unknown' %} -
          {% elif state == 'Unknown' %} -
          {% endif %}

- platform: template
  sensors:
    weatherxm_icon:
      friendly_name: 'weatherxm icon'
      value_template: >
          {% set state = state_attr('sensor.weatherxm_sensor', 'icon') %}
          {% if state == 'partly-cloudy-night' %} mdi:weather-night-partly-cloudy
          {% elif state == 'partly-cloudy-day' %} mdi:weather-partly-cloudy
          {% elif state == 'cloudy-night' %} mdi:weather-night-partly-cloudy
          {% elif state == 'cloudy-day' %} mdi:weather-cloudy
          {% elif state == 'sunny' %} mdi:weather-sunny
          {% elif state == 'drizzle' %} mdi:weather-pouring
          {% elif state == 'rainy' %} mdi:weather-pouring
          {% elif state == 'unavailable' %} mdi:reload
          {% elif state == 'Unavailable' %} mdi:reload
          {% elif state == 'unknown' %} mdi:reload
          {% elif state == 'Unknown' %} mdi:reload
          {% endif %}

- platform: template
  sensors:
    weatherxm_icon_color:
      friendly_name: 'weatherxm icon color'
      value_template: >
          {% set state = state_attr('sensor.weatherxm_sensor', 'icon') %}
          {% if state == 'partly-cloudy-night' %} blue-grey
          {% elif state == 'partly-cloudy-day' %} white
          {% elif state == 'cloudy-night' %} blue-grey
          {% elif state == 'cloudy-day' %} white
          {% elif state == 'sunny' %} yellow
          {% elif state == 'drizzle' %} blue
          {% elif state == 'rainy' %} blue
          {% elif state == 'unavailable' %} grey
          {% elif state == 'Unavailable' %} grey
          {% elif state == 'unknown' %} grey
          {% elif state == 'Unknown' %} grey
          {% endif %}
  ```
</details>

* if the station you want is the second one in the HEX, then change the [0] with [1] in line 6.
* restart Home assistant and you're done, now weather station data is avalible in your home assistant and you're free to use it.

### Big portion of the code was inpired by [arcidodo](https://github.com/arcidodo) Thanks to him, [link](https://github.com/arcidodo/WeatherXM-Home-Assistant) to his repo.

# Enjoy
