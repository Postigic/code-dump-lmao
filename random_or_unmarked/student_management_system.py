import random

FIRST_NAMES = ["Rowan", "Riley", "Avery", "Logan", "Quinn", "Jordan", "River", "Cameron", "Angel", "Carter", "Ryan", "Dylan", "Noah", "Ezra", "Emery", "Hunter", "Kai", "August", "Nova",
               "Parker", "Arbor", "Ash", "Charlie", "Drew", "Ellis", "Everest", "Jett", "Lowen", "Moss", "Oakley", "Onyx", "Phoenix", "Ridley", "Remy", "Robin", "Royal", "Sage", "Scout", "Tatum", "Wren", "Monroe"]
LAST_NAMES = ["Vaughn", "Rios", "Smith", "Johnson", "Williams", "Jones", "Brown",
              "Davis", "Miller", "Sanders", "Kelly", "Boone", "Francis", "Martin", "Tyler", "Potter", "Hicks", "Goodwin", "Gardner", "Palmer"]
SCHOOLS = ["Victoria Junior College", "Millenia Institute", "Jurong Pioneers College", "Catholic Junior College",
           "Temasek Junior College", "River Valley High School", "Hwa Chong Institution", "Raffles Institution", "Dunman High School"]
CO_CURRICULAR_ACTIVITIES = ["Volleyball", "Media", "Infocomm", "Track and Field", "Badminton", "Table Tennis", "Hockey", "Floorball", "Basketball", "Soccer", "Choir", "Band", "Chinese Dance",
                            "Malay Dance", "Modern Dance", "Police National Cadet Corps", "Chinese Drama", "Chinese Orchestra", "Singapore Youth Flying Club"]


# -------------------------------------------------------------------------------------------------------------------- #
#
# MAIN CODE
#
# -------------------------------------------------------------------------------------------------------------------- #


class Student:
    all_students = []

    def __init__(self, first_name, last_name, age, gender, school, cca, marks, phone_number):
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.school = school
        self.cca = cca
        self.marks = marks
        self.overall_marks = round(sum(self.marks.values()) / len(self.marks))
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

    def update_student_details(self):
        self.overall_marks = round(sum(self.marks.values()) / len(self.marks))
        self.grade = self.calculate_overall_grade()
        self.ranking = self.calculate_ranking()

    def generate_student_ID(self):
        string = (self.name + self.school).lower()
        letter_positions = [(ord(char) - 96) -
                            2 for char in string if char.isalpha()]
        letter_positions = [(pos + 25) if pos <
                            1 else pos for pos in letter_positions]
        student_id = ''.join(str(pos) for pos in letter_positions)[:8]
        if len(student_id) < 8:
            student_id = student_id.zfill(8)
        return student_id

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


# -------------------------------------------------------------------------------------------------------------------- #
#
# INTERFACE FUNCTIONS
#
# -------------------------------------------------------------------------------------------------------------------- #


def main():
    while True:
        print("Welcome to the Student Management System!",
              end="\n\n-------------------------------\n\n")
        print("1. Add a new student")
        print("2. View student details")
        print("3. Exit")

        choice = input("\nEnter your choice: ")
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
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")


def add_student():
    while True:
        print("1. Add a new student manually")
        print("2. Generate a random student")
        print("3. Go back")

        choice = input("\nEnter your choice: ")
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
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def view_student_details():
    while True:
        print("1. View a student's details")
        print("2. Edit a student's details")
        print("3. Delete a student's details")
        print("4. Go back")

        choice = input("\nEnter your choice: ")
        print("\n-------------------------------\n")

        if choice == "1":
            print_student_details()

        elif choice == "2":
            edit_student_details()
        elif choice == "3":
            delete_student_details()
        elif choice == "4":
            main()
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def get_student_details():
    first_name = get_valid_string("Enter first name: ")
    last_name = get_valid_string("Enter last name: ")
    age = get_valid_age("Enter age: ")
    gender = get_valid_gender("Enter gender (M or F): ")
    school = get_valid_string("Enter school: ")
    cca = get_valid_string("Enter co-curricular activity: ")
    marks = {}
    num_subjects = get_valid_num_of_subjects(
        "Enter the number of subjects (7 or 8): ")
    for _ in range(num_subjects):
        subject = get_valid_string("Enter subject name: ")
        subject = get_valid_unique_subject(marks, subject)
        mark = get_valid_mark(f"Enter {subject} mark: ")
        marks[subject] = mark
    phone_number = get_valid_phone_number("Enter phone number (XXXXXXXX): ")
    print("\n-------------------------------\n")

    new_student = Student(first_name, last_name, age,
                          gender, school, cca, marks, phone_number)
    print("Student added successfully!",
          end="\n\n-------------------------------\n\n")


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


