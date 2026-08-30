# Calculating the average of three numbers
def calculate_average(a, b, c):
    total = a + b + c
    return total / 3


print("===== AVERAGE CALCULATOR =====")

try:
    # Taking three numbers as input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calculating and displaying the average
    result = calculate_average(num1, num2, num3)
    print("Average:", round(result, 2))

except ValueError:
    print("Invalid input. Please enter valid numbers.")