import random


def generate_random_marks():
    subjects = ["English", "Mother Tongue", "Maths"]
    subjects.extend(generate_science_subjects())
    subjects.extend(generate_humanities_subjects())
    subjects.extend(generate_coursework_non_coursework_subjects())

    return {subject: random.randint(60, 100) for subject in subjects}


def generate_science_subjects():
    COMBINED_SCIENCES = ["Physics/Chemistry",
                         "Physics/Biology", "Biology/Chemistry"]
    PURE_SCIENCES = ["Pure Physics", "Pure Chemistry", "Pure Biology"]

    science_type = random.choice(["combined", "pure"])
    if science_type == "combined":
        return [random.choice(COMBINED_SCIENCES)]
    else:
        return random.sample(PURE_SCIENCES, 2)


def generate_humanities_subjects():
    HUMANITIES = ["Geography/Social Studies", "History/Social Studies",
                  "Literature/Social Studies", "Pure History", "Pure Literature"]
    return [random.choice(HUMANITIES)]


def generate_coursework_non_coursework_subjects():
    COURSEWORK_NON_COURSEWORK = ["Design and Technology", "Additional Mathematics",
                                 "Principles of Accounting", "Art", "Nutrition and Food Science", "Computing"]
    num_courses = random.choice([1, 2])
    return random.sample(COURSEWORK_NON_COURSEWORK, num_courses)


def generate_random_phone_number():
    return f"{random.randint(6000, 9999)}{random.randint(1000, 9999)}"
