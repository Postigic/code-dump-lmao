import { createHash } from "crypto";

class Student {
    static allStudents = [];

    constructor(
        firstName,
        lastName,
        age,
        gender,
        school,
        cca,
        marks,
        phoneNumber
    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.name = `${firstName} ${lastName}`;
        this.age = age;
        this.gender = gender;
        this.school = school;
        this.cca = cca;
        this.marks = marks;
        this.overallMarks = this.calculateOverallMarks();
        this.phoneNumber = phoneNumber;
        Student.allStudents.push(this);
    }

    printDetails() {
        console.log(`Student ID: ${this.generateStudentID()}`);
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
        console.log(`Gender: ${this.gender}`);
        console.log(`School: ${this.school}`);
        console.log(`Co-Curricular Activities: ${this.cca}`);
        console.log(`Marks: ${this.marksStr()}`);
        console.log(
            `Performance (Best to Worst): ${this.displaySubjectDescending()}`
        );
        console.log(`Overall Marks: ${this.overallMarks}`);
        console.log(`Overall Grade: ${this.calculateOverallGrade()}`);
        console.log(`Ranking: ${this.calculateRanking()}`);
        console.log(`Email: ${this.email()}`);
        console.log(`Phone Number: ${this.phoneNumber}`);
        console.log("\n-------------------------------\n");
    }

    updateStudentDetails() {
        this.overallMarks = this.calculateOverallMarks();
        this.grade = this.calculateOverallGrade();
        this.ranking = this.calculateRanking();
    }

    generateStudentID() {
        const string = (this.name + this.school).toLowerCase();
        return createHash("sha256").update(string).digest("hex").slice(0, 8);
    }

    email() {
        return `${this.name.toLowerCase().replace(" ", "_")}@gmail.com`;
    }

    marksStr() {
        return Object.entries(this.marks)
            .map(([subject, mark]) => `${subject}: ${mark}`)
            .join(", ");
    }

    displaySubjectDescending() {
        return Object.keys(this.marks)
            .sort((a, b) => this.marks[b] - this.marks[a])
            .join(", ");
    }

    calculateOverallMarks() {
        const totalMarks = Object.values(this.marks).reduce((a, b) => a + b, 0);
        return Math.round(totalMarks / Object.keys(this.marks).length);
    }

    calculateOverallGrade() {
        const gradeBoundaries = [0, 40, 45, 50, 60, 70];
        const gradeMapping = "FEDCBA";
        const gradeIndex = gradeBoundaries.findIndex(
            (boundary) => this.overallMarks < boundary
        );
        return gradeMapping[
            gradeIndex === -1 ? gradeMapping.length - 1 : gradeIndex - 1
        ];
    }

    calculateRanking() {
        const sortedStudents = Student.allStudents.sort(
            (a, b) => b.overallMarks - a.overallMarks
        );
        return sortedStudents.indexOf(this) + 1;
    }

    toDict() {
        return {
            name: this.name,
            age: this.age,
            gender: this.gender,
            school: this.school,
            cca: this.cca,
            marks: this.marks,
            phoneNumber: this.phoneNumber,
        };
    }

    static fromDict(data) {
        const [firstName, lastName] = data.name.split(" ");
        return new Student(
            firstName,
            lastName,
            data.age,
            data.gender,
            data.school,
            data.cca,
            data.marks,
            data.phoneNumber
        );
    }
}

export default Student;
