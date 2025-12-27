students = []
courses = []
marks = {}

def input_number_of_students():
    while True:
        try:
            return int(input("Enter number of students in the class: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_student_information():
    count = input_number_of_students()
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        s_id = input("  Enter student ID: ")
        s_name = input("  Enter student name: ")
        s_dob = input("  Enter student Date of Birth (DoB): ")
        
        student_data = {"id": s_id, "name": s_name, "dob": s_dob}
        students.append(student_data)

def input_number_of_courses():
    while True:
        try:
            return int(input("\nEnter number of courses: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_course_information():
    count = input_number_of_courses()
    for i in range(count):
        print(f"\n--- Course {i+1} ---")
        c_id = input("  Enter course ID: ")
        c_name = input("  Enter course name: ")
        
        course_data = {"id": c_id, "name": c_name}
        courses.append(course_data)

def input_marks():
    if not courses:
        print("\n[Error] No courses available. Add courses first.")
        return
    if not students:
        print("\n[Error] No students available. Add students first.")
        return

    list_courses()
    selected_cid = input("\nSelect a course ID to input marks for: ")

    found_course = False
    for c in courses:
        if c['id'] == selected_cid:
            found_course = True
            break
    
    if not found_course:
        print("[Error] Course ID not found.")
        return
    
    if selected_cid not in marks:
        marks[selected_cid] = {}

    print(f"\nEntering marks for course: {selected_cid}")
    for s in students:
        while True:
            try:
                score = float(input(f"  Enter mark for {s['name']} (ID: {s['id']}): "))
                marks[selected_cid][s['id']] = score
                break
            except ValueError:
                print("  Invalid input. Please enter a numerical mark.")

def list_courses():
    print("\n--- List of Courses ---")
    if not courses:
        print("No courses available.")
    else:
        for c in courses:
            print(f"ID: {c['id']}, Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    if not students:
        print("No students available.")
    else:
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def show_student_marks():
    if not marks:
        print("\nNo marks recorded yet.")
        return

    list_courses()
    target_cid = input("\nEnter course ID to show marks: ")

    if target_cid not in marks:
        print(f"[Error] No marks found for course ID: {target_cid}")
        return

    print(f"\n--- Marks for Course ID: {target_cid} ---")
    for s_id, score in marks[target_cid].items():
        # Find student name from ID for better readability
        name = "Unknown"
        for s in students:
            if s['id'] == s_id:
                name = s['name']
                break
        print(f"Student: {name} (ID: {s_id}), Mark: {score}")

# --- Main Program Loop ---

def main():
    while True:
        print("\n==================================")
        print(" STUDENT MARK MANAGEMENT SYSTEM ")
        print("==================================")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            input_student_information()
        elif choice == '2':
            input_course_information()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()