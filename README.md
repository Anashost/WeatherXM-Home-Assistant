[![Community Forum][community_forum_shield]][community_forum]<!-- anashost_support_badges_start -->
[![Revolut.Me][revolut_me_shield]][revolut_me]
[![PayPal.Me][paypal_me_shield]][paypal_me]
[![ko_fi][ko_fi_shield]][ko_fi_me]
[![buymecoffee][buy_me_coffee_shield]][buy_me_coffee_me]
<!-- anashost_support_badges_end -->

# WeatherXM-Home-Assistant
Extract weather data from any weatherXM station via api calls in Home Assistant.

![Alt text](imgs/ha-img1.png "link")

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
* Paste the folowing [code](sensors.yaml) to your **sensors.yaml** and replace the url in line 3 with yours.
  
  (If you don't already have **sensors.yaml** file, then create it in the `/homeassistant/` directory using your File editor.

* paste the folowing [code](templates.yaml) to your **templates.yaml**
  
  (If you don't already have **templates.yaml** file, then create it in the `/homeassistant/` directory using your File editor.
  
* make sure you add these lines to your configuration.yaml:

```yaml
sensor: !include sensors.yaml
template: !include templates.yaml
```

* if the station you want is the second one in the HEX, then change the [0] with [1] in line 6.
* restart Home assistant and you're done, now weather station data is avalible in your home assistant and you're free to use it.

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
