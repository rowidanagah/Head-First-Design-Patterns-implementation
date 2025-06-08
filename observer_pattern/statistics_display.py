from observer_pattern.display_element import DisplayElement
from observer_pattern.observer import Observer
from observer_pattern.weather_data import WeatherData


class StatisticsDisplay(Observer, DisplayElement):
    """
    A display element that shows statistics of the weather data.
    It implements the Observer interface to receive updates from WeatherData.
    """

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.total_temp = 0.0
        self.num_readings = 0
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """
        Update the statistics with the latest weather data.
        :param temperature: The current temperature.
        :param humidity: The current humidity.
        :param pressure: The current pressure (not used in this display).
        """
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        # Update statistics
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

        self.total_temp += temperature
        self.num_readings += 1

        self.display()

    def display(self):
        """
        Display the statistics.
        """
        avg_temp = self.total_temp / self.num_readings if self.num_readings > 0 else 0.0
        print(f"Avg/Max/Min temperature: {avg_temp:.2f}/{self.max_temp:.2f}/{self.min_temp:.2f}°C")
