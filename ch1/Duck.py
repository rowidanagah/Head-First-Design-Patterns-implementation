from abc import ABC, abstractmethod

from ch1.FlyBehavior.FlyBehavior import FlyBehavior
from ch1.QuackBehavior.QuackBehavior import QuackBehavior



class Duck(ABC):
    flyBehavior: FlyBehavior
    quackBehavior: QuackBehavior

    # def setFlyBehavior(self, fb: FlyBehavior) -> None:
    #     self.flyBehavior = fb

    # def setQuackBehavior(self, qb: QuackBehavior) -> None:
    #     self.quackBehavior = qb

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError

    def swim(self):
        print("all ducks swim")
