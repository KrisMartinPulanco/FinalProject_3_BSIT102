# Food Menu
menu = {
    'frappe': 15.0,
    'fruit tea': 10.0,
    'coffee': 12.0,
    'milktea': 8.0
}

# Display Menu
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")

# Order Selection
order = input("Please select an item from the menu: ")

# Check if the item is valid
if order not in menu:
    print("Invalid selection.")
else:
    total = menu[order]
    print(f"Total cost for {order}: ${total}")

    # Payment Processing
    while True:
        cash = float(input("Enter cash amount: "))
        if cash >= total:
            change = cash - total
            print(f"Payment accepted. Your change is ${change:.2f}")
            break
        else:
            print("Insufficient cash, please pay the full amount.")