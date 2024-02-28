import hashlib
import bisect


class Student:
    all_students = []

    def __init__(self, first_name, last_name, age, gender, school, cca, marks, phone_number):
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.school = school
        self.cca = cca
        self.marks = marks
        self.overall_marks = self.calculate_overall_marks()
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
        self.overall_marks = self.calculate_overall_marks()
        self.grade = self.calculate_overall_grade()
        self.ranking = self.calculate_ranking()

    def generate_student_ID(self):
        string = (self.name + self.school).lower()
        student_id = hashlib.sha256(string.encode()).hexdigest()[:8]
        return student_id

    def email(self):
        return f"{self.name.lower().replace(' ', '_')}@gmail.com"

    def marks_str(self):
        return ', '.join([f"{subject}: {mark}" for subject, mark in self.marks.items()])

    def display_subject_descending(self):
        sorted_subjects = sorted(
            self.marks.keys(), key=lambda x: self.marks[x], reverse=True)
        return ', '.join(sorted_subjects)

    def calculate_overall_marks(self):
        return round(sum(self.marks.values()) / len(self.marks))

    def calculate_overall_grade(self):
        grade_boundaries = [0, 40, 45, 50, 60, 70]
        grade_mapping = "FEDCBA"
        grade_index = bisect.bisect_right(grade_boundaries, self.overall_marks)
        return grade_mapping[grade_index - 1]

    def calculate_ranking(self):
        sorted_students = sorted(
            Student.all_students, key=lambda x: x.overall_marks, reverse=True)
        return sorted_students.index(self) + 1
