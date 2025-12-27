class Person:
    """A base class for people, demonstrating a common structure."""
    def __init__(self, id, name, dob):
        self._id = id       
        self._name = name
        self._dob = dob

    def list(self):
        """Illustrates a polymorphic list/display method."""
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}"

    def get_id(self):
        return self._id

class Student(Person):
    """Represents a student with marks for various courses."""
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.marks = {}

    def set_mark(self, course_id, mark):
        """Sets or updates a mark for a specific course."""
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        """Retrieves a mark for a specific course."""
        return self.marks.get(course_id, "N/A")

    def list(self):
        """Overrides list to include the base info."""
        return super().list()

    @staticmethod
    def input():
        """Illustrates a polymorphic input method (as a class method for creation)."""
        while True:
            student_id = input("Enter student ID: ")
            if student_id: break
            print("ID cannot be empty.")
        student_name = input("Enter student Name: ")
        student_dob = input("Enter student Date of Birth (e.g., DD/MM/YYYY): ")
        return Student(student_id, student_name, student_dob)

class Course:
    """Represents a course."""
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def list(self):
        """Illustrates a polymorphic list/display method."""
        return f"ID: {self._id}, Name: {self._name}"

    @staticmethod
    def input():
        """Illustrates a polymorphic input method (as a class method for creation)."""
        while True:
            course_id = input("Enter course ID: ")
            if course_id: break
            print("ID cannot be empty.")
        course_name = input("Enter course Name: ")
        return Course(course_id, course_name)

class StudentMarkManager:
    """
    Manages all students and courses.
    Acts as the main controller, demonstrating proper encapsulation 
    by controlling access to student and course lists.
    """
    def __init__(self):
        # Encapsulation: internal storage for data
        self._students = []
        self._courses = []

    # --- Input Functions ---

    def input_students(self):
        """Input number of students and their details."""
        while True:
            try:
                num_students = int(input("Enter number of students in the class: "))
                if num_students >= 0:
                    break
                else:
                    print("Number must be non-negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(num_students):
            print(f"\n--- Input Student {i+1} Details ---")
            new_student = Student.input()
            # Check for ID uniqueness (simple check for demonstration)
            if any(s.get_id() == new_student.get_id() for s in self._students):
                print(f"Warning: Student with ID {new_student.get_id()} already exists. Skipping.")
                continue
            self._students.append(new_student)
        print(f"\n{len(self._students)} students added.")

    def input_courses(self):
        """Input number of courses and their details."""
        while True:
            try:
                num_courses = int(input("Enter number of courses: "))
                if num_courses >= 0:
                    break
                else:
                    print("Number must be non-negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(num_courses):
            print(f"\n--- Input Course {i+1} Details ---")
            new_course = Course.input()
            # Check for ID uniqueness
            if any(c.get_id() == new_course.get_id() for c in self._courses):
                print(f"Warning: Course with ID {new_course.get_id()} already exists. Skipping.")
                continue
            self._courses.append(new_course)
        print(f"\n{len(self._courses)} courses added.")

    def select_course_and_input_marks(self):
        """Select a course and input marks for all students in that course."""
        if not self._courses:
            print("No courses available. Please input courses first.")
            return
        if not self._students:
            print("No students available. Please input students first.")
            return

        print("\n--- Available Courses ---")
        self.list_courses()

        course_id = input("Enter the ID of the course to input marks for: ")
        selected_course = next((c for c in self._courses if c.get_id() == course_id), None)

        if not selected_course:
            print(f"Error: Course with ID '{course_id}' not found.")
            return

        print(f"\n--- Input Marks for Course: {selected_course.get_name()} ---")
        
        for student in self._students:
            while True:
                try:
                    mark = float(input(f"Enter mark for student {student.get_id()} ({student._name}): "))
                    if 0.0 <= mark <= 20.0:  # Assuming marks are 0-20
                        student.set_mark(course_id, mark)
                        break
                    else:
                        print("Mark must be between 0.0 and 20.0.")
                except ValueError:
                    print("Invalid input. Please enter a number for the mark.")
        
        print(f"\nMarks for course {selected_course.get_name()} recorded.")

    def list_courses(self):
        if not self._courses:
            print("No courses available.")
            return

        print("\n--- Course List ---")
        for course in self._courses:
            print(course.list()) # Polymorphism: calling .list() on Course object

    def list_students(self):
        if not self._students:
            print("No students available.")
            return

        print("\n--- Student List ---")
        for student in self._students:
            print(student.list()) 

    def show_student_marks_for_course(self):
        if not self._courses:
            print("No courses available. Please input courses first.")
            return
        if not self._students:
            print("No students available. Please input students first.")
            return

        print("\n--- Available Courses ---")
        self.list_courses()

        course_id = input("Enter the ID of the course to show marks for: ")
        selected_course = next((c for c in self._courses if c.get_id() == course_id), None)

        if not selected_course:
            print(f"Error: Course with ID '{course_id}' not found.")
            return

        print(f"\n--- Marks for Course: {selected_course.get_name()} ---")
        print("{:<10} {:<20} {:>5}".format("ID", "Name", "Mark"))
        print("-" * 35)

        found_marks = False
        for student in self._students:
            mark = student.get_mark(course_id)
            print("{:<10} {:<20} {:>5}".format(student.get_id(), student._name, mark))
            if mark != "N/A":
                found_marks = True
        
        if not found_marks:
             print("\nNo marks have been recorded for this course yet.")


def display_menu():
    print("      Student Mark Management System    ")
    print("  --- Input Functions ---")
    print("  1. Input number of students and their details")
    print("  2. Input number of courses and their details")
    print("  3. Select a course and input marks")
    print("  --- Listing Functions ---")
    print("  4. List courses")
    print("  5. List students")
    print("  6. Show student marks for a given course")
    print("  0. Exit")
    print("==============================================")

def main():
    """Main function to run the application."""
    manager = StudentMarkManager()

    while True:
        display_menu()
        choice = input("Enter your choice (0-6): ")

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.input_courses()
        elif choice == '3':
            manager.select_course_and_input_marks()
        elif choice == '4':
            manager.list_courses()
        elif choice == '5':
            manager.list_students()
        elif choice == '6':
            manager.show_student_marks_for_course()
        elif choice == '0':
            print("Exiting Student Mark Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()