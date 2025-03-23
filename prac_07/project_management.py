"""
Estimated time: 60 min 18 16
Actual time:
"""

import csv
from datetime import datetime
from prac_07.project import Project

FILENAME = "projects.txt"
WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
def main():
    """Manage and track projects from a text file."""
    print(WELCOME_MESSAGE)

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

   option = input("\n- (L)oad projects \n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit").upper()

   while option != "Q":
       if option == "L"


def load_projects(filename):
    """Load projects from a text file."""
    projects = []
    with open(filename) as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for record in reader:
            name, start_date, priority, cost, completion = record[0], record[1], int(record[2]), float(record[3]), int(
                record[4])
            projects.append([name, start_date, priority, cost, completion])
    return projects