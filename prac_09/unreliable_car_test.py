from prac_09.unreliable_car import UnreliableCar

def main():
    """Simulate repeated drives."""
    reliable_car = UnreliableCar("Trusty", 100, 90)
    unreliable_car = UnreliableCar("Sketchy", 100, 10)

    # Try driving each car over multiple distances
    for distance in range(1, 10):
        print(f"Driving attempt: {distance}km")
        print(f"{reliable_car.name:10} drove {reliable_car.drive(distance):2}km")
        print(f"{unreliable_car.name:10} drove {unreliable_car.drive(distance):2}km")

    # Display final car status
    print(reliable_car)
    print(unreliable_car)


if __name__ == "__main__":
    main()

