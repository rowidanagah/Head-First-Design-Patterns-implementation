from observer_pattern.forecast_display import ForecastDisplay
from observer_pattern.weather_data import WeatherData
from observer_pattern.statistics_display import StatisticsDisplay


class WeatherStation:
    def __init__(self):
        self.weatherData = WeatherData()
        self.statisticsDisplay = StatisticsDisplay(self.weatherData)
        self.forecastDisplay = ForecastDisplay(self.weatherData)

    def run(self):
        print("Weather Station is running...")
        self.weatherData.set_measurements(26.0, 60.0, 1014.0)
        self.weatherData.set_measurements(29.0, 68.0, 1013.5)
        self.weatherData.set_measurements(27.0, 72.0, 1012.5)


if __name__ == "__main__":
    weather_station = WeatherStation()
    weather_station.run()
