from student_class import Student


def get_valid_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "" or not user_input.isalpha():
            print("Invalid input.")
            continue
        return user_input


def get_valid_index(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input == -1:
                return -1
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_age(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 17 or user_input >= 50:
                print("Student must be at least 17 years old and below 50.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid age.")


def get_valid_gender(prompt):
    while True:
        user_input = input(prompt).upper()
        if user_input in ["M", "F"]:
            return user_input
        print("Invalid gender. Please enter 'M' or 'F'.")


def get_valid_num_of_subjects(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input not in [7, 8]:
                print("Invalid input. Please enter a valid number of subjects.")
                continue
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_unique_subject(marks, subject):
    while True:
        if subject.lower() in (subject.lower() for subject in marks):
            print(
                f"Subject '{subject}' already exists. Please enter a unique subject name.")
            subject = input("Enter a different subject name: ")
        else:
            return subject


def get_valid_mark(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0 or user_input > 100:
                print("Invalid mark. Please enter a valid mark.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid mark.")


def get_valid_phone_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() != "n/a" and (len(user_input) < 8 or user_input.strip() == "" or not user_input.isdigit()):
            print("Invalid input. Please enter a valid phone number.")
            continue
        return user_input


def get_valid_student_ID(prompt):
    while True:
        student_id = input(prompt)
        if student_id == "-1":
            return -1
        elif student_id in {student.generate_student_ID() for student in Student.all_students}:
            return student_id
        else:
            print("Invalid student ID. Please try again.")
