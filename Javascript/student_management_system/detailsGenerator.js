import {
    COMBINED_SCIENCES,
    PURE_SCIENCES,
    HUMANITIES,
    COURSEWORK_NON_COURSEWORK,
} from "./utils.js";

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

export function generateRandomMarks() {
    const subjects = ["English", "Mother Tongue", "Maths"];
    subjects.push(...generateScienceSubjects());
    subjects.push(...generateHumanitiesSubjects());
    subjects.push(...generateCourseworkNonCourseworkSubjects());

    const marks = {};
    subjects.forEach((subject) => {
        marks[subject] = getRandomInt(60, 100);
    });

    return marks;
}

function generateScienceSubjects() {
    const scienceType = Math.random() < 0.5 ? "combined" : "pure";
    if (scienceType === "combined") {
        return [
            COMBINED_SCIENCES[
                Math.floor(Math.random() * COMBINED_SCIENCES.length)
            ],
        ];
    } else {
        const selected = [];
        while (selected.length < 2) {
            const subject =
                PURE_SCIENCES[Math.floor(Math.random() * PURE_SCIENCES.length)];
            if (!selected.includes(subject)) {
                selected.push(subject);
            }
        }
        return selected;
    }
}

function generateHumanitiesSubjects() {
    return [HUMANITIES[Math.floor(Math.random() * HUMANITIES.length)]];
}

function generateCourseworkNonCourseworkSubjects() {
    const numCourses = Math.random() < 0.5 ? 1 : 2;
    const shuffled = COURSEWORK_NON_COURSEWORK.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, numCourses);
}

export function generateRandomPhoneNumber() {
    return `${getRandomInt(6000, 9999)}${getRandomInt(1000, 9999)}`;
}
