import { createInterface } from "readline";
const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
});

export async function promptUser(question) {
    return new Promise((resolve) => {
        rl.question(question, (answer) => {
            resolve(answer);
        });
    });
}

export async function getValidString(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        if (userInput.trim() === "" || !/^[a-zA-Z]+$/.test(userInput)) {
            console.log("Invalid input.");
            continue;
        }
        return userInput;
    }
}

export async function getValidIndex(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        const number = parseInt(userInput, 10);
        if (isNaN(number)) {
            console.log("Invalid input. Please enter a valid integer.");
            continue;
        }
        if (number === -1) return -1;
        return number;
    }
}

export async function getValidAge(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        const age = parseInt(userInput, 10);
        if (isNaN(age) || age < 17 || age >= 50) {
            console.log("Student must be at least 17 years old and below 50.");
            continue;
        }
        return age;
    }
}

export async function getValidGender(prompt) {
    while (true) {
        const userInput = (await promptUser(prompt)).toUpperCase();
        if (userInput === "M" || userInput === "F") {
            return userInput;
        }
        console.log("Invalid gender. Please enter 'M' or 'F'.");
    }
}

export async function getValidNumOfSubjects(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        const numSubjects = parseInt(userInput, 10);
        if (isNaN(numSubjects) || ![7, 8].includes(numSubjects)) {
            console.log(
                "Invalid input. Please enter a valid number of subjects."
            );
            continue;
        }
        return numSubjects;
    }
}

export async function getValidUniqueSubject(marks, subject) {
    return new Promise(async (resolve) => {
        while (true) {
            if (
                Object.keys(marks)
                    .map((sub) => sub.toLowerCase())
                    .includes(subject.toLowerCase())
            ) {
                console.log(
                    `Subject '${subject}' already exists. Please enter a unique subject name.`
                );
                subject = await promptUser("Enter a different subject name: ");
            } else {
                resolve(subject);
                return;
            }
        }
    });
}

export async function getValidMark(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        const mark = parseInt(userInput, 10);
        if (isNaN(mark) || mark < 0 || mark > 100) {
            console.log("Invalid mark. Please enter a valid mark.");
            continue;
        }
        return mark;
    }
}

export async function getValidPhoneNumber(prompt) {
    while (true) {
        const userInput = await promptUser(prompt);
        if (
            userInput.toLowerCase() !== "n/a" &&
            (userInput.length < 8 ||
                userInput.trim() === "" ||
                isNaN(userInput))
        ) {
            console.log("Invalid input. Please enter a valid phone number.");
            continue;
        }
        return userInput;
    }
}

export async function getValidStudentID(prompt, students) {
    while (true) {
        const studentID = await promptUser(prompt);
        if (studentID === "-1") return "-1";
        if (
            students.some(
                (student) => student.generateStudentID() === studentID
            )
        ) {
            return studentID;
        } else {
            console.log("Invalid student ID. Please try again.");
        }
    }
}
