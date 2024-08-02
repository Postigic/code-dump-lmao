import json
from student_class import Student


def save_students(filename):
    unique_student_ids = set()
    unique_students = []

    for student in Student.all_students:
        student_id = student.generate_student_ID()
        if student_id not in unique_student_ids:
            unique_student_ids.add(student_id)
            unique_students.append(student)

    with open(filename, "w") as file:
        json.dump([student.to_dict()
                  for student in unique_students], file, indent=4)


def load_students(filename):
    with open(filename, "r") as file:
        student_data_list = json.load(file)

    return [Student.from_dict(student_data) for student_data in student_data_list]
