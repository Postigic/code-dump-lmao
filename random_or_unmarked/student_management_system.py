import random

FIRST_NAMES = ["Rowan", "Riley", "Avery", "Logan", "Quinn", "Jordan", "River", "Cameron", "Angel", "Carter", "Ryan", "Dylan", "Noah", "Ezra", "Emery", "Hunter", "Kai", "August", "Nova",
               "Parker", "Arbor", "Ash", "Charlie", "Drew", "Ellis", "Everest", "Jett", "Lowen", "Moss", "Oakley", "Onyx", "Phoenix", "Ridley", "Remy", "Robin", "Royal", "Sage", "Scout", "Tatum", "Wren", "Monroe"]
LAST_NAMES = ["Vaughn", "Rios", "Smith", "Johnson", "Williams", "Jones", "Brown",
              "Davis", "Miller", "Sanders", "Kelly", "Boone", "Francis", "Martin", "Tyler", "Potter", "Hicks", "Goodwin", "Gardner", "Palmer"]
SCHOOLS = ["Victoria Junior College", "Millenia Institute", "Jurong Pioneers College", "Catholic Junior College",
           "Temasek Junior College", "River Valley High School", "Hwa Chong Institution", "Raffles Institution", "Dunman High School"]
CO_CURRICULAR_ACTIVITIES = ["Volleyball", "Media", "Infocomm", "Track and Field", "Badminton", "Table Tennis", "Hockey", "Floorball", "Basketball", "Soccer", "Choir", "Band", "Chinese Dance",
                            "Malay Dance", "Modern Dance", "Police National Cadet Corps", "Chinese Drama", "Chinese Orchestra", "Singapore Youth Flying Club"]


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
             "English": 90, "Mother Tongue": 82, "Maths": 88, "Pure Physics": 89, "Pure Chemistry": 95, "Geography/Social Studies": 87, "Additional Mathematics": 76, "Computing": 88}, "86972149")

s2 = Student("Bobby", "Gardner", 21, "Male", "Millenia Institute", "Infocomm", {
             "English": 67, "Mother Tongue": 73, "Maths": 75, "Biology/Chemistry": 87, "History/Social Studies": 66, "Design and Technology": 76, "Principles of Accounting": 78}, "N/A")

s3 = Student("Jack", "Goodwin", 22, "Male", "Jurong Pioneers College", "Hockey", {
             "English": 68, "Mother Tongue": 45, "Maths": 87, "Physics/Chemistry": 89, "Literature/Social Studies": 67, "Nutrition and Food Science": 76, "Principles of Accounting": 67}, "91081566")

s4 = Student("Carla", "Hicks", 23, "Female", "Catholic Junior College", "Volleyball", {
             "English": 65, "Mother Tongue": 88, "Maths": 77, "Physics/Biology": 88, "Pure History": 76, "Art": 69, "Design and Technology": 67}, "99718770")


# --------------------------------------------------------------------------------------------------------------------#
#
# INTERFACE FUNCTIONS
#
# --------------------------------------------------------------------------------------------------------------------#


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
            print("Thanks for using the Student Management System!")
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
            get_student_details()
            break
        elif choice == "2":
            generate_random_student()
            break
        elif choice == "3":
            main()

        else:
            print("Invalid choice. Please try again.")


def get_student_details():
    first_name = verify_string("Enter first name: ")
    last_name = verify_string("Enter last name: ")
    age = verify_age("Enter age: ")
    gender = verify_gender("Enter gender (M or F): ")
    school = verify_string("Enter school: ")
    cca = verify_string("Enter co-curricular activity: ")
    marks = {}
    num_subjects = verify_num_of_subjects(
        "Enter the number of subjects (7 or 8): ")
    for _ in range(num_subjects):
        subject = verify_string("Enter subject name: ")
        mark = verify_mark(f"Enter {subject} mark: ")
        marks[subject] = mark
    phone_number = verify_phone_number("Enter phone number (XXXXXXXX): ")
    print("\n-------------------------------\n")

    new_student = Student(first_name, last_name, age,
                          gender, school, cca, marks, phone_number)
    print("Student added successfully!",
          end="\n\n-------------------------------\n\n")


