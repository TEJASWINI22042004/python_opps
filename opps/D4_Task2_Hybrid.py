# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Child Class 1 (Single Inheritance)
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


# Child Class 2 (Single Inheritance)
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sport Name:", self.sport_name)


# Hybrid Inheritance (Multiple Inheritance)
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Person.__init__(self, name)
        self.student_id = student_id
        self.sport_name = sport_name
        self.college_name = college_name

    def display_college_student(self):
        print("College Name:", self.college_name)


# Creating Object
print("---- College Student Details ----")

student1 = CollegeStudent("Teja", 101, "Cricket", "ABC Engineering College")

student1.display_person()
student1.display_student()
student1.display_sports_player()
student1.display_college_student()