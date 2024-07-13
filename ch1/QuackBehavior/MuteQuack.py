from ch1.QuackBehavior.QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("MuteQuack")
