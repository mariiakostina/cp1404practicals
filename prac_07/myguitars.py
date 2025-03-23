import csv
from prac_07.guitar import Guitar

def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')

        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)

        guitars.append(guitar)

    in_file.close()

    display_guitars(guitars)
    print("Sort guitars by year: ")
    guitars.sort()


def display_guitars(guitars):
    """Display all guitars in the list"""
    if not guitars:
        print("Guitars not found")
    else:
        print("Guitars:")
        for guitar in guitars:
            print(guitar)

def add_new_guitars(guitars):
    """Add new guitars to the list"""
    name = input("Enter new guitar: ").strip()

    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added!")
        name = input("Name: ").strip()

