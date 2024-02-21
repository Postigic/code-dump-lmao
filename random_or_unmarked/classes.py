class Student:
    def __init__(self, first_name, last_name, age, gender, school, cca, marks, phone_number):
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.school = school
        self.cca = cca
        self.marks = marks
        self.phone_number = phone_number

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"School: {self.school}")
        print(f"Co-Curricular Activities: {self.cca}")
        print(
            f"Marks: {', '.join([f'{subject}: {mark}' for subject, mark in self.marks.items()])}")
        print(f"Overall Marks: {self.overall_marks()}")
        print(f"Overall Grade: {self.overall_grade()}")
        print(f"Email: {self.email()}")
        print(f"Phone Number: {self.phone_number}")
        print("\n-------------------------------\n\n")

    def generate_student_ID():
        pass

    def email(self):
        return f"{self.name.lower().replace(' ', '_')}@gmail.com"

    def overall_marks(self):
        return f"{round(sum(self.marks.values()) / len(self.marks))}"

    def overall_grade(self):
        average_marks = int(self.overall_marks())
        if average_marks >= 70:
            return "A"
        elif average_marks >= 60:
            return "B"
        elif average_marks >= 50:
            return "C"
        elif average_marks >= 45:
            return "D"
        elif average_marks >= 40:
            return "E"
        else:
            return "F"

    def calculate_ranking():
        pass

    def analyse_performance():
        pass


s1 = Student("Leona", "Palmer", 20, "Female", "Victoria Junior College", "Badminton", {
             "English": 90, "Maths": 81, "Science": 95, "History": 80, "Social Studies": 87, "Mother Tongue": 92}, "86972149")
s1.print_details()
s2 = Student("Bobby", "Gardner", 21, "Male", "Millenia Institute", "Infocomm", {
             "English": 67, "Maths": 75, "Science": 87, "History": 76, "Social Studies": 64, "Mother Tongue": 73}, "N/A")
s2.print_details()
s3 = Student("Jack", "Goodwin", 22, "Male", "Jurong Pioneers College", "Robotics", {
             "English": 68, "Maths": 87, "Science": 89, "History": 67, "Social Studies": 90, "Mother Tongue": 55}, "91081566")
s3.print_details()
s4 = Student("Carla", "Hicks", 23, "Female", "Catholic College", "Volleyball", {
             "English": 65, "Maths": 77, "Science": 78, "History": 89, "Social Studies": 67, "Mother Tongue": 88}, "99718770")
s4.print_details()


"""
TODO: 

Ranking: Implement a method to rank students based on their marks. You can sort the students by marks and assign ranks accordingly.

Student ID: Generate and assign a unique student ID to each student upon initialization. This can be helpful for identification purposes.

Performance Analytics: Add methods to analyze the overall performance of the student, such as average marks, highest/lowest marks, etc.
"""
