import {
    getValidString,
    getValidIndex,
    getValidAge,
    getValidGender,
    getValidNumOfSubjects,
    getValidUniqueSubject,
    getValidMark,
    getValidPhoneNumber,
    getValidStudentID,
} from "./inputValidation.js";

import {
    editName,
    editAge,
    editGender,
    editPhoneNumber,
    editMarks,
    editSchool,
    editCca,
} from "./editing.js";

export const FIRST_NAMES = [
    "Rowan",
    "Riley",
    "Avery",
    "Logan",
    "Quinn",
    "Jordan",
    "River",
    "Cameron",
    "Angel",
    "Carter",
    "Ryan",
    "Dylan",
    "Noah",
    "Ezra",
    "Emery",
    "Hunter",
    "Kai",
    "August",
    "Nova",
    "Parker",
    "Arbor",
    "Ash",
    "Charlie",
    "Drew",
    "Ellis",
    "Everest",
    "Jett",
    "Lowen",
    "Moss",
    "Oakley",
    "Onyx",
    "Phoenix",
    "Ridley",
    "Remy",
    "Robin",
    "Royal",
    "Sage",
    "Scout",
    "Tatum",
    "Wren",
    "Monroe",
];

export const LAST_NAMES = [
    "Vaughn",
    "Rios",
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Sanders",
    "Kelly",
    "Boone",
    "Francis",
    "Martin",
    "Tyler",
    "Potter",
    "Hicks",
    "Goodwin",
    "Gardner",
    "Palmer",
];

export const SCHOOLS = [
    "Victoria Junior College",
    "Millenia Institute",
    "Jurong Pioneers College",
    "Catholic Junior College",
    "Temasek Junior College",
    "River Valley High School",
    "Hwa Chong Institution",
    "Raffles Institution",
    "Dunman High School",
];

export const CO_CURRICULAR_ACTIVITIES = [
    "Volleyball",
    "Media",
    "Infocomm",
    "Track and Field",
    "Badminton",
    "Table Tennis",
    "Hockey",
    "Floorball",
    "Basketball",
    "Soccer",
    "Choir",
    "Band",
    "Chinese Dance",
    "Malay Dance",
    "Modern Dance",
    "Police National Cadet Corps",
    "Chinese Drama",
    "Chinese Orchestra",
    "Singapore Youth Flying Club",
];

export const COMBINED_SCIENCES = [
    "Physics/Chemistry",
    "Physics/Biology",
    "Biology/Chemistry",
];

export const PURE_SCIENCES = ["Pure Physics", "Pure Chemistry", "Pure Biology"];

export const HUMANITIES = [
    "Geography/Social Studies",
    "History/Social Studies",
    "Literature/Social Studies",
    "Pure History",
    "Pure Literature",
];

export const COURSEWORK_NON_COURSEWORK = [
    "Design and Technology",
    "Additional Mathematics",
    "Principles of Accounting",
    "Art",
    "Nutrition and Food Science",
    "Computing",
];

export const validationFunctions = {
    string: getValidString,
    index: getValidIndex,
    age: getValidAge,
    gender: getValidGender,
    numOfSubjects: getValidNumOfSubjects,
    uniqueSubject: getValidUniqueSubject,
    mark: getValidMark,
    phoneNumber: getValidPhoneNumber,
    studentID: getValidStudentID,
};

export const editingFunctions = {
    name: editName,
    age: editAge,
    gender: editGender,
    phoneNumber: editPhoneNumber,
    marks: editMarks,
    school: editSchool,
    cca: editCca,
};

export const filename = String.raw`D:\vs code projects\JavaScript\student_management_system\students.json`;
