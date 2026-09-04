# Processing student marks and assigning grades
def process_student_data(students):
    for student in students:
        name = student["name"]
        marks = student["marks"]

        # Calculating percentage 
        percentage = (sum(marks) / (len(marks) * 100)) * 100

        # Assigning a grade based on percentage
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        print(f"Student: {name} | Grade: {grade} | Percentage: {percentage:.2f}%")

    print("\nAll student records processed successfully.")


students_list = [
    {"name": "Riya", "marks": [88, 92, 85]},
    {"name": "Arjun", "marks": [75, 64, 70]},
    {"name": "Meena", "marks": [55, 60, 58]}
]

# Processing and displaying the results
process_student_data(students_list)