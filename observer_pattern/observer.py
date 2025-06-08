from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract base class for observers in the observer pattern.
    Observers must implement the `update` method to receive notifications.
    """

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Update method to be called when the subject changes.
        :param args: Positional arguments passed from the subject.
        :param kwargs: Keyword arguments passed from the subject.
        """
        pass