"""
Estimated time: 20 min
Actual time: start 23:16, 16 min
"""

class ProgrammingLanguage:
    """Represent a Programming Language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True/False if the programming language is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
