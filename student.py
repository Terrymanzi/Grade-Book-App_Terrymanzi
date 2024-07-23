#!/usr/bin/python3
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
