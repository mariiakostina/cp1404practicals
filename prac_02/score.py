"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

def main():
    """Get score, print score, random score"""
    score = float(input("Enter score: "))
    print(f"Your result: {get_score_result(score)}")

    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(f"Random score {random_score}: {get_score_result(random_score)}")

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
