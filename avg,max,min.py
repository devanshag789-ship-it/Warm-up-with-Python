# Calculating average, highest, and lowest numbers
def calculate_average(numbers):
    total = 0

    # Adding all numbers
    for num in numbers:
        total += num

    return total / len(numbers)


def find_highest_and_lowest(numbers):
    return max(numbers), min(numbers)


print("===== NUMBER STATISTICS =====")

# Taking numbers separated by commas
user_input = input("Enter numbers separated by commas: ")

try:
    data = [float(value.strip()) for value in user_input.split(",")]

    # Checking for empty entries
    if not data or any(value.strip() == "" for value in user_input.split(",")):
        print("Please enter valid numbers.")
    else:
        average = calculate_average(data)
        highest, lowest = find_highest_and_lowest(data)

        # Displaying the results
        print("\nNumbers:", data)
        print("Average:", round(average, 2))
        print("Highest:", highest)
        print("Lowest:", lowest)

except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")