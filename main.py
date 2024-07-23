class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}  # Dictionary to store courses and grades
        self.gpa = 0.0

    def register_for_course(self, course, grade=None):
        """Register the student for a course with an optional grade."""
        self.courses_registered[course.name] = grade

    def calculate_gpa(self):
        """Calculate the GPA of the student based on registered courses and grades."""
        total_credits = 0
        total_points = 0

        for course_name, grade in self.courses_registered.items():
            course = gradebook.get_course(course_name)
            if course and grade is not None:
                total_credits += course.credits
                total_points += grade * course.credits

        if total_credits > 0:
            self.gpa = total_points / total_credits

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

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
