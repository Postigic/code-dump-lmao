import { createInterface } from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
});

const num = Math.floor(Math.random() * 101);
let tries = 1;

console.log("Number Guessing Game!");
console.log("*********************\n");

function askQuestion() {
    rl.question("Enter a number between 1 to 100: ", (answer) => {
        const guess = parseInt(answer);

        if (isNaN(guess) || guess < 1 || guess > 100) {
            console.log("Please enter a valid number between 1 and 100.");
            askQuestion();
        } else if (guess < num) {
            console.log("Too low! Try again.");
            tries++;
            askQuestion();
        } else if (guess > num) {
            console.log("Too high! Try again.");
            tries++;
            askQuestion();
        } else {
            console.log(
                `Congratulations! You guessed the number ${num} in ${tries} tries.`
            );
            rl.close();
        }
    });
}

askQuestion();
