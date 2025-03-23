"""
Estimated time: 40 min
Actual time: 1 hour
"""

import datetime


class Project:
    """Represent project object"""

    def __init__(self, name, start_date, priority, cost, completion):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.cost:,.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority
