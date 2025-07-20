students = {}

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'Fail'

while True:
    print("Students Grade Management System")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice(1 to 4): ")
    if choice == '1':
        name = input("Enter student's name: ")
        marks = int(input("Enter student's marks: "))
        students[name] = marks
        print(f"{name} added successfully.")
    elif choice == '2':
        if not students:
            print("No student records are available.")
        else:
            print("\nName\tMarks\tGrade")
            print("-"*25)
            for name, marks in students.items():
                grade = calculate_grade(marks)
                print(f"{name}\t{marks}\t{grade}")
    elif choice == '3':
        search_name = input("Enter student's name to search: ")
        if search_name in students:
            marks = students[search_name]
            grade = calculate_grade(marks)
            print(f"Name: {search_name}, Marks: {marks}, Grade: {grade}")
        else:
            print(f"No record found for {search_name}.")
    elif choice == '4':
        print("Thank you! Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")