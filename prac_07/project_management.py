"""
Estimated time: 60 min
Actual time: 2 hours
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

    option = input("\n- (L)oad projects \n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>>" ).upper()

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

        option = input("- (L)oad projects \n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>>" ).upper()

    save_option = input(f"Would you like to save to {FILENAME}? (y/n): ").strip().lower()
    if save_option == "y":
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a text file."""
    projects = []
    with open(filename) as in_file:
        reader = csv.reader(in_file, delimiter="\t")
        next(reader)  # Skip header line
        for record in reader:
            if len(record) == 5:
                name, start_date, priority, cost, completion = record
                priority, cost, completion = int(priority), float(cost), int(completion)
                projects.append([name, start_date, priority, cost, completion])
    return projects

def display_projects(projects):
    """Display the list of projects"""
    projects.sort(key=itemgetter(2))  # Sort by priority

    completed_projects = [project for project in projects if project[4] == 100]
    incomplete_projects = [project for project in projects if project[4] < 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

    print(f"{len(completed_projects)} projects completed, {len(incomplete_projects)} projects still in progress.")

def filter_projects_date(projects):
    """Filter projects that start after a given date."""
    filter_date = get_valid_date ("Show projects that start after date (dd/mm/yyyy): ")
    for project in projects:
        project_date = datetime.datetime.strptime(project[1], "%d/%m/%Y").date()
        if project_date >= filter_date:
            print(f"{project[0]}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

def get_valid_date(prompt):
    """Ensure input is a valid date format"""
    date_string = input(prompt).strip()
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

def get_valid_input(prompt):
    """Ensure input is not empty"""
    value = input(prompt).strip()
    return value

def get_positive_number(prompt, number_type):
    """Ensure input is positive"""
    value = input(prompt).strip()
    try:
        number = number_type(value)
        if number >= 0:
            return number
        else:
            print(f"Number must be positive. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return get_positive_number(prompt, number_type)
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

    choice = get_positive_number("Project choice: ", int)
    if 0 <= choice < len(projects):
        project = projects[choice]

        print(
            f"{project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:,.2f}, completion: {project[4]}%")

        new_completion = input(f"New Percentage ").strip()
        new_priority = input(f"New Priority ").strip()

        project[4] = int(new_completion) if new_completion.isdigit() else project[4]
        project[2] = int(new_priority) if new_priority.isdigit() else project[2]

        print("Project updated successfully!")


def save_projects(filename, projects):
    """Save the project list to a text file."""
    with open(filename, "w") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for project in projects:
            writer.writerow(project)

if __name__ == "__main__":
    main()



