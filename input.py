def input_student():
    
    class_data = {"students":[
        
        ]
    }
    print("Enter the number of students in the class:")
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        id = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        DoB = input(f"Enter Date of Birth for student {i+1} (YYYY-MM-DD): ")
        student = {
            "id": id,
            "name": name,
            "DoB": DoB
        }
        class_data["students"].append(student)
    return class_data
def input_course():
    course_data = {"courses":[]}
    print("Enter the number of courses:")
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        course_id = input(f"Enter ID for course {i+1}: ")
        course_name = input(f"Enter name for course {i+1}: ")
        course = {
            "id": course_id,
            "name": course_name
        }
        course_data["courses"].append(course)
    return course_data
def input_marks(course_id, class_data):
    marks_data = {"marks":[]}
    print(f"Entering marks for course ID: {course_id}")
    for student in class_data["students"]:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        mark_entry = {
            "student_id": student["id"],
            "course_id": course_id,
            "mark": mark
        }
        marks_data["marks"].append(mark_entry)
    return marks_data