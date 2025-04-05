from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """A car that may fail to drive."""

    def __init__(self, name, fuel, reliability):
        """Set up car with reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt drive based on reliability."""
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        return super().drive(0)
