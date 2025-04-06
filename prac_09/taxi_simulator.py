from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main function to simulate a taxi booking and driving service."""
    # Initial taxis available
    taxi_fleet = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_cost = 0.0

    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()

    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available: ")
            display_taxis(taxi_fleet)
            taxi_index = int(input("Choose taxi: "))
            try:
                current_taxi = taxi_fleet[taxi_index]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                try:
                    distance = float(input("Drive how far? "))
                except ValueError:
                    print("Please enter a valid distance.")
                    distance = 0
                current_taxi.drive(distance)
                trip_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_fare:.2f}")
                total_cost += trip_fare
            else:
                print("You need to select a taxi before you can drive.")
        else:
            print("Invalid option.")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxi_fleet)


def display_taxis(taxis):
    """Display the list of taxis with indices."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


if __name__ == "__main__":
    main()

