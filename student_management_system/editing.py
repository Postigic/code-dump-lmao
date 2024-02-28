from utils import validation_functions


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
