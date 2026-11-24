"""Demonstrates the Student class."""

from student import Student


def main():
    s1 = Student("2023001", "Ali", "Yilmaz",
                 "2023001@std.neu.edu.tr", "Computer Engineering")
    s2 = Student("2023002", "Ayse", "Demir",
                 "2023002@std.neu.edu.tr", "Software Engineering")

    s1.enroll_course("Object Oriented Programming")
    s1.enroll_course("Data Structures")
    s1.enroll_course("Data Structures")   # already enrolled
    s1.set_gpa(3.45)

    s2.enroll_course("Software Design")
    s2.drop_course("Calculus")            # not enrolled
    s2.set_gpa(5.0)                       # invalid GPA
    s2.set_gpa(3.80)

    print()
    s1.display_info()
    s2.display_info()


if __name__ == "__main__":
    main()
