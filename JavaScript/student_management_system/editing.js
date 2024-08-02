import { validationFunctions } from "./utils.js";

export async function editName(student) {
    const newName = await validationFunctions.string("Enter new name: ");
    student.name = newName;
    console.log("\n-------------------------------\n");
    console.log(
        "Name updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}

export async function editAge(student) {
    const newAge = await validationFunctions.age("Enter new age: ");
    student.age = newAge;
    console.log("\n-------------------------------\n");
    console.log(
        "Age updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}

export async function editGender(student) {
    const newGender = await validationFunctions.gender(
        "Enter new gender (M or F): "
    );
    student.gender = newGender;
    console.log("\n-------------------------------\n");
    console.log(
        "Gender updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}

export async function editSchool(student) {
    const newSchool = await validationFunctions.string("Enter new school: ");
    student.school = newSchool;
    console.log("\n-------------------------------\n");
    console.log(
        "School updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}

export async function editCca(student) {
    const newCca = await validationFunctions.string(
        "Enter new co-curricular activity: "
    );
    student.cca = newCca;
    console.log("\n-------------------------------\n");
    console.log(
        "Co-Curricular Activities updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}

export async function editMarks(student) {
    console.log(`Current Marks: ${student.marksStr()}\n`);
    console.log("1. Edit subject");
    console.log("2. Edit mark");
    const editChoice = await promptUser("\nEnter your choice: ");
    console.log("\n-------------------------------\n");

    if (editChoice === "1") {
        await editSubject(student);
    } else if (editChoice === "2") {
        await editMark(student);
    } else {
        console.log("Invalid choice. Please try again.");
    }
}

async function editSubject(student) {
    const subjectToEdit = await promptUser(
        "Enter the subject you want to edit: "
    );
    if (subjectToEdit in student.marks) {
        let newSubject = await validationFunctions.string(
            "Enter the new subject name: "
        );
        newSubject = await validationFunctions.uniqueSubject(
            student.marks,
            newSubject
        );
        student.marks[newSubject] = student.marks[subjectToEdit];
        delete student.marks[subjectToEdit];
        console.log("\n-------------------------------\n");
        console.log(
            "Subject updated successfully!",
            "\n\n-------------------------------\n\n"
        );
    } else {
        console.log("\n-------------------------------\n");
        console.log(
            `Subject '${subjectToEdit}' not found in marks.`,
            "\n\n-------------------------------\n\n"
        );
    }
}

async function editMark(student) {
    const subjectToEdit = await promptUser(
        "Enter the subject for which you want to edit the mark: "
    );
    if (subjectToEdit in student.marks) {
        const newMark = await validationFunctions.mark(
            `Enter new mark for ${subjectToEdit}: `
        );
        student.marks[subjectToEdit] = newMark;
        student.updateStudentDetails();
        console.log("\n-------------------------------\n");
        console.log(`Mark for ${subjectToEdit} updated successfully!`);
    } else {
        console.log("\n-------------------------------\n");
        console.log(`Subject '${subjectToEdit}' not found in marks.`);
    }
}

export async function editPhoneNumber(student) {
    const newPhoneNumber = await validationFunctions.phoneNumber(
        "Enter new phone number (XXXXXXXX): "
    );
    student.phoneNumber = newPhoneNumber;
    console.log("\n-------------------------------\n");
    console.log(
        "Phone number updated successfully!",
        "\n\n-------------------------------\n\n"
    );
}
