def list_student(class_data):
    print("List of students:")
    for student in class_data["students"]:
        print("Student name: {}, ID: {}, DoB: {}".format(student["name"], student["id"], student["DoB"]))
def list_course(course_data):
    print("List of courses:")
    for course in course_data["courses"]:
        print("Course name: {}, ID: {}".format(course["name"], course["id"]))