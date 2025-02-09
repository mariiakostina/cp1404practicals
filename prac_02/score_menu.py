

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

MENU = "Main menu: \n(G)et valid score \n(P)rint result\n(S)how stars\n(Q)uit \n"
def main():
    """Display the menu"""
    print(MENU)
    choice = input("Get choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            print(f"Result: {get_score_result(validate_score())}")
        elif choice == "S":
            print_stars(validate_score())
        else:
            print("Invalid option")

        print(MENU)
        choice = input("Get choice: ").upper()
    print("Farewell")

def print_stars(score):
    """Prints as many stars as the score."""
    print("*" * int(score))


def validate_score():
    """Get the score and validate the score"""
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Score sould be 0-100 inclusive")
        score = float(input("Enter score: "))
    return score

def get_score_result(score):
    """Returns result based on the score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()