def print_student_details():
    while True:
        for i, student in enumerate(Student.all_students, start=1):
            print(f"{i}. ID: {student.generate_student_ID()} — {student.name}")
        student_index = get_valid_index(
            "\nEnter student index (1, 2, ..., -1 to go back): ")
        print("\n-------------------------------\n")
        if student_index == -1:
            view_student_details()
        if 1 <= student_index <= len(Student.all_students):
            student = Student.all_students[student_index - 1]
            student.print_details()
        else:
            print("Invalid student index. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def edit_student_details():
    while True:
        for i, student in enumerate(Student.all_students, start=1):
            print(f"{i}. ID: {student.generate_student_ID()} — {student.name}")
        student_index = get_valid_index(
            "\nEnter student index (1, 2, ..., -1 to go back): ")
        print("\n-------------------------------\n")
        if student_index == -1:
            view_student_details()
        if 1 <= student_index <= len(Student.all_students):
            student = Student.all_students[student_index - 1]
            edit_student(student)
            break
        else:
            print("Invalid student index. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def edit_student(student):
    print("Current Details:", end="\n\n")
    student.print_details()

    while True:
        print("What would you like to edit?", end="\n\n")
        print("1. Name")
        print("2. Age")
        print("3. Gender")
        print("4. School")
        print("5. Co-Curricular Activities")
        print("6. Marks")
        print("7. Phone Number")
        print("8. Exit")

        choice = input("\nEnter your choice: ")
        print("\n-------------------------------\n")

        if choice == "1":
            edit_name(student)
        elif choice == "2":
            edit_age(student)
        elif choice == "3":
            edit_gender(student)
        elif choice == "4":
            edit_school(student)
        elif choice == "5":
            edit_cca(student)
        elif choice == "6":
            edit_marks(student)
        elif choice == "7":
            edit_phone_number(student)
        elif choice == "8":
            print("Exiting editing mode.",
                  end="\n\n-------------------------------\n\n")
            break
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")


def edit_name(student):
    new_name = get_valid_string("Enter new name: ")
    student.name = new_name
    print("\n-------------------------------\n")
    print("Name updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_age(student):
    new_age = get_valid_age("Enter new age: ")
    student.age = new_age
    print("\n-------------------------------\n")
    print("Age updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_gender(student):
    new_gender = get_valid_gender("Enter new gender (M or F): ")
    student.gender = new_gender
    print("\n-------------------------------\n")
    print("Gender updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_school(student):
    new_school = get_valid_string("Enter new school: ")
    student.school = new_school
    print("\n-------------------------------\n")
    print("School updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_cca(student):
    new_cca = get_valid_string("Enter new co-curricular activity: ")
    student.cca = new_cca
    print("\n-------------------------------\n")
    print("Co-Curricular Activities updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_marks(student):
    print(f"Current Marks: {student.marks_str()}", end="\n\n")
    print("1. Edit subject")
    print("2. Edit mark")
    edit_choice = input("\nEnter your choice: ")
    print("\n-------------------------------\n")

    if edit_choice == "1":
        edit_subject(student)
    elif edit_choice == "2":
        edit_mark(student)
    else:
        print("Invalid choice. Please try again.")


def edit_subject(student):
    subject_to_edit = input("Enter the subject you want to edit: ")
    if subject_to_edit in student.marks:
        new_subject = get_valid_string(
            "Enter the new subject name: ")
        new_subject = get_valid_unique_subject(
            student.marks, new_subject)
        student.marks[new_subject] = student.marks.pop(
            subject_to_edit)
        print("\n-------------------------------\n")
        print(f"Subject updated successfully!",
              end="\n\n-------------------------------\n\n")
    else:
        print("\n-------------------------------\n")
        print(f"Subject '{subject_to_edit}' not found in marks.",
              end="\n\n-------------------------------\n\n")


def edit_mark(student):
    subject_to_edit = input(
        "Enter the subject for which you want to edit the mark: ")
    if subject_to_edit in student.marks:
        new_mark = get_valid_mark(
            f"Enter new mark for {subject_to_edit}: ")
        student.marks[subject_to_edit] = new_mark
        student.update_student_details()
        print("\n-------------------------------\n")
        print(f"Mark for {subject_to_edit} updated successfully!")
    else:
        print("\n-------------------------------\n")
        print(f"Subject '{subject_to_edit}' not found in marks.")


def edit_phone_number(student):
    new_phone_number = get_valid_phone_number(
        "Enter new phone number (XXXXXXXX): ")
    student.phone_number = new_phone_number
    print("\n-------------------------------\n")
    print("Phone number updated successfully!",
          end="\n\n-------------------------------\n\n")


def delete_student_details():
    for i, student in enumerate(Student.all_students, start=1):
        print(f"{i}. ID: {student.generate_student_ID()} — {student.name}")
    student_index = get_valid_index(
        "\nEnter student index (1, 2, ..., -1 to go back): ")
    print("\n-------------------------------\n")
    if student_index == -1:
        view_student_details()
    if 1 <= student_index < len(Student.all_students):
        confirmation = input(
            "Are you sure you want to delete this student? (Y, N): ")
        print("\n-------------------------------\n")
        if confirmation.lower() == "y":
            deleted_student = Student.all_students.pop(student_index - 1)
            print(f"Successfully deleted {deleted_student.name}!",
                  end="\n\n-------------------------------\n\n")
        elif confirmation.lower() == "n":
            print("Student deletion cancelled.",
                  end="\n\n-------------------------------\n\n")
        else:
            print("Invalid input. Student deletion cancelled.",
                  end="\n\n-------------------------------\n\n")
    else:
        print("Invalid student index. Please try again.",
              end="\n\n-------------------------------\n\n")


# -------------------------------------------------------------------------------------------------------------------- #
#
# RANDOM STUDENT DETAILS GENERATION
#
# -------------------------------------------------------------------------------------------------------------------- #


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


# -------------------------------------------------------------------------------------------------------------------- #
#
# ERROR CHECKING FUNCTIONS
#
# -------------------------------------------------------------------------------------------------------------------- #


def has_number(string):
    for char in string:
        if char.isdigit():
            return True
    return False


def get_valid_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "" or has_number(user_input):
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
        if user_input != "N/A" and (len(user_input) < 8 or user_input.strip() == "" or not user_input.isdigit()):
            print("Invalid input. Please enter a valid phone number.")
            continue
        return user_input


# -------------------------------------------------------------------------------------------------------------------- #
#
# -------------------------------------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    s1 = Student("Leona", "Palmer", 20, "Female", "Victoria Junior College", "Badminton", {
        "English": 90, "Mother Tongue": 82, "Maths": 88, "Pure Physics": 89, "Pure Chemistry": 95, "Geography/Social Studies": 87, "Additional Mathematics": 76, "Computing": 88}, "86972149")
    s2 = Student("Bobby", "Gardner", 21, "Male", "Millenia Institute", "Infocomm", {
        "English": 67, "Mother Tongue": 73, "Maths": 75, "Biology/Chemistry": 87, "History/Social Studies": 66, "Design and Technology": 76, "Principles of Accounting": 78}, "N/A")
    s3 = Student("Jack", "Goodwin", 22, "Male", "Jurong Pioneers College", "Hockey", {
        "English": 68, "Mother Tongue": 45, "Maths": 87, "Physics/Chemistry": 89, "Literature/Social Studies": 67, "Nutrition and Food Science": 76, "Principles of Accounting": 67}, "91081566")
    s4 = Student("Carla", "Hicks", 23, "Female", "Catholic Junior College", "Volleyball", {
        "English": 65, "Mother Tongue": 88, "Maths": 77, "Physics/Biology": 88, "Pure History": 76, "Art": 69, "Design and Technology": 67}, "99718770")
    main()
