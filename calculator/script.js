// INPUT DETECTION

const screen = document.querySelector(".screen");

// VARIABLES

let totalResults = 0;
let currentInput = "0";
let chosenOperator;
let hasDecimal = false;

// FUNCTIONS

function buttonClick(value) {
    if (isNaN(value)) {
        // If it's not a number, it's a symbol
        handleSymbol(value);
    } else {
        // Else, it's a number
        handleNumber(value);
    }
    screen.innerText = currentInput;
}

function handleSymbol(symbol) {
    switch (symbol) {
        case "C":
            // Clear the calculator
            currentInput = "0";
            totalResults = 0;
            hasDecimal = false;
            break;
        case "=":
            if (chosenOperator === null) {
                // If chosen operator was null return nothing
                return;
            }
            if (chosenOperator === "x^") {
                // If chosen operator was x^ calculate the exponent
                const exponent = parseFloat(currentInput);
                totalResults = Math.pow(totalResults, exponent); // Update total results with exponentiation
            } else {
                // Perform normal arithmetic operation
                performArithmetic(parseFloat(currentInput));
            }
            // Reset calculator state
            chosenOperator = null;
            currentInput = totalResults.toString();
            totalResults = 0;
            hasDecimal = currentInput.includes(".");
            break;
        case "√x":
            handleSquareRoot();
            break;
        case "x^":
            handleExponent();
            break;
        case "x!":
            handleFactorial();
            break;
        case ".":
            handleDecimal();
            break;
        case "←":
            if (currentInput.length === 1) {
                // If current input has only 1 character
                currentInput = "0";
            } else {
                // Remove one character from current input
                currentInput = currentInput.substring(
                    0,
                    currentInput.length - 1
                );
            }
            break;
        case "+":
        case "−":
        case "×":
        case "÷":
            handleMath(symbol);
            break;
    }
}

function handleMath(symbol) {
    if (currentInput === "0") {
        // If input is 0 just return 0
        return;
    }

    const inCurrentInput = parseFloat(currentInput);
    // Convert string to float

    if (totalResults === 0) {
        totalResults = inCurrentInput;
    } else {
        performArithmetic(inCurrentInput);
    }
    chosenOperator = symbol;
    currentInput = "0";
    hasDecimal = false;
}

function handleNumber(numberString) {
    if (currentInput === "0") {
        // If input is 0 just return 0
        currentInput = numberString;
    } else {
        currentInput += numberString;
        if (numberString === ".") {
            hasDecimal = true;
        }
    }
}

function handleDecimal() {
    if (!hasDecimal) {
        currentInput += ".";
        hasDecimal = true;
    }
}

function handleSquareRoot() {
    if (currentInput === "0") {
        // If input is 0 just return 0
        return;
    }
    currentInput = Math.sqrt(parseFloat(currentInput)).toString();
}

function handleExponent() {
    if (currentInput === "0") {
        // If input is 0 just return 0
        return;
    }

    const base = parseFloat(currentInput);
    chosenOperator = "x^"; // Mark that exponentiation is in progress
    totalResults = base;
    currentInput = "0";
    hasDecimal = false;
}

function handleFactorial() {
    if (currentInput === "0") {
        // If input is 0 just return 0
        return;
    }

    const number = parseFloat(currentInput);
    if (Number.isInteger(number) && number >= 0 && number <= 69) {
        let result = 1;
        for (let i = 2; i <= number; i++) {
            result *= i;
        }
        currentInput = result.toString();
    } else {
        // Handle invalid input, like infinity
        currentInput = "Math ERROR";
    }
}

function performArithmetic(inCurrentInput) {
    if (chosenOperator === "+") {
        totalResults += inCurrentInput;
    } else if (chosenOperator === "−") {
        totalResults -= inCurrentInput;
    } else if (chosenOperator === "×") {
        totalResults *= inCurrentInput;
    } else if (chosenOperator === "÷") {
        totalResults /= inCurrentInput;
    }
}

function init() {
    // Event listener
    document
        .querySelector(".calc_buttons")
        .addEventListener("click", function (event) {
            buttonClick(event.target.innerText);
        });
}

// haha the only non function

init();
