class Student:
    def __init__(self,name,age,gpa):
        self.name=name
        self.age=age
        self.gpa=gpa
    def display(self):
        return f"Name {self.name},age {self.age},GPA {self.gpa}"
    
student=Student("Manasa",21,9.23)
print(student.display())
print(student.name)