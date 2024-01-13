class Student:
    def __init__(self, name, age, major, gender):
        self.name = name
        self.age = age
        self.major = major
        self.gender = gender

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        if self.gender == "male":
            return f"He is {self.name}\nAge: {self.age}\nMajor: {self.major}"
        else  
            return f"She is {self.name}\nAge: {self.age}\nMajor: {self.major}"


s1 = Student("Zahra", 20, "Computer Engineering")
print(s1)
