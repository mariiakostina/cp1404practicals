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

    print("Loaded Guitars ")
    display_guitars(guitars)

    choice_to_sort = input("\nDo you want to sort guitars by year? (y/n): ").strip().lower()
    if choice_to_sort == "y":
        guitars.sort()
        print("Sorted Guitars:")
        display_guitars(guitars)


    choice_add_guitar = input("\nDo you want to add new guitars? (y/n): ").strip().lower()
    if choice_add_guitar == "y":
        add_new_guitars(guitars)


    store_guitars(guitars)

def display_guitars(guitars):
    """Display all guitars in the list"""
    if not guitars:
        print("Guitars not found")
    else:
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
    out_file = open("guitars.csv", "w", newline="")
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    out_file.close()
    print("\nGuitars saved to 'guitars.csv'!")

if __name__ == "__main__":
    main()

