from student import Student
from course import Course
from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Save Data")
        print("9. Load Data")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
            print("Course added successfully.")

        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade (0-4 scale, optional): "))
            gradebook.register_student_for_course(email, course_name, grade)
            print("Student registered for course successfully.")

        elif choice == '4':
            email = input("Enter student email: ")
            gradebook.calculate_gpa(email)
            print("GPA calculated successfully.")

        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            print("Student Ranking based on GPA:")
            for i, student in enumerate(ranking, 1):
                print(f"{i}. {student.names} (GPA: {student.gpa:.2f})")

        elif choice == '6':
            course_name = input("Enter course name: ")
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            results = gradebook.search_by_grade(course_name, min_grade, max_grade)
            print("Students with grades in the specified range:")
            for student in results:
                print(f"{student.names} (Grade: {student.courses_registered[course_name]})")

        elif choice == '7':
            email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(email)
            if transcript:
                print(transcript)
            else:
                print("Student not found.")

        elif choice == '8':
            filename = input("Enter filename to save data: ")
            gradebook.save_to_file(filename)
            print("Data saved successfully.")

        elif choice == '9':
            filename = input("Enter filename to load data: ")
            gradebook.load_from_file(filename)
            print("Data loaded successfully.")

        elif choice == '10':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
