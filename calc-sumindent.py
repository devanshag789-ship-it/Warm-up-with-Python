# Calculate the sum of numbers and show each addition

def calculate_sum(numbers):
    total = 0

    for n in numbers:
        total += n
        print(f"Adding {n} -> Total: {total}")

    return total


# Taking numbers separated by commas
user_input = input("Enter numbers separated by commas: ")

try:
    nums = [float(n.strip()) for n in user_input.split(",")]

    # Checking for empty entries
    if not nums or any(n.strip() == "" for n in user_input.split(",")):
        print("Please enter valid numbers.")
    else:
        result = calculate_sum(nums)
        print("Total sum:", result)

except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")