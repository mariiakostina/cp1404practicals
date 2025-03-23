"""
Estimated time: 40 min 20:00
Actual time:
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

    def update_completion(self, new_completion):
        """Update the project's completion percentage."""
        try:
            new_value = int(new_completion)
            if 0 <= new_value <= 100:
                self.completion = new_value
        except ValueError:
            print("Invalid input")

    def update_priority(self, new_priority):
        """Update the project's priority."""
        try:
            new_value = int(new_priority)
            if new_value > 0:
                self.priority = new_value
        except ValueError:
            print("Invalid input")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority