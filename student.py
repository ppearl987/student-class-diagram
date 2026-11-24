"""
Student class mapped from the Student UML class diagram.

Private attributes (-) are written with a leading double underscore and
accessed through public (+) methods, following the encapsulation principle.
"""


class Student:
    def __init__(self, student_id, first_name, last_name, email, department):
        # ---------- Attributes (private) ----------
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__department = department
        self.__gpa = 0.0
        self.__courses = []

    # ---------- Getters ----------
    def get_student_id(self):
        return self.__student_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_department(self):
        return self.__department

    def get_gpa(self):
        return self.__gpa

    def get_courses(self):
        return list(self.__courses)

    # ---------- Setters ----------
    def set_email(self, email):
        self.__email = email

    def set_department(self, department):
        self.__department = department

    def set_gpa(self, gpa):
        if gpa < 0.0 or gpa > 4.0:
            print("Invalid GPA! It must be between 0.0 and 4.0.")
            return
        self.__gpa = gpa

    # ---------- Operations ----------
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def enroll_course(self, course):
        if course in self.__courses:
            print(f"{self.get_full_name()} is already enrolled in {course}.")
        else:
            self.__courses.append(course)
            print(f"{self.get_full_name()} enrolled in {course}.")

    def drop_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            print(f"{self.get_full_name()} dropped {course}.")
        else:
            print(f"{self.get_full_name()} is not enrolled in {course}.")

    def display_info(self):
        courses = ", ".join(self.__courses) if self.__courses else "None"
        print("----- Student Information -----")
        print(f"ID         : {self.__student_id}")
        print(f"Name       : {self.get_full_name()}")
        print(f"Email      : {self.__email}")
        print(f"Department : {self.__department}")
        print(f"GPA        : {self.__gpa}")
        print(f"Courses    : {courses}")
        print("-------------------------------")
