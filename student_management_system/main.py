import random
import sys
from student_class import Student
from input_validation import get_valid_string, get_valid_index, get_valid_age, get_valid_gender, get_valid_num_of_subjects, get_valid_unique_subject, get_valid_mark, get_valid_phone_number, get_valid_student_ID
from random_generation import generate_random_marks, generate_random_phone_number

FIRST_NAMES = ["Rowan", "Riley", "Avery", "Logan", "Quinn", "Jordan", "River", "Cameron", "Angel", "Carter", "Ryan", "Dylan", "Noah", "Ezra", "Emery", "Hunter", "Kai", "August", "Nova",
               "Parker", "Arbor", "Ash", "Charlie", "Drew", "Ellis", "Everest", "Jett", "Lowen", "Moss", "Oakley", "Onyx", "Phoenix", "Ridley", "Remy", "Robin", "Royal", "Sage", "Scout", "Tatum", "Wren", "Monroe"]
LAST_NAMES = ["Vaughn", "Rios", "Smith", "Johnson", "Williams", "Jones", "Brown",
              "Davis", "Miller", "Sanders", "Kelly", "Boone", "Francis", "Martin", "Tyler", "Potter", "Hicks", "Goodwin", "Gardner", "Palmer"]
SCHOOLS = ["Victoria Junior College", "Millenia Institute", "Jurong Pioneers College", "Catholic Junior College",
           "Temasek Junior College", "River Valley High School", "Hwa Chong Institution", "Raffles Institution", "Dunman High School"]
CO_CURRICULAR_ACTIVITIES = ["Volleyball", "Media", "Infocomm", "Track and Field", "Badminton", "Table Tennis", "Hockey", "Floorball", "Basketball", "Soccer", "Choir", "Band", "Chinese Dance",
                            "Malay Dance", "Modern Dance", "Police National Cadet Corps", "Chinese Drama", "Chinese Orchestra", "Singapore Youth Flying Club"]

validation_functions = {
    "string": get_valid_string,
    "index": get_valid_index,
    "age": get_valid_age,
    "gender": get_valid_gender,
    "num_of_subjects": get_valid_num_of_subjects,
    "unique_subject": get_valid_unique_subject,
    "mark": get_valid_mark,
    "phone_number": get_valid_phone_number,
    "student_ID": get_valid_student_ID,
}


def main():
    options = {
        "1": add_student,
        "2": view_student_details
    }

    while True:
        print("Welcome to the Student Management System!",
              end="\n\n-------------------------------\n\n")
        print("1. Add a new student")
        print("2. View student details")
        print("3. Exit")

        choice = input("\nEnter your choice: ")
        print("\n-------------------------------\n")

        if choice == "3":
            print("Thanks for using the Student Management System!")
            print("Exiting...")
            sys.exit()
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")


