import Student from "./student_class.js";
import {
    generateRandomMarks,
    generateRandomPhoneNumber,
} from "./details_generator.js";
import {
    FIRST_NAMES,
    LAST_NAMES,
    SCHOOLS,
    CO_CURRICULAR_ACTIVITIES,
    validationFunctions,
    editingFunctions,
    filename,
} from "./utils.js";
import { loadStudents, saveStudents } from "./data_management.js";
import { promptUser } from "./input_validation.js";

async function main() {
    const options = {
        1: addStudent,
        2: viewStudentDetails,
    };

    loadStudents(filename);

    while (true) {
        console.log(
            "Welcome to the Student Management System!\n\n-------------------------------\n\n"
        );
        console.log("1. Add a new student");
        console.log("2. View student details");
        console.log("3. Exit");

        const choice = await promptUser("\nEnter your choice: ");
        console.log("\n-------------------------------\n");

        if (choice === "3") {
            saveStudents(filename);
            console.log("Thanks for using the Student Management System!");
            console.log("Exiting...");
            process.exit();
        } else if (options[choice]) {
            await options[choice]();
        } else {
            console.log(
                "Invalid choice. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function addStudent() {
    const options = {
        1: getStudentDetails,
        2: generateRandomStudent,
        3: main,
    };

    while (true) {
        console.log("1. Add a new student manually");
        console.log("2. Generate a random student");
        console.log("3. Go back");

        const choice = await promptUser("\nEnter your choice: ");
        console.log("\n-------------------------------\n");

        if (options[choice]) {
            await options[choice]();
        } else {
            console.log(
                "Invalid choice. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function viewStudentDetails() {
    const options = {
        1: printStudentDetails,
        2: editStudentDetails,
        3: deleteStudentDetails,
        4: main,
    };

    while (true) {
        console.log("1. View a student's details");
        console.log("2. Edit a student's details");
        console.log("3. Delete a student's details");
        console.log("4. Go back");

        const choice = await promptUser("\nEnter your choice: ");
        console.log("\n-------------------------------\n");

        if (options[choice]) {
            await options[choice]();
        } else {
            console.log(
                "Invalid choice. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function getStudentDetails() {
    const details = {};
    details.firstName = await validationFunctions.string("Enter first name: ");
    details.lastName = await validationFunctions.string("Enter last name: ");
    details.age = await validationFunctions.age("Enter age: ");
    details.gender = await validationFunctions.gender(
        "Enter gender (M or F): "
    );
    details.school = await validationFunctions.string("Enter school: ");
    details.cca = await validationFunctions.string(
        "Enter co-curricular activity: "
    );
    details.marks = {};
    const numSubjects = await validationFunctions.numOfSubjects(
        "Enter the number of subjects (7 or 8): "
    );
    for (let i = 0; i < numSubjects; i++) {
        let subject = await validationFunctions.string("Enter subject name: ");
        subject = await validationFunctions.uniqueSubject(
            details.marks,
            subject
        );
        const mark = await validationFunctions.mark(`Enter ${subject} mark: `);
        details.marks[subject] = mark;
    }
    details.phoneNumber = await validationFunctions.phoneNumber(
        "Enter phone number (XXXXXXXX): "
    );
    console.log("\n-------------------------------\n");

    new Student(
        details.firstName,
        details.lastName,
        details.age,
        details.gender,
        details.school,
        details.cca,
        details.marks,
        details.phoneNumber
    );
    console.log(
        "Student added successfully!\n\n-------------------------------\n\n"
    );
}

async function generateRandomStudent() {
    const firstName =
        FIRST_NAMES[Math.floor(Math.random() * FIRST_NAMES.length)];
    const lastName = LAST_NAMES[Math.floor(Math.random() * LAST_NAMES.length)];
    const age = Math.floor(Math.random() * (25 - 17 + 1)) + 17;
    const gender = ["M", "F"][Math.floor(Math.random() * 2)];
    const school = SCHOOLS[Math.floor(Math.random() * SCHOOLS.length)];
    const cca =
        CO_CURRICULAR_ACTIVITIES[
            Math.floor(Math.random() * CO_CURRICULAR_ACTIVITIES.length)
        ];
    const marks = generateRandomMarks();
    const phoneNumber = generateRandomPhoneNumber();

    new Student(
        firstName,
        lastName,
        age,
        gender,
        school,
        cca,
        marks,
        phoneNumber
    );
    console.log(
        "Student added successfully!\n\n-------------------------------\n\n"
    );
}

async function printStudentDetails() {
    while (true) {
        const studentDict = {};
        Student.allStudents.forEach((student) => {
            studentDict[student.generateStudentID()] = student;
        });

        Object.entries(studentDict).forEach(([studentId, student], index) => {
            console.log(`${index + 1}. ID: ${studentId} — ${student.name}`);
        });

        const studentId = await validationFunctions.studentID(
            "\nEnter student ID (-1 to go back): ",
            Student.allStudents
        );
        console.log("\n-------------------------------\n");

        if (studentId === "-1") {
            await viewStudentDetails();
            break;
        } else if (studentDict[studentId]) {
            const student = studentDict[studentId];
            student.printDetails();
        } else {
            console.log(
                "Invalid student ID. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function editStudentDetails() {
    while (true) {
        const studentDict = {};
        Student.allStudents.forEach((student) => {
            studentDict[student.generateStudentID()] = student;
        });

        Object.entries(studentDict).forEach(([studentId, student], index) => {
            console.log(`${index + 1}. ID: ${studentId} — ${student.name}`);
        });

        const studentId = await validationFunctions.studentID(
            "\nEnter student ID (-1 to go back): ",
            Student.allStudents
        );
        console.log("\n-------------------------------\n");

        if (studentId === "-1") {
            await viewStudentDetails();
            break;
        } else if (studentDict[studentId]) {
            const student = studentDict[studentId];
            await editStudent(student);
            break;
        } else {
            console.log(
                "Invalid student ID. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function editStudent(student) {
    console.log("Current Details:\n\n");
    student.printDetails();

    const options = {
        1: editingFunctions.name,
        2: editingFunctions.age,
        3: editingFunctions.gender,
        4: editingFunctions.school,
        5: editingFunctions.cca,
        6: editingFunctions.marks,
        7: editingFunctions.phoneNumber,
    };

    while (true) {
        console.log("What would you like to edit?\n\n");
        console.log("1. Name");
        console.log("2. Age");
        console.log("3. Gender");
        console.log("4. School");
        console.log("5. Co-Curricular Activities");
        console.log("6. Marks");
        console.log("7. Phone Number");
        console.log("8. Exit");

        const choice = await promptUser("\nEnter your choice: ");
        console.log("\n-------------------------------\n");

        if (choice === "8") {
            console.log(
                "Exiting editing mode.\n\n-------------------------------\n\n"
            );
            break;
        } else if (options[choice]) {
            await options[choice](student);
        } else {
            console.log(
                "Invalid choice. Please try again.\n\n-------------------------------\n\n"
            );
        }
    }
}

async function deleteStudentDetails() {
    const studentDict = {};
    Student.allStudents.forEach((student) => {
        studentDict[student.generateStudentID()] = student;
    });

    Object.entries(studentDict).forEach(([studentId, student], index) => {
        console.log(`${index + 1}. ID: ${studentId} — ${student.name}`);
    });

    const studentId = await validationFunctions.studentID(
        "\nEnter student ID (-1 to go back): ",
        Student.allStudents
    );
    console.log("\n-------------------------------\n");

    if (studentId === "-1") {
        await viewStudentDetails();
    } else if (studentDict[studentId]) {
        const confirmation = await promptUser(
            "Are you sure you want to delete this student? (Y, N): "
        );
        console.log("\n-------------------------------\n");

        if (confirmation.toLowerCase() === "y") {
            Student.allStudents = Student.allStudents.filter(
                (student) => student.generateStudentID() !== studentId
            );
            console.log(
                `Successfully deleted ${studentDict[studentId].name}!\n\n-------------------------------\n\n`
            );
        } else {
            console.log(
                "Student deletion cancelled.\n\n-------------------------------\n\n"
            );
        }
    } else {
        console.log(
            "Invalid student ID. Please try again.\n\n-------------------------------\n\n"
        );
    }
}

main();
