# WeatherXM-Home-Home-Assistant
Extract weather data from any weatherXM station via api calls in Home Assistant

# How it works?
* navigate to [WeatheXM Explorer](https://explorer.weatherxm.com/).
* pick the station you want.
* in the website link copy the highlighted tex in yellow.

![Alt text](imgs/link.png "link")

* replace the (*****) with the text you copied
  https://api.weatherxm.com/api/v1/cells/*****/devices
  we need this url for the api call.
* now paste the folowing coe to your *sensors.yaml*

