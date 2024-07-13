from Duck import Duck
from ch1.FlyBehavior.FlyWithWings import FlyWithWings
from ch1.QuackBehavior.Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self) -> None:
        print("I'm a real Mallard duck")


c = MallardDuck()
c.display()


c.performFly()
