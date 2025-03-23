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

    print("Sort guitars by year: ")
    guitars.sort()
    display_guitars(guitars)
    add_new_guitars(guitars)
    store_guitars(guitars)

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

def store_guitars(guitars):
    """Save current list of guitars to a text file"""
    in_file = open("guitars.csv", "w", newline="")
    for guitar in guitars:
        in_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    in_file.close()
    print("\nGuitars saved to 'guitars.csv'!")

if __name__ == "__main__":
    main()

