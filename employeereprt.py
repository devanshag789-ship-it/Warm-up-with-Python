# Generating an employee performance report

def generate_employee_report(employees):
    print("\n===== EMPLOYEE PERFORMANCE REPORT =====")

    for emp in employees:
        name = emp["name"]
        ratings = emp["ratings"]

        # Checking whether ratings are available
        if not ratings:
            print(f"\nEmployee: {name}")
            print("Average rating: Not available")
            print("Status: No ratings provided")
            continue

        average = sum(ratings) / len(ratings)

        # Assigning a status based on the average rating
        if average >= 9:
            status = "Outstanding"
        elif average >= 7.5:
            status = "Very Good"
        elif average >= 6:
            status = "Good"
        else:
            status = "Needs Improvement"

        print(f"\nEmployee: {name}")
        print(f"Ratings: {ratings}")
        print(f"Average rating: {average:.2f}/10")
        print(f"Performance: {status}")
        print("-" * 35)


# Sample employee data
employees_data = [
    {"name": "Rohan", "ratings": [9, 8.5, 9.2]},
    {"name": "Sneha", "ratings": [7, 7.5, 8]},
    {"name": "Aarav", "ratings": [5.5, 6, 6.2]}
]

# Generating the report
generate_employee_report(employees_data)