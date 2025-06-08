from observer_pattern.display_element import DisplayElement
from observer_pattern.observer import Observer
from observer_pattern.weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    """
    A display element that shows the current weather conditions.
    It implements the Observer interface to receive updates from WeatherData.
    """

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """
        Update the display with the latest weather data.
        :param temperature: The current temperature.
        :param humidity: The current humidity.
        :param pressure: The current pressure (not used in this display).
        """
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        """
        Display the current conditions.
        """
        print(f"Current conditions: {self.temperature}°C and {self.humidity}% humidity")