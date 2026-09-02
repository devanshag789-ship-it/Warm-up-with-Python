# Calculating the final price after discount
def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        print("Discount must be between 0 and 100.")
        return None

    discount_amount = price * discount / 100
    return price - discount_amount


print("===== DISCOUNT CALCULATOR =====")

try:
    # Taking the original price and discount percentage
    price = float(input("Enter the original price: ₹"))
    discount = float(input("Enter discount percentage: "))

    if price < 0:
        print("Price cannot be negative.")
    else:
        final_price = calculate_discount(price, discount)

        if final_price is not None:
            # Displaying the discount summary
            print("\nOriginal price: ₹{:.2f}".format(price))
            print("Discount: {}%".format(discount))
            print("You save: ₹{:.2f}".format(price - final_price))
            print("Final price: ₹{:.2f}".format(final_price))

except ValueError:
    print("Invalid input. Please enter valid numbers.")