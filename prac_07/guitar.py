CURRENT_YEAR = 2024
VINTAGE_AGE = 50
class Guitar:
    """Represent a Guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare Guitars by year."""
        return self.year < other.year

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"