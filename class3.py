class Course:
    courses = []

    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
        self.students = []
        Course.courses.append(self)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Name: {self.name}\nProfessor: {self.professor}"


class Student:
    students = []

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.courses = []
        self.grades = {}
        Student.students.append(self)

    def change_major(self, new_major):
        self.major = new_major

    def add_course(self, course):
        self.courses.append(course)
        course.add_student(self)

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMajor: {self.major}"


c1 = Course("Python", "Professor1")
c2 = Course("Java", "Professor2")

s1 = Student("Fatemeh", 20, "Civil Engineering")
s2 = Student("Ali", 21, "Finance")

s1.add_course(c1)
s1.add_course(c2)
s2.add_course(c1)

s1.add_grade(c1, 20)
s1.add_grade(c2, 19)
s2.add_grade(c1, 9)


c1_average = 0
c2_average = 0
for s in Student.students:
    if c1 in s.courses:
        c1_average += s.grades[c1]
    if c2 in s.courses:
        c2_average += s.grades[c2]

c1_average /= len(c1.students)
c2_average /= len(c2.students)

print(f"Average of {c1.name}: {c1_average}")
print(f"Average of {c2.name}: {c2_average}")
