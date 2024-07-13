from ch1.QuackBehavior.QuackBehavior import QuackBehavior


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("Quack")



c = Quack()

c.quack()