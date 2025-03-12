"""
Estimated time: 20 min
Actual time: 31 min
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2024
def run_test():
    """Test the Guitar class methods"""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1256.3)

    print(f"{guitar1.name} get_age() - Expected {102}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {11}. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected {True}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {False}. Got {guitar2.is_vintage()}")


if __name__ == "__main__":
    run_test()