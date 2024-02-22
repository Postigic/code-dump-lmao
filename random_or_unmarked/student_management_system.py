class Student:
    all_students = []

    def __init__(self, first_name, last_name, age, gender, school, cca, marks, phone_number):
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.school = school
        self.cca = cca
        self.marks = marks
        self.overall_marks = round(sum(marks.values()) / len(marks))
        self.phone_number = phone_number
        Student.all_students.append(self)

    def print_details(self):
        print(f"Student ID: {self.generate_student_ID()}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"School: {self.school}")
        print(f"Co-Curricular Activities: {self.cca}")
        print(f"Marks: {self.marks_str()}")
        print(
            f"Performance (Best to Worst): {self.display_subject_descending()}")
        print(f"Overall Marks: {self.overall_marks}")
        print(f"Overall Grade: {self.calculate_overall_grade()}")
        print(f"Ranking: {self.calculate_ranking()}")
        print(f"Email: {self.email()}")
        print(f"Phone Number: {self.phone_number}")
        print("\n-------------------------------\n")

    def generate_student_ID(self):
        string = (self.name + self.school).lower()
        letter_positions = [(ord(char) - 96) -
                            2 for char in string if char.isalpha()]
        letter_positions = [(pos + 25) if pos <
                            1 else pos for pos in letter_positions]
        return ''.join(str(pos) for pos in letter_positions)[:8]

    def email(self):
        return f"{self.name.lower().replace(' ', '_')}@gmail.com"

    def marks_str(self):
        return ', '.join([f"{subject}: {mark}" for subject, mark in self.marks.items()])

    def display_subject_descending(self):
        sorted_subjects = sorted(
            self.marks.keys(), key=lambda x: self.marks[x], reverse=True)
        return ', '.join(sorted_subjects)

    def calculate_overall_grade(self):
        if self.overall_marks >= 70:
            return "A"
        elif self.overall_marks >= 60:
            return "B"
        elif self.overall_marks >= 50:
            return "C"
        elif self.overall_marks >= 45:
            return "D"
        elif self.overall_marks >= 40:
            return "E"
        else:
            return "F"

    def calculate_ranking(self):
        sorted_students = sorted(
            Student.all_students, key=lambda x: x.overall_marks, reverse=True)
        return sorted_students.index(self) + 1


s1 = Student("Leona", "Palmer", 20, "Female", "Victoria Junior College", "Badminton", {
             "English": 90, "Maths": 88, "Science": 95, "Geography": 81, "Social Studies": 87, "Mother Tongue": 82}, "86972149")
s2 = Student("Bobby", "Gardner", 21, "Male", "Millenia Institute", "Infocomm", {
             "English": 67, "Maths": 75, "Science": 87, "History": 76, "Social Studies": 64, "Mother Tongue": 73}, "N/A")
s3 = Student("Jack", "Goodwin", 22, "Male", "Jurong Pioneers College", "Robotics", {
             "English": 68, "Maths": 87, "Science": 89, "Literature": 67, "Social Studies": 67, "Mother Tongue": 45}, "91081566")
s4 = Student("Carla", "Hicks", 23, "Female", "Catholic College", "Volleyball", {
             "English": 65, "Maths": 77, "Science": 78, "History": 89, "Social Studies": 67, "Mother Tongue": 88}, "99718770")


def main():
    while True:
        print("Welcome to the Student Management System!",
              end="\n\n-------------------------------\n\n")
        print("1. Add a new student")
        print("2. View student details")
        print("3. Exit")

        choice = input("Enter your choice: ")
        print("\n-------------------------------\n")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student_details()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_student():
    while True:
        print("1. Add a new student manually")
        print("2. Generate a random student")
        print("3. Go back")

        choice = input("Enter your choice: ")
        print("\n-------------------------------\n")

        if choice == "1":
            break
        elif choice == "2":
            generate_random_student()
            break
        elif choice == "3":
            main()

        else:
            print("Invalid choice. Please try again.")

    first_name = verify_string("Enter first name: ")
    last_name = verify_string("Enter last name: ")
    age = verify_integer("Enter age: ")
    gender = verify_gender("Enter gender (M, F): ")
    school = verify_string("Enter school: ")
    cca = verify_string("Enter co-curricular activity: ")
    marks = {}
    num_subjects = verify_num_of_subjects("Enter the number of subjects: ")
    for _ in range(num_subjects):
        subject = verify_string("Enter subject name: ")
        mark = verify_integer(f"Enter {subject} mark: ")
        marks[subject] = mark
    phone_number = verify_phone_number("Enter phone number: ")
    print("\n-------------------------------\n")

    new_student = Student(first_name, last_name, age,
                          gender, school, cca, marks, phone_number)
    print("Student added successfully!",
          end="\n\n-------------------------------\n\n")


def generate_random_student():
    pass


def view_student_details():
    student_index = int(input("Enter student index (1, 2, ...): "))
    print("\n-------------------------------\n")
    if 1 <= student_index <= len(Student.all_students):
        student = Student.all_students[student_index - 1]
        student.print_details()
    else:
        print("Invalid student index. Please try again.",
              end="\n\n-------------------------------\n\n")


def has_number(string):
    for char in string:
        if char.isdigit():
            return True
    return False


def verify_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "" or has_number(user_input):
            print("Invalid input.")
            continue
        return user_input


def verify_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
            print("Input must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def verify_gender(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ["M", "F"]:
            return user_input
        print("Invalid gender. Please enter 'M' or 'F'.")


def verify_num_of_subjects(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 6:
                return int(user_input)
            print("Invalid input. Please enter a valid number of subjects.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def verify_phone_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "" or (not user_input.isdigit() and user_input != "N/A"):
            print("Invalid input. Please enter a valid phone number.")
            continue
        return user_input


if __name__ == "__main__":
    main()
