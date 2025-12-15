# File: 3.student.mark.oop.math.py

import math
import numpy as np
import sys
# Note: The 'curses' module is skipped for full UI in this environment, 
# but text-based decoration is used instead (ANSI escape codes).

# --- Base Classes ---

class Person:
    """A base class for people."""
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def list(self):
        """Displays base information."""
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}"

    def get_id(self):
        return self._id

class Course:
    """Represents a course with credits (for GPA calculation)."""
    def __init__(self, id, name, credits):
        self._id = id
        self._name = name
        self._credits = credits # New attribute for GPA calculation

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_credits(self):
        return self._credits

    def list(self):
        """Displays course information including credits."""
        return f"ID: {self._id}, Name: {self._name}, Credits: {self._credits}"

# STATIC .input() METHOD IS REMOVED/NOT USED TO AVOID LOGIC FLAW IN MANAGER

class Student(Person):
    """Represents a student with marks and GPA calculation."""
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        # Marks will be stored as {course_id: mark_value}
        self.marks = {}
        self._gpa = None # Encapsulation: store GPA after calculation

    def set_mark(self, course_id, mark):
        """Sets or updates a mark for a specific course (with floor rounding)."""
        # Use math.floor() to round down the score to 1-digit decimal
        rounded_mark = math.floor(mark * 10) / 10
        self.marks[course_id] = rounded_mark
        # Reset GPA when marks change
        self._gpa = None 

    def get_mark(self, course_id):
        """Retrieves a mark for a specific course."""
        return self.marks.get(course_id, "N/A")

    def calculate_gpa(self, all_courses):
        """
        Use numpy array to calculate weighted average GPA.
        GPA = (Sum of Mark * Credit) / (Sum of Credit)
        """
        
        marks_credits_data = []
        for course in all_courses:
            course_id = course.get_id()
            if course_id in self.marks:
                mark = self.marks[course_id]
                credit = course.get_credits()
                marks_credits_data.append((mark, credit))
        
        if not marks_credits_data:
            self._gpa = 0.0
            return 0.0

        # Convert to numpy array for efficient calculation
        data_array = np.array(marks_credits_data, dtype=[('mark', float), ('credit', int)])
        
        marks = data_array['mark']
        credits = data_array['credit']
        
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)

        if total_credits == 0:
            self._gpa = 0.0
        else:
            self._gpa = weighted_sum / total_credits
            self._gpa = round(self._gpa, 2) 

        return self._gpa

    def get_gpa(self, all_courses):
        """Returns stored GPA or calculates it if necessary."""
        if self._gpa is None:
            return self.calculate_gpa(all_courses)
        return self._gpa

    def list(self, include_gpa=False, all_courses=None):
        """Displays student info, optionally including GPA."""
        base_info = super().list()
        if include_gpa and all_courses is not None:
            gpa = self.get_gpa(all_courses)
            return f"{base_info}, GPA: {gpa:.2f}"
        return base_info

# --- Manager Class (Logic Fix Applied) ---

