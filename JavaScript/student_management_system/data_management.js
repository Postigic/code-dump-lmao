import { writeFileSync, readFileSync } from "fs";
import Student from "./student_class.js";

export function saveStudents(filename) {
    const studentData = Student.allStudents.map((student) => student.toDict());
    writeFileSync(filename, JSON.stringify(studentData, null, 4), "utf8");
}

export function loadStudents(filename) {
    const studentDataList = JSON.parse(readFileSync(filename, "utf8"));

    writeFileSync(filename, "[]", "utf8");

    return studentDataList.map((studentData) => Student.fromDict(studentData));
}
