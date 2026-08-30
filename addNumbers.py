# Adding two numbers
def add_numbers(a, b):
    return a + b


print("===== ADD TWO NUMBERS =====")

try:
    # Taking two numbers as input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculating and displaying the sum
    result = add_numbers(num1, num2)
    print(f"The sum is: {result:g}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")