class StudentMarkManager:
    """Manages all students and courses."""
    def __init__(self):
        self._students = []
        self._courses = []
    def _get_number_of_items(item_type):
        """Helper to safely get the number of items to input."""
        while True:
            try:
                num = int(input(f"Enter number of {item_type} to input: "))
                if num >= 0:
                    return num
                else:
                    print("Number must be non-negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _get_unique_id(self, prompt, existing_items):
        """Helper to get a unique ID, checking against a list of existing items."""
        while True:
            item_id = input(prompt)
            if not item_id:
                print("ID cannot be empty.")
                continue
            if any(item.get_id() == item_id for item in existing_items):
                print(f"\033[91mError: ID '{item_id}' already exists.\033[0m Please enter a unique ID.")
                continue
            return item_id
            
    # --- Input Functions (Logic Fixed) ---

    def input_students(self):
        """Input number of students and their details, with unique ID validation."""
        num_students = self._get_number_of_items("students")
        temp_students = [] # To check for duplicates within the current batch

        for i in range(num_students):
            print(f"\n--- Input Student {i+1} Details ---")
            
            # Use the helper to get a unique ID against existing and current batch students
            all_current_students = self._students + temp_students
            student_id = self._get_unique_id("Enter student ID: ", all_current_students)
            
            # Get remaining details (no need for a static Student.input() now)
            student_name = input("Enter student Name: ")
            student_dob = input("Enter student Date of Birth (e.g., DD/MM/YYYY): ")
            
            new_student = Student(student_id, student_name, student_dob)
            temp_students.append(new_student)
            
        self._students.extend(temp_students)
        print(f"\n\033[92m{len(temp_students)} students added.\033[0m")

    def input_courses(self):
        """Input number of courses and their details, with unique ID and credits validation."""
        num_courses = self._get_number_of_items("courses")
        temp_courses = [] # To check for duplicates within the current batch

        for i in range(num_courses):
            print(f"\n--- Input Course {i+1} Details ---")
            
            # Use the helper to get a unique ID against existing and current batch courses
            all_current_courses = self._courses + temp_courses
            course_id = self._get_unique_id("Enter course ID: ", all_current_courses)
            
            # Get remaining details (no need for a static Course.input() now)
            course_name = input("Enter course Name: ")
            while True:
                try:
                    credits = int(input("Enter course Credits (integer): "))
                    if credits > 0:
                        break
                    else:
                        print("Credits must be a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter an integer for credits.")
            
            new_course = Course(course_id, course_name, credits)
            temp_courses.append(new_course)
            
        self._courses.extend(temp_courses)
        print(f"\n\033[92m{len(temp_courses)} courses added.\033[0m")


    def select_course_and_input_marks(self):
        """Select a course and input marks for all students, using math.floor()."""
        # ... (Rest of the logic is kept as it was correct for mark input and floor rounding) ...
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
                        print(f"   -> Mark recorded (floored to 1-digit): \033[93m{student.get_mark(course_id)}\033[0m")
                        break
                    else:
                        print("Mark must be between 0.0 and 20.0.")
                except ValueError:
                    print("Invalid input. Please enter a number for the mark.")
        
        print(f"\nMarks for course {selected_course.get_name()} recorded.")

    # --- Listing Functions (Kept as they were correct) ---

    def list_courses(self):
        """Lists all stored courses."""
        if not self._courses:
            print("No courses available.")
            return

        print("\n--- Course List (ID | Name | Credits) ---")
        for course in self._courses:
            print(course.list()) 

    def list_students(self):
        """Lists all stored students."""
        if not self._students:
            print("No students available.")
            return

        print("\n--- Student List (ID | Name | DoB) ---")
        for student in self._students:
            print(student.list())

    def sort_and_list_students_by_gpa(self):
        """Sort student list by GPA descending and list them."""
        if not self._students:
            print("No students available.")
            return
        if not self._courses:
            print("No courses available. Cannot calculate GPA without credits.")
            return

        for student in self._students:
            student.calculate_gpa(self._courses)

        sorted_students = sorted(
            self._students, 
            key=lambda s: s.get_gpa(self._courses), 
            reverse=True 
        )

        print("\n--- Student List Sorted by GPA (Descending) ---")
        print("{:<10} {:<20} {:<15} {:>5}".format("ID", "Name", "DoB", "\033[1;93mGPA\033[0m"))
        print("-" * 55)
        for student in sorted_students:
            gpa = student.get_gpa(self._courses)
            print("{:<10} {:<20} {:<15} {:>5.2f}".format(
                student.get_id(), 
                student._name, 
                student._dob, 
                gpa
            ))

    def show_student_marks_for_course(self):
        """Shows marks for all students in a given course."""
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

        print(f"\n--- Marks for Course: {selected_course.get_name()} (Credits: {selected_course.get_credits()}) ---")
        print("{:<10} {:<20} {:>5}".format("ID", "Name", "Mark"))
        print("-" * 35)

        found_marks = False
        for student in self._students:
            mark = student.get_mark(course_id)
            # Decorate the mark display
            mark_display = f"\033[93m{mark}\033[0m" if mark != "N/A" else mark
            print("{:<10} {:<20} {:>5}".format(student.get_id(), student._name, mark_display))
            if mark != "N/A":
                found_marks = True
        
        if not found_marks:
             print("\nNo marks have been recorded for this course yet.")

def display_menu():
    """Decorated menu display (text-based decoration with ANSI escape codes)."""
    print("\n\n" + "=" * 50)
    print("|\t\t\t\t\t\t |")
    print("|\t\033[1;36mSTUDENT MARK MANAGEMENT SYSTEM|\t\033[1;36m")
    print("|\t\t\t\t\t\t |")
    print("=" * 50)
    print("  --- \033[92mINPUT FUNCTIONS\033[0m ---")
    print("  1. Input number of students and their details")
    print("  2. Input number of courses and their details (\033[3mincluding credits\033[0m)")
    print("  3. Select a course and input marks (\033[3mfloored to 1-digit\033[0m)")
    print("  --- \033[92mLISTING & ANALYSIS FUNCTIONS\033[0m ---")
    print("  4. List courses")
    print("  5. List students (basic)")
    print("  6. Show student marks for a given course")
    print("  7. \033[93mSort and List students by GPA (Descending)\033[0m")
    print("  0. \033[91mExit\033[0m")
    print("=" * 50)

def main():
    """Main function to run the application."""
    manager = StudentMarkManager()

    while True:
        display_menu()
        choice = input("Enter your choice (0-7): ")

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
        elif choice == '7':
            manager.sort_and_list_students_by_gpa()
        elif choice == '0':
            print("\n\033[91mExiting Student Mark Management System. Goodbye!\033[0m")
            break
        else:
            print("\n\033[91mInvalid choice. Please enter a number between 0 and 7.\033[0m")

if __name__ == "__main__":
    main()