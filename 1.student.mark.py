from input import input_student, input_course, input_marks
from list import list_student, list_course

print("Pls enter the student information:" )
class_data = input_student()   

print("\nPls enter the course information:" )
course_data = input_course()

print("\nPls enter the marks for each course:")
for course in course_data["courses"]:
    marks_data = input_marks(course["id"], class_data)

print("\nListing all students:")
list_student(class_data)

print("\nListing all courses:")
list_course(course_data)

print("\nMarks entered for each course:")
print(marks_data)