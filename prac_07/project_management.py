"""
Estimated time: 60 min 18 16
Actual time:
"""

import csv
from datetime import datetime
from operator import itemgetter
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
       if option == "L":
           filename = input("Enter filename: ")
           projects = load_projects(filename)
       elif option == "S":
           filename = input("Enter filename to save to: ")
           save_projects(filename, projects)
       elif option == "D":
           display_projects(projects)
       elif option == "F":
           filter_projects_date(projects)
       elif option == "A":
           add_project(projects)
       elif option == "U":
           update_project(projects)

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

def display_projects(projects):
    """Display the list of projects"""
    projects.sort(key=itemgetter(2, 0))
    completed_projects = [project for project in projects if project[4] == 100]
    incomplete_projects = [project for project in projects if project[4] < 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"* {project[0]} - Start: {project[1]}, Priority: {project[2]}, Estimate: ${project[3]:,.2f}, Completion: {project[4]}%")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project[0]} - Start: {project[1]}, Priority: {project[2]}, Estimate: ${project[3]:,.2f}, Completion: {project[4]}%")

    print(f"{len(completed_projects)} projects completed, {len(incomplete_projects)} projects still in progress.")


