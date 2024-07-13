from abc import ABC, abstractmethod

from ch1.FlyBehavior.FlyBehavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")