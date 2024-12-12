from input_validation import *

FIRST_NAMES = ["Rowan", "Riley", "Avery", "Logan", "Quinn", "Jordan", "River", "Cameron", "Angel", "Carter", "Ryan", "Dylan", "Noah", "Ezra", "Emery", "Hunter", "Kai", "August", "Nova", "Parker",
               "Arbor", "Ash", "Charlie", "Drew", "Ellis", "Everest", "Jett", "Lowen", "Moss", "Oakley", "Onyx", "Phoenix", "Ridley", "Remy", "Robin", "Royal", "Sage", "Scout", "Tatum", "Wren", "Monroe"]

LAST_NAMES = ["Vaughn", "Rios", "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
              "Sanders", "Kelly", "Boone", "Francis", "Martin", "Tyler", "Potter", "Hicks", "Goodwin", "Gardner", "Palmer"]

SCHOOLS = ["Victoria Junior College", "Millenia Institute", "Jurong Pioneers College", "Catholic Junior College",
           "Temasek Junior College", "River Valley High School", "Hwa Chong Institution", "Raffles Institution", "Dunman High School"]

CO_CURRICULAR_ACTIVITIES = ["Volleyball", "Media", "Infocomm", "Track and Field", "Badminton", "Table Tennis", "Hockey", "Floorball", "Basketball", "Soccer",
                            "Choir", "Band", "Chinese Dance", "Malay Dance", "Modern Dance", "Police National Cadet Corps", "Chinese Drama", "Chinese Orchestra", "Singapore Youth Flying Club"]

COMBINED_SCIENCES = ["Physics/Chemistry",
                     "Physics/Biology", "Biology/Chemistry"]

PURE_SCIENCES = ["Pure Physics", "Pure Chemistry", "Pure Biology"]

HUMANITIES = ["Geography/Social Studies", "History/Social Studies",
              "Literature/Social Studies", "Pure History", "Pure Literature"]

COURSEWORK_NON_COURSEWORK = ["Design and Technology", "Additional Mathematics",
                             "Principles of Accounting", "Art", "Nutrition and Food Science", "Computing"]

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

current_dir = Path(__file__).parent
filename = current_dir / "students.json"
