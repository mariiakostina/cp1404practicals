import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    """loop to generate and print each quick pick"""
    number_picks = get_number_quick_picks()

    for i in range(number_picks):
        quick_picks = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_picks))


def get_number_quick_picks():
    """prompt user to enter quick picks number"""
    number_picks = int(input("Number quick picks:  "))
    while number_picks <= 0:
        print("Cannot be less or equal to 0")
        number_picks = int(input("Number quick picks: "))
    return number_picks


def generate_quick_pick():
    """generate a list of 6 unique numbers"""
    quick_picks = []
    for j in range(NUMBERS_PER_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_picks:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    return quick_picks

main()
