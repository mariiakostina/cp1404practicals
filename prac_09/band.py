class Band:
    """Represent a band composed of musicians."""
    def __init__(self, name):
        """Initialize Band with name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string showing band name and members."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a summary of what each musician plays."""
        return "\n".join(musician.play() for musician in self.musicians)
