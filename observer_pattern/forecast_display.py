from observer_pattern.display_element import DisplayElement
from observer_pattern.observer import Observer
from observer_pattern.weather_data import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    """
    A display element that shows the weather forecast.
    It implements the Observer interface to receive updates from WeatherData.
    """

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.current_temperature = 0.0
        self.current_humidity = 0.0
        self.forecast = "No forecast available"
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """
        Update the forecast with the latest weather data.
        :param temperature: The current temperature.
        :param humidity: The current humidity.
        :param pressure: The current pressure (not used in this display).
        """
        self.current_temperature = temperature
        self.current_humidity = humidity
        self.forecast = self.calculate_forecast()
        self.display()

    def calculate_forecast(self):
        """
        Calculate the forecast based on the current conditions.
        This is a simple example; real forecasting would be more complex.
        """
        if self.current_temperature > 30:
            return "Hot and sunny"
        elif self.current_temperature < 10:
            return "Cold and possibly snowy"
        else:
            return "Mild and pleasant"

    def display(self):
        """
        Display the forecast.
        """
        print(f"Forecast: {self.forecast}")