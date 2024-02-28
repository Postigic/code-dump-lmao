import random


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
