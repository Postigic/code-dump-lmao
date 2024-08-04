import { writeFileSync, readFileSync } from "fs";
import Student from "./studentClass.js";

export function saveStudents(filename) {
    const uniqueStudentIds = new Set();
    const uniqueStudents = [];

    Student.allStudents.forEach((student) => {
        const studentId = student.generateStudentID();
        if (!uniqueStudentIds.has(studentId)) {
            uniqueStudentIds.add(studentId);
            uniqueStudents.push(student);
        }
    });

    const studentData = uniqueStudents.map((student) => student.toDict());
    writeFileSync(filename, JSON.stringify(studentData, null, 4), "utf8");
}

export function loadStudents(filename) {
    const studentDataList = JSON.parse(readFileSync(filename, "utf8"));

    return studentDataList.map((studentData) => Student.fromDict(studentData));
}
