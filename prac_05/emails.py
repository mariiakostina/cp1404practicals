"""
Emails
Estimate: 20 minutes
Actual: 39 minutes

"""
def main():
    """Prompt users for emails and store names in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()

    while email != "":
        email_to_name[email] = extract_name(email)
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Derive a probable name from an email address."""
    name = " ".join(email.split("@")[0].replace("_", " ").split(".")).title()
    response = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if response == "" or response == "y" or response == "yes":
        return name
    else:
        return input("Name: ").title()

main()