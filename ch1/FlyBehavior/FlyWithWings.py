from abc import ABC, abstractmethod

from ch1.FlyBehavior.FlyBehavior import FlyBehavior


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!!")