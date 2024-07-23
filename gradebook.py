import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        """Add a student to the grade book."""
        self.student_list.append(student)

    def add_course(self, course):
        """Add a course to the grade book."""
        self.course_list.append(course)

    def get_course(self, course_name):
        """Retrieve a course object by its name."""
        for course in self.course_list:
            if course.name == course_name:
                return course
        return None

    def register_student_for_course(self, student_email, course_name, grade=None):
        """Register a student for a course and assign a grade."""
        student = self.get_student(student_email)
        course = self.get_course(course_name)

        if student and course:
            student.register_for_course(course, grade)

    def calculate_gpa(self, student_email):
        """Calculate GPA for a student."""
        student = self.get_student(student_email)
        if student:
            student.calculate_gpa()

    def calculate_ranking(self):
        """Calculate the ranking of students based on their GPA."""
        self.student_list.sort(key=lambda student: student.gpa, reverse=True)
        return self.student_list

    def search_by_grade(self, course_name, min_grade, max_grade):
        """Search for students who obtained a grade in the specified range for a course."""
        results = []
        for student in self.student_list:
            if course_name in student.courses_registered:
                grade = student.courses_registered[course_name]
                if min_grade <= grade <= max_grade:
                    results.append(student)
        return results

    def generate_transcript(self, student_email):
        """Generate a transcript for a student showing their GPA and courses."""
        student = self.get_student(student_email)
        if student:
            transcript = f"Transcript for {student.names} ({student.email}):\n"
            transcript += "Courses:\n"
            for course_name, grade in student.courses_registered.items():
                transcript += f"  {course_name}: {grade}\n"
            transcript += f"GPA: {student.gpa:.2f}\n"
            return transcript
        return None

    def get_student(self, email):
        """Retrieve a student object by their email."""
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def save_to_file(self, filename):
        """Save the grade book data to a file."""
        data = {
            "students": [
                {
                    "email": student.email,
                    "names": student.names,
                    "courses_registered": student.courses_registered,
                    "gpa": student.gpa,
                }
                for student in self.student_list
            ],
            "courses": [
                {
                    "name": course.name,
                    "trimester": course.trimester,
                    "credits": course.credits,
                }
                for course in self.course_list
            ],
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        """Load the grade book data from a file."""
        with open(filename, 'r') as file:
            data = json.load(file)

        self.student_list = [
            Student(student["email"], student["names"])
            for student in data["students"]
        ]
        for student, student_data in zip(self.student_list, data["students"]):
            student.courses_registered = student_data["courses_registered"]
            student.gpa = student_data["gpa"]

        self.course_list = [
            Course(course["name"], course["trimester"], course["credits"])
            for course in data["courses"]
        ]
