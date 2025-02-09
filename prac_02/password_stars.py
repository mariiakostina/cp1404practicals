MIN_LENGTH = 4

def main():
    """Get password and print asterisks"""
    user_password = get_password()

    print_asterisks(user_password)


def print_asterisks(user_password):
    """Print asterisks equal to the length of password"""
    print("*" * len(user_password))


def get_password():
    """Get password and check its validity"""
    user_password = input(f"Enter a password of minimum length {MIN_LENGTH}: ")
    while len(user_password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} long")
        user_password = input(f"Enter a password of minimum length {MIN_LENGTH}: ")
    return user_password


main()
