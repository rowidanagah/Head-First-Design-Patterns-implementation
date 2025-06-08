from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        """Register an observer to the subject."""
        pass

    @abstractmethod
    def remove_observer(self, observer):
        """Remove an observer from the subject."""
        pass

    @abstractmethod
    def notify_observers(self):
        """Notify all registered observers of a change."""
        pass