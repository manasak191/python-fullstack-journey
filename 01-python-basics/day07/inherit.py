class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        return f"Name {self.name},age {self.age}"
    
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    
    def display(self):
        return f"{super().display()},ID {self.student_id}"
    
s=Student("Manasa",21,2025001)
print(s.display())