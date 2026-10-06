"""Student Registration System - simple console module."""
 
students = []
 
 
def register_student(student_id, name, course):
    """Add a student after validating the input.
 
    Returns True if registered, False otherwise.
    """
    if not student_id or not name or not course:
        print("Error: All fields are required.")
        return False
    if any(s["id"] == student_id for s in students):
        print("Error: Student ID already exists.")
        return False
    students.append({"id": student_id, "name": name, "course": course})
    print(f"Student {name} registered successfully.")
    return True
 
 
def display_students():
    """Print all registered students."""
    if not students:
        print("No registered students.")
        return
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['course']}")
 
 
def main():
    register_student("2026-001", "Airon Alconcel", "BSCS")
    register_student("2026-002", "Mikaela Flamiano", "BSIT")
    register_student("2026-003", "Eden Asiong", "BSOA")  
    register_student("2026-004", "Edrich Caberoto", "BSBA") 
    display_students()
 
 
if __name__ == "__main__":
    main()

