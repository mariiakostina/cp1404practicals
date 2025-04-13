from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Fancy taxi with flagfall and price multiplier."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Init SilverServiceTaxi with fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """String representation with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