def add_student():
    options = {
        "1": get_student_details,
        "2": generate_random_student,
        "3": main
    }

    while True:
        print("1. Add a new student manually")
        print("2. Generate a random student")
        print("3. Go back")

        choice = input("\nEnter your choice: ")
        print("\n-------------------------------\n")

        if choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def view_student_details():
    options = {
        "1": print_student_details,
        "2": edit_student_details,
        "3": delete_student_details,
        "4": main
    }

    while True:
        print("1. View a student's details")
        print("2. Edit a student's details")
        print("3. Delete a student's details")
        print("4. Go back")

        choice = input("\nEnter your choice: ")
        print("\n-------------------------------\n")

        if choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def get_student_details():
    details = {}
    details["first_name"] = validation_functions["string"](
        "Enter first name: ")
    details["last_name"] = validation_functions["string"]("Enter last name: ")
    details["age"] = validation_functions["age"]("Enter age: ")
    details["gender"] = validation_functions["gender"](
        "Enter gender (M or F): ")
    details["school"] = validation_functions["string"]("Enter school: ")
    details["cca"] = validation_functions["string"](
        "Enter co-curricular activity: ")
    details["marks"] = {}
    num_subjects = validation_functions["num_of_subjects"](
        "Enter the number of subjects (7 or 8): ")
    for _ in range(num_subjects):
        subject = validation_functions["string"]("Enter subject name: ")
        subject = validation_functions["unique_subject"](
            details["marks"], subject)
        mark = validation_functions["mark"](f"Enter {subject} mark: ")
        details["marks"][subject] = mark
    details["phone_number"] = validation_functions["phone_number"](
        "Enter phone number (XXXXXXXX): ")
    print("\n-------------------------------\n")

    new_student = Student(details["first_name"], details["last_name"], details["age"],
                          details["gender"], details["school"], details["cca"], details["marks"], details["phone_number"])
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
        student_dict = {student.generate_student_ID(
        ): student for student in Student.all_students}

        for i, (student_id, student) in enumerate(student_dict.items(), start=1):
            print(f"{i}. ID: {student_id} — {student.name}")

        student_id = validation_functions["student_ID"](
            "\nEnter student ID (-1 to go back): ")
        print("\n-------------------------------\n")

        if student_id == -1:
            view_student_details()
        elif student_id in student_dict:
            student = student_dict[student_id]
            student.print_details()
        else:
            print("Invalid student ID. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def edit_student_details():
    while True:
        student_dict = {student.generate_student_ID(
        ): student for student in Student.all_students}

        for i, (student_id, student) in enumerate(student_dict.items(), start=1):
            print(f"{i}. ID: {student_id} — {student.name}")

        student_id = validation_functions["student_ID"](
            "\nEnter student ID (-1 to go back): ")
        print("\n-------------------------------\n")

        if student_id == -1:
            view_student_details()
        elif student_id in student_dict:
            student = student_dict[student_id]
            edit_student(student)
            break
        else:
            print("Invalid student ID. Please try again.",
                  end="\n\n-------------------------------\n\n")
            continue


def edit_student(student):
    print("Current Details:", end="\n\n")
    student.print_details()

    options = {
        "1": edit_name,
        "2": edit_age,
        "3": edit_gender,
        "4": edit_school,
        "5": edit_cca,
        "6": edit_marks,
        "7": edit_phone_number
    }

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

        if choice == "8":
            print("Exiting editing mode.",
                  end="\n\n-------------------------------\n\n")
            break
        elif choice in options:
            options[choice](student)
        else:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")


def edit_name(student):
    new_name = validation_functions["string"]("Enter new name: ")
    student.name = new_name
    print("\n-------------------------------\n")
    print("Name updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_age(student):
    new_age = validation_functions["age"]("Enter new age: ")
    student.age = new_age
    print("\n-------------------------------\n")
    print("Age updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_gender(student):
    new_gender = validation_functions["gender"]("Enter new gender (M or F): ")
    student.gender = new_gender
    print("\n-------------------------------\n")
    print("Gender updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_school(student):
    new_school = validation_functions["string"]("Enter new school: ")
    student.school = new_school
    print("\n-------------------------------\n")
    print("School updated successfully!",
          end="\n\n-------------------------------\n\n")


def edit_cca(student):
    new_cca = validation_functions["string"](
        "Enter new co-curricular activity: ")
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
        new_subject = validation_functions["string"](
            "Enter the new subject name: ")
        new_subject = validation_functions["unique_subject"](
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
        new_mark = validation_functions["mark"](
            f"Enter new mark for {subject_to_edit}: ")
        student.marks[subject_to_edit] = new_mark
        student.update_student_details()
        print("\n-------------------------------\n")
        print(f"Mark for {subject_to_edit} updated successfully!")
    else:
        print("\n-------------------------------\n")
        print(f"Subject '{subject_to_edit}' not found in marks.")


def edit_phone_number(student):
    new_phone_number = validation_functions["phone_number"](
        "Enter new phone number (XXXXXXXX): ")
    student.phone_number = new_phone_number
    print("\n-------------------------------\n")
    print("Phone number updated successfully!",
          end="\n\n-------------------------------\n\n")


def delete_student_details():
    student_dict = {student.generate_student_ID(
    ): student for student in Student.all_students}

    for i, (student_id, student) in enumerate(student_dict.items(), start=1):
        print(f"{i}. ID: {student_id} — {student.name}")

    student_id = validation_functions["student_ID"](
        "\nEnter student ID (-1 to go back): ")
    print("\n-------------------------------\n")

    if student_id == -1:
        view_student_details()
    elif student_id in student_dict:
        confirmation = input(
            "Are you sure you want to delete this student? (Y, N): ")
        print("\n-------------------------------\n")

        if confirmation.lower() == "y":
            for student in Student.all_students:
                if student.generate_student_ID() == student_id:
                    deleted_student = student
                    Student.all_students.remove(student)
                    break
            print(f"Successfully deleted {deleted_student.name}!",
                  end="\n\n-------------------------------\n\n")
        elif confirmation.lower() == "n":
            print("Student deletion cancelled.",
                  end="\n\n-------------------------------\n\n")
        else:
            print("Invalid input. Student deletion cancelled.",
                  end="\n\n-------------------------------\n\n")
    else:
        print("Invalid student ID. Please try again.",
              end="\n\n-------------------------------\n\n")


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
