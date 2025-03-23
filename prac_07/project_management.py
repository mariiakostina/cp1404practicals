"""
Estimated time: 60 min 18 16
Actual time:
"""

import csv
import datetime
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
        else:
            print("Invalid menu choice")

save_option = input(f"Would you like to save to {FILENAME}? (y/n): ").strip().lower()
if save_option == "y":
    save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a text file."""
    projects = []
    try:
        with open(filename) as in_file:
            reader = csv.reader(in_file)
            next(reader)
            for record in reader:
                name, start_date, priority, cost, completion = record[0], record[1], int(record[2]), float(record[3]), int(record[4])
            projects.append([name, start_date, priority, cost, completion])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
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

def filter_projects_date(projects):
    """Filter projects that start after a given date."""
    filter_date = get_valid_date ("Show projects that start after date (dd/mm/yyyy): ")
    print(f"That day is/was {filter_date.strftime('%A')}")
    print(filter_date.strftime("%d/%m/%Y"))
    print("Filtered projects:")
    for project in projects:
        project_date = datetime.datetime.strptime(project[1], "%d/%m/%Y").date()
        print(f"  {project[0]}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

def get_valid_date(prompt):
    """Ensure input is a valid date format"""
    try:
        date_string = input(prompt).strip()
        return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")

def get_valid_input(prompt):
    """Ensure input is not empty"""
    value = input(promt).strip()
    if value != "":
        return value
    else:
        return "Value cannot be blank"

def get_positive_number(prompt):
    """Ensure input is positive"""
    try:
        value = number_type(input(prompt).strip())
        if value > 0:
            return value
    except ValueError:
        print(f"Invalid input")

def add_project(projects):
    """Add new project"""
    print("Let's add a new project!")

    name = get_valid_input ("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_positive_number("Priority: ", int)
    cost = get_positive_number("Cost estimate: $", float)
    completion = get_positive_number("Percent complete: ", int)

    projects.append([name, start_date.strftime("%d/%m/%Y"), priority, cost, completion])


def update_project(projects):
    """Update project completion percentage"""
    for i, project in enumerate(projects):
        print(f"{i} {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

    try:
        choice = int(input("Project choice: ").strip())
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(f"\nUpdating project: {project[0]}")

            new_completion = input("New Percentage (press Enter to keep current): ").strip()
            new_priority = input("New Priority (press Enter to keep current): ").strip()

            project[4] = int(new_completion) if new_completion.isdigit() else project[4]
            project[2] = int(new_priority) if new_priority.isdigit() else project[2]

            print("\nProject updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def save_projects(filename, projects):
    """Save the project list to a text file."""
    with open(filename, "w") as out_file:
        for project in projects:
            print(",".join([str(item) for item in project]), file=out_file)

if __name__ == "__main__":
    main()