def view_student_details():
    student_index = int(
        input("Enter student index (1, 2, ..., -1 to go back): "))
    print("\n-------------------------------\n")
    if student_index == -1:
        main()
    if 1 <= student_index <= len(Student.all_students):
        student = Student.all_students[student_index - 1]
        student.print_details()
    else:
        print("Invalid student index. Please try again.",
              end="\n\n-------------------------------\n\n")


# --------------------------------------------------------------------------------------------------------------------#
#
# RANDOM STUDENT DETAILS GENERATION
#
# --------------------------------------------------------------------------------------------------------------------#


def generate_random_student():
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    age = random.randint(17, 25)
    gender = random.choice(["M", "F"])
    school = random.choice(SCHOOLS)
    cca = random.choice(CO_CURRICULAR_ACTIVITIES)
    marks = generate_random_marks()
    phone_number = generate_random_phone_number()

    new_student = Student(first_name, last_name, age,
                          gender, school, cca, marks, phone_number)
    print("Student added successfully!",
          end="\n\n-------------------------------\n\n")


def generate_random_marks():
    marks = {}
    marks["English"] = generate_subject_mark()
    marks["Mother Tongue"] = generate_subject_mark()
    marks["Maths"] = generate_subject_mark()

    marks.update(generate_science_marks())
    marks.update(generate_humanities_marks())
    marks.update(generate_coursework_non_coursework_marks())

    return marks


def generate_subject_mark():
    return random.randint(60, 100)


def generate_science_marks():
    COMBINED_SCIENCES = ["Physics/Chemistry",
                         "Physics/Biology", "Biology/Chemistry"]
    PURE_SCIENCES = ["Pure Physics", "Pure Chemistry", "Pure Biology"]

    science_type = random.choice(["combined", "pure"])
    if science_type == "combined":
        subject = random.choice(COMBINED_SCIENCES)
        return {subject: generate_subject_mark()}
    else:
        subjects = random.sample(PURE_SCIENCES, 2)
        return {subject: generate_subject_mark() for subject in subjects}


def generate_humanities_marks():
    HUMANITIES = ["Geography/Social Studies", "History/Social Studies",
                  "Literature/Social Studies", "Pure History", "Pure Literature"]
    subject = random.choice(HUMANITIES)
    return {subject: generate_subject_mark()}


def generate_coursework_non_coursework_marks():
    COURSEWORK_NON_COURSEWORK = ["Design and Technology", "Additional Mathematics",
                                 "Principles of Accounting", "Art", "Nutrition and Food Science", "Computing"]
    num_courses = random.choice([1, 2])
    subjects = random.sample(COURSEWORK_NON_COURSEWORK, num_courses)
    return {subject: generate_subject_mark() for subject in subjects}


def generate_random_phone_number():
    return f"{random.randint(6000, 9999)}{random.randint(1000, 9999)}"


# --------------------------------------------------------------------------------------------------------------------#
#
# ERROR CHECKING FUNCTIONS
#
# --------------------------------------------------------------------------------------------------------------------#


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


def verify_age(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 17 or user_input >= 50:
                print("Student must be at least 17 years old and below 50.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid age.")


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
            if user_input not in [7, 8]:
                print("Invalid input. Please enter a valid number of subjects.")
                continue
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def verify_mark(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0 or user_input > 100:
                print("Invalid mark. Please enter a valid mark.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid mark.")


def verify_phone_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "" or (not user_input.isdigit() and user_input != "N/A"):
            print("Invalid input. Please enter a valid phone number.")
            continue
        return user_input


# --------------------------------------------------------------------------------------------------------------------#
#
# --------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()
