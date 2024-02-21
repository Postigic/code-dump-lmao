class Student:
    def __init__(self, first_name, last_name, age, gender, school, marks):
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.gender = gender
        self.school = school
        self.marks = marks

    def email(self):
        return f"{self.name.lower().replace(' ', '_')}@gmail.com"

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"School: {self.school}")
        print(f"Marks: {self.marks}")
        print(f"Email: {self.email()}\n")


s1 = Student("Leona", "Palmer", 20, "Male", "Victoria Junior College", 90)
s1.print_details()
s2 = Student("Bobby", "Gardner", 21, "Female", "Millenia Institute", 85)
s2.print_details()
s3 = Student("Jack", "Goodwin", 22, "Male", "Jurong Pioneers College", 95)
s3.print_details()


class Phone:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}\n")


p1 = Phone("iPhone 13", 1000, "Apple")
p1.print_details()
p2 = Phone("Pixel 6", 800, "Google")
p2.print_details()
p3 = Phone("OnePlus 9", 1200, "OnePlus")
p3.print_details()
