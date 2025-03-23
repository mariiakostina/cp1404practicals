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



