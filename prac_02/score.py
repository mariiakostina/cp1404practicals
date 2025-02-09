"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

score = float(input("Enter score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASSABLE_THRESHOLD:
    print("Passable")
else:
    print("Bad")