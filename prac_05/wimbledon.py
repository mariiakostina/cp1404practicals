"""
Wimbledon
Estimate: 20 minutes
Actual: 52 minutes
"""
import csv

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 2
INDEX_COUNTRY = 1

def main():
    """Process Wimbledon data and display results."""
    match_details = load_data(FILENAME)
    champion_to_wins, winning_countries = analyze_data(match_details)
    display_results(champion_to_wins, winning_countries)
def load_data(filename):
    """Read data from CSV file and return a list of records."""
    match_details = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            match_details.append(row)
    return match_details

def analyze_data(match_details):
    """Process match_data to count champion wins and track winning countries."""
    champion_to_wins = {}
    winning_countries = set()
    for match in match_details:
        champion = match[INDEX_CHAMPION]
        country = match[INDEX_COUNTRY]
        winning_countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, winning_countries

def display_results(champion_to_wins, winning_countries):
    """Display processed Wimbledon champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(winning_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(winning_countries)))

main()



