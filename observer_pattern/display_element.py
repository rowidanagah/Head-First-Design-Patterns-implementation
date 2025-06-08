from abc import ABC, abstractmethod


class DisplayElement(ABC):
    """
    An abstract base class TO display elements in the observer pattern.
    """

    @abstractmethod
    def display(self):
        """
        Display the content of the element.
        """
        pass