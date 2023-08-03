[![Community Forum][community_forum_shield]][community_forum]<!-- anashost_support_badges_start -->
[![PayPal.Me][paypal_me_shield]][paypal_me]
[![Revolut.Me][revolut_me_shield]][revolut_me]
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
* now paste the folowing [code](sensors.yaml) to your **sensors.yaml** and replace the url in line 3 with yours.
  
  (If you don't already have **sensos.yaml** file, then create it in the `/config/` directory using your File editor.
* make sure you add this line to your configuration.yaml:

  `sensor: !include sensors.yaml`
* if the station you want is the second one in the HEX, then change the [0] with [1] in line 6.
* restart Home assistant and you're done, now weather station data is avalible in your home assistant and you're free to use it.

# Enjoy

Inpired by [arcidodo](https://github.com/arcidodo), here's a [link](https://github.com/arcidodo/WeatherXM-Home-Assistant) to his repo.

[latest_release]: https://github.com/Anashost/WeatherXM-Home-Assistant/releases/latest

[releases_shield]: https://img.shields.io/github/release/Anashost/WeatherXM-Home-Assistant.svg?style=popout

[releases]: https://github.com/Anashost/WeatherXM-Home-Assistant/releases

[community_forum_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Forum&style=popout&color=41bdf5&logo=HomeAssistant&logoColor=white

[community_forum]: https://community.home-assistant.io/t/weatherxm-integration-in-home-assistant/521667

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal

[paypal_me]: https://www.paypal.me/anashost

[revolut_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Revolut&logo=revolut

[revolut_me]: https://revolut.me/anas4e
