#Program to calculate the total shopping bill

def calculate_total(items):
    total = 0

    # Adding each item's price to the total
    for price in items:
        total += price

    return total


print("===== SHOPPING BILL CALCULATOR =====")
print("Enter the prices of your items.")
print("Type 'done' when you have finished.")

# Storing the prices entered by the user
shopping_list = []

while True:
    user_input = input("Enter item price: ₹").strip()

    # Stopping when the user types 'done'
    if user_input.lower() == "done":
        break

    try:
        price = float(user_input)

        if price < 0:
            print("Price cannot be negative.")
            continue

        shopping_list.append(price)

    except ValueError:
        print("Invalid input. Please enter a price or type 'done'.")

# Checking whether any prices were entered
if not shopping_list:
    print("No items entered. No bill to calculate.")
else:
    total = calculate_total(shopping_list)

    # Displaying the final bill
    print("\n----- BILL SUMMARY -----")
    print(f"Number of items: {len(shopping_list)}")
    print(f"Total bill: ₹{total:.2f}")