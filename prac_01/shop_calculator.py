DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100


number_items = int(input("Number of items: "))

while number_items < 0:
    print("Invalid number of items")
    number_items = int(input("Number of items: "))

total_price = 0
for i in range(number_items):
    price_item = float(input("Price of item: "))
    total_price += price_item

if total_price > DISCOUNT_THRESHOLD:
    total_price -= total_price * DISCOUNT_RATE

print(f"Total price for {number_items} items is ${total_price:.2f}")