import json
from student_class import Student


def save_students(filename):
    with open(filename, "w") as file:
        json.dump([student.to_dict()
                  for student in Student.all_students], file, indent=4)


def load_students(filename):
    with open(filename, "r") as file:
        student_data_list = json.load(file)

    with open(filename, "w") as file:
        file.write("[]")

    return [Student.from_dict(student_data) for student_data in student_data_list]
