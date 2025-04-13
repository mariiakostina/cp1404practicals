from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi fare calculation."""
    flagfall = 4.50
    distance = 18
    expected_price_per_km = 4.92

    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
    fancy_taxi.drive(distance)
    print(fancy_taxi)
    fare = fancy_taxi.get_fare()
    print(f"Fare for 18km: ${fare:.2f}")

    assert round(fare, 2) == round(expected_price_per_km * distance + flagfall, 2), "Fare calculation error"

main()


