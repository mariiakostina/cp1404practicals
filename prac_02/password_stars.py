MIN_LENGTH = 4

def main():
    """Get password and print asterisks"""
    user_password = get_password(MIN_LENGTH)

    print_asterisks(user_password)


def print_asterisks(user_password):
    """Print asterisks equal to the length of password"""
    print("*" * len(user_password))


def get_password(min_length):
    """Get password and check its validity"""
    user_password = input(f"Enter a password of minimum length {min_length}: ")
    while len(user_password) < min_length:
        print(f"Password must be at least {min_length} long")
        user_password = input(f"Enter a password of minimum length {min_length}: ")
    return user_password


main()
