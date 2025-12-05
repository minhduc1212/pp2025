class Student:
    def __init__(self, name, id, DoB):
        self.name = name
        self.id = id
        self.DoB = DoB
        
    #getter and setter
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_DoB(self):
        return self.DoB
    def set_DoB(self, DoB):
        self.DoB = DoB
        
    #input and list
    def input(self, name, id, DoB):
        self.set_name(name)
        self.set_id(id)
        self.set_DoB(DoB)
    def list(self):
        print("Student name: {}, ID: {}, DoB: {}".format(self.get_name(), self.get_id(), self.get_DoB()))



class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    #getter and setter
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id

    #input and list
    def input(self, id, name):
        self.set_name(name)
        self.set_id(id)
    def list(self):
        print("Course name: {}, ID: {}".format(self.get_name(), self.get_id()))

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark
        
    #getter and setter
    def get_student_id(self):
        return self.student_id
    def set_student_id(self, student_id):
        self.student_id = student_id
    def get_course_id(self):
        return self.course_id
    def set_course_id(self, course_id):
        self.course_id = course_id
    def get_mark(self):
        return self.mark
    def set_mark(self, mark):
        self.mark = mark
        
    #input and list
    def input(self, student_id, course_id, mark):
        self.set_student_id(student_id)
        self.set_course_id(course_id)
        self.set_mark(mark)
    def list(self):
        print("Student ID: {}, Course ID: {}, Mark: {}".format(self.get_student_id(), self.get_course_id(), self.get_mark()))


def main():
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        id = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        DoB = input(f"Enter Date of Birth for student {i+1} (YYYY-MM-DD): ")
        student = Student(name, id, DoB)
        student.input(name, id, DoB)
        students.append(student)

    num_courses = int(input("Enter number of courses: "))
    courses = []
    for i in range(num_courses):
        id = input(f"Enter ID for course {i+1}: ")
        name = input(f"Enter name for course {i+1}: ")
        course = Course(id, name)
        course.input(id, name)
        courses.append(course)

    marks = []

    # Select a course and input marks for students in that course
    while True:
        course_id_to_mark = input("Enter the ID of the course to input marks: ")
        if course_id_to_mark.lower() == 'done':
            break

        # Check if the course exists
        found_course = False
        for course in courses:
            if course.get_id() == course_id_to_mark:
                found_course = True
                print(f"Inputting marks for course: {course.get_name()} (ID: {course.get_id()})")
                for student in students:
                    student_mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}) in course {course.get_name()}: "))
                    mark = Mark(student.get_id(), course.get_id(), student_mark)
                    marks.append(mark)
                break
        if not found_course:
            print("Course not found. Please enter a valid course ID.")
        
    #list
    for student in students:
        student.list()  
    for course in courses:
        course.list()
    course_id_to_list = input("Enter the ID of the course to list: ")
    for mark in marks:
        if mark.get_course_id() == course_id_to_list:
            mark.list()
    
if __name__ == "__main__":
    main()