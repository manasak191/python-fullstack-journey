import json
import os

class Student:
    def __init__(self,student_id,name,email,gpa):
        self.student_id=student_id
        self.name=name
        self.email=email
        self.gpa=gpa
        
    def to_dict(self):  #JSON DATA
        return {
            "student_id":self.student_id,
            "name":self.name,
            "email":self.email,
            "gpa":self.gpa
        }
        
    def __str__(self):
        return f"ID: {self.student_id},Name: {self.name}, Email {self.email}, GPA: {self.gpa}"

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename=filename
        self.students={}
        self.load_from_file()
        
    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,'r') as f:
                    data=json.load(f)
                    for sid,info in data.items():
                        self.students[sid]=Student(**info)
            except json.JSONDecodeError:
                self.student={}
                
    def save_to_file(Self):
        data={sid:s.to_dict() for sid,s in self.students.items()}
        
        with open(self.filename,'w') as f:
            json.dump(data,f,indent=2)
            
    def add_student(self,student_id,name,email,gpa):
        if student_id in self.students:
            print(f"student {student_id} already exists!")
            return False
        self.students[student_id]=Student(student_id,name,email,gpa)
        self.save_to_file()
        print(f"Student {name} added successfully!")
        return True
    
    def view_all(self):