class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMajor: {self.major}"


s1 = Student("Zahra", 20, "Computer Engineering")
print(s1)