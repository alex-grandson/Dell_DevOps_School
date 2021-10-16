# Weather service app

[For more info see docs](docs/README.md)

## What app can do?

App can give you an idea about average, min, max values of weather parameters like temperature (in Celsius), humidity (
in %), pressure (in mb).

![img.png](preview_image.png)

## Request parameters

You have only 2 possible parameters:

- `city=<name>` - city name you want
- `days=<n>` - number of days back

## Starting app

In order to start the application you need:

1. Get your api-key from https://weather.visualcrossing.com and paste it
 into `docker-compose.yaml`
```
environment:
  - API_KEY_WEATHER=<your_api-key_goes_here>
```

2. Be sure you installed docker-compose on your machine
3. Execute command `docker-compose start`


## Response example

```json
{
  "city": "Saint-Petersburg",
  "from": "2021-09-10",
  "to": "2021-09-15",
  "temperature_c": {
    "average": 25.0,
    "median": 24.5,
    "min": 20.1,
    "max": 29.3
  },
  "humidity": {
    "average": 55.4,
    "median": 58.1,
    "min": 43.1,
    "max": 82.4
  },
  "pressure_mb": {
    "average": 1016.0,
    "median": 1016.5,
    "min": 1015.1,
    "max": 1017.3
  }
}
```

