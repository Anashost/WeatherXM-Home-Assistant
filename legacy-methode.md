[![Community Forum][community_forum_shield]][community_forum]<!-- anashost_support_badges_start -->
[![Revolut.Me][revolut_me_shield]][revolut_me]
[![PayPal.Me][paypal_me_shield]][paypal_me]
[![ko_fi][ko_fi_shield]][ko_fi_me]
[![buymecoffee][buy_me_coffee_shield]][buy_me_coffee_me]
<!-- anashost_support_badges_end -->

# WeatherXM-Home-Assistant
Extract weather data from any weatherXM station via api calls in Home Assistant.

<img width="503" height="244" alt="Screenshot 2026-01-05 045623" src="https://github.com/user-attachments/assets/49c9ab30-a1e3-477e-b0a9-ccd630c87938" />

<details>
<summary><strong>want this card? click here</summary>
  
* integrations needed from HACS: mushroom, card-mod

```yaml
type: custom:mod-card
style: |
  ha-card {
    background: linear-gradient(to bottom right, #2c3e50, #4ca1af); /* Default Dark Blue/Teal Gradient */
    border-radius: 20px;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    padding: 10px 0px;
    border: none;
  }
card:
  type: vertical-stack
  cards:
    - type: custom:mushroom-template-card
      entity: sensor.weatherxm_weather_condition
      primary: |
        {{ states('sensor.weatherxm_temperature_celsius') }}°
      secondary: >
        {{ states('sensor.weatherxm_weather_condition') }} • Feels like {{
        states('sensor.weatherxm_feels_like_celsius') | round(0) }}°
      icon: |
        {{ states('sensor.weatherxm_icon') }}
      icon_color: >
        {% set cond = states('sensor.weatherxm_weather_condition') %} {% if
        'Sun' in cond or 'Clear' in cond %} orange {% elif 'Rain' in cond %}
        blue {% elif 'Cloud' in cond %} light-blue {% else %} white {% endif %}
      layout: horizontal
      multiline_secondary: true
      fill_container: true
      tap_action:
        action: more-info
      card_mod:
        style: |
          ha-card {
            background: none;
            box-shadow: none;
            border: none;
          }
          :host {
            --mush-icon-size: 72px;
          }
          .primary {
            font-size: 48px !important;
            font-weight: 700 !important;
            line-height: 1.2 !important;
            color: white !important;
          }
          .secondary {
            font-size: 18px !important;
            color: rgba(255,255,255,0.8) !important;
          }
    - type: custom:mushroom-chips-card
      alignment: center
      chips:
        - type: template
          entity: sensor.weatherxm_humidity
          content: "{{ states('sensor.weatherxm_humidity') }}% Humidity"
          icon: mdi:water-percent
          icon_color: blue
          tap_action:
            action: more-info
          card_mod:
            style: |
              ha-card {
                background: rgba(255,255,255,0.1) !important;
                border: none !important;
                border-radius: 12px !important;
                --text-color: white;
              }
        - type: template
          entity: sensor.weatherxm_uv_index
          content: UV {{ states('sensor.weatherxm_uv_index') }}
          icon: mdi:sun-wireless
          icon_color: orange
          tap_action:
            action: more-info
          card_mod:
            style: |
              ha-card {
                background: rgba(255,255,255,0.1) !important;
                border: none !important;
                border-radius: 12px !important;
                --text-color: white;
              }
    - type: grid
      columns: 3
      square: false
      cards:
        - type: custom:mushroom-entity-card
          entity: sensor.weatherxm_wind_speed_kmh
          name: Wind
          icon: mdi:weather-windy
          primary_info: state
          secondary_info: name
          icon_color: green
          layout: vertical
          card_mod:
            style: |
              ha-card {
                background: none;
                box-shadow: none;
                border: none;
                color: white;
              }
              :host {
                --card-secondary-text-color: rgba(255,255,255,0.7);
                --card-primary-text-color: white;
              }
        - type: custom:mushroom-entity-card
          entity: sensor.weatherxm_daily_precipitation_mm
          name: Rain
          icon: mdi:weather-pouring
          primary_info: state
          secondary_info: name
          icon_color: light-blue
          layout: vertical
          card_mod:
            style: |
              ha-card {
                background: none;
                box-shadow: none;
                border: none;
                color: white;
              }
              :host {
                --card-secondary-text-color: rgba(255,255,255,0.7);
                --card-primary-text-color: white;
              }
        - type: custom:mushroom-entity-card
          entity: sensor.weatherxm_pressure_hpa
          name: Pressure
          icon: mdi:gauge
          primary_info: state
          secondary_info: name
          icon_color: orange
          layout: vertical
          card_mod:
            style: |
              ha-card {
                background: none;
                box-shadow: none;
                border: none;
                color: white;
              }
              :host {
                --card-secondary-text-color: rgba(255,255,255,0.7);
                --card-primary-text-color: white;
              }

```
</details>

# This implementation will create the following sensors:
* weather condition (sunny, cloudy, partly cloudy, rainy).
* temperature
* temperature real feel
* humidity
* wind speed
* wind gust
* pressure hpa
* wind direction
* wind direction cardinal
* live precipitation
* daily precipitation
* past 7 days precipitation
* uv_index
* icon 
* icon color

# How it works?
* navigate to [WeatheXM Explorer](https://explorer.weatherxm.com/).
* pick the station you want.
* in the website url copy the highlighted text after the # (in yellow).

![Alt text](imgs/link.png "link")

* replace the (*****) with the text you copied.

  `https://api.weatherxm.com/api/v1/cells/*****/devices`

  we need this url for the api call.
* Paste the following [code](sensors.yaml) to your **sensors.yaml** and replace the url in line 3 with yours.
  
  (If you don't already have **sensors.yaml** file, then create it in the `/homeassistant/` directory using your File editor.

* paste the following [code](templates.yaml) to your **templates.yaml**
  
  (If you don't already have **templates.yaml** file, then create it in the `/homeassistant/` directory using your File editor.
  
* make sure you add these lines to your configuration.yaml:

```yaml
sensor: !include sensors.yaml
template: !include templates.yaml
```

* if the station you want is the second one in the HEX, then change the [0] with [1] in line 6.
* restart Home Assistant and you're done, now weather station data is available in your Home Assistant and you're free to use it.

# Enjoy

Inpired by [arcidodo](https://github.com/arcidodo), here's a [link](https://github.com/arcidodo/WeatherXM-Home-Assistant) to his repo.

[latest_release]: https://github.com/Anashost/WeatherXM-Home-Assistant/releases/latest

[releases_shield]: https://img.shields.io/github/release/Anashost/WeatherXM-Home-Assistant.svg?style=popout

[releases]: https://github.com/Anashost/WeatherXM-Home-Assistant/releases

[community_forum_shield]: 
https://img.shields.io/badge/Fourms-23cede?style=for-the-badge&logo=HomeAssistant&logoColor=white

[community_forum]: https://community.home-assistant.io/t/weatherxm-integration-in-home-assistant/521667

[paypal_me_shield]: https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white

[paypal_me]: https://paypal.me/anasboxsupport

[revolut_me_shield]:
https://img.shields.io/badge/revolut-FFFFFF?style=for-the-badge&logo=revolut&logoColor=black

[revolut_me]: https://revolut.me/anas4e

[ko_fi_shield]: https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white

[ko_fi_me]: https://ko-fi.com/anasbox

[buy_me_coffee_shield]: 
https://img.shields.io/badge/Buy%20Me%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black

[buy_me_coffee_me]: https://www.buymeacoffee.com/anasbox
