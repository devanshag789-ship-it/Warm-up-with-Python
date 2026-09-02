# Printing the multiplication table of a number
def multiplication_table(number):
    print(f"\nMultiplication table of {number}")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Taking a number as input
try:
    num = int(input("Enter a positive number: "))

    if num > 0:
        multiplication_table(num)
    else:
        print("Please enter a positive number.")

except ValueError:
    print("Invalid input. Please enter a whole number.")