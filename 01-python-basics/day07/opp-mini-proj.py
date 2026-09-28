import json
import os

class Student:
    def __init__(self, student_id, name, email, gpa):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.gpa = gpa
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "gpa": self.gpa
        }
    
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}, GPA: {self.gpa}"

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_from_file()
    
    def load_from_file(self):
        """Load students from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for sid, info in data.items():
                        self.students[sid] = Student(**info)
            except json.JSONDecodeError:
                self.students = {}
    
    def save_to_file(self):
        """Save students to JSON file"""
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_student(self, student_id, name, email, gpa):
        """Add new student"""
        if student_id in self.students:
            print(f"Student {student_id} already exists!")
            return False
        self.students[student_id] = Student(student_id, name, email, gpa)
        self.save_to_file()
        print(f"Student {name} added successfully!")
        return True
    
    def view_all(self):
        """Display all students"""
        if not self.students:
            print("No students in system.")
            return
        for student in self.students.values():
            print(student)
    
    def search_by_id(self, student_id):
        """Search student by ID"""
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print(f"Student {student_id} not found.")
    
    def update_student(self, student_id, **kwargs):
        """Update student info"""
        if student_id not in self.students:
            print(f"Student {student_id} not found.")
            return
        s = self.students[student_id]
        for key, value in kwargs.items():
            if hasattr(s, key):
                setattr(s, key, value)
        self.save_to_file()
        print(f"Student {student_id} updated!")
    
    def delete_student(self, student_id):
        """Delete student"""
        if student_id in self.students:
            del self.students[student_id]
            self.save_to_file()
            print(f"Student {student_id} deleted!")
        else:
            print(f"Student {student_id} not found.")

def main():
    system = StudentManagementSystem()
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All")
        print("3. Search by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            sid = input("Student ID: ")
            name = input("Name: ")
            email = input("Email: ")
            gpa = float(input("GPA: "))
            system.add_student(sid, name, email, gpa)
        
        elif choice == '2':
            system.view_all()
        
        elif choice == '3':
            sid = input("Student ID: ")
            system.search_by_id(sid)
        
        elif choice == '4':
            sid = input("Student ID: ")
            print("Leave blank to skip a field")
            name = input("New name (optional): ") or None
            email = input("New email (optional): ") or None
            gpa_str = input("New GPA (optional): ")
            gpa = float(gpa_str) if gpa_str else None
            
            updates = {k: v for k, v in [('name', name), ('email', email), ('gpa', gpa)] if v}
            system.update_student(sid, **updates)
        
        elif choice == '5':
            sid = input("Student ID: ")
            system.delete_student(sid)
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()