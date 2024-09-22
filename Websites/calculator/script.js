const screen = document.querySelector(".screen");

let totalResults = 0;
let currentInput = "0";
let chosenOperator = null;
let hasDecimal = false;
let isDegreeMode = true;

function buttonClick(value) {
    if (isNaN(value)) {
        handleSymbol(value);
    } else {
        handleNumber(value);
    }

    screen.innerText = currentInput;
    console.log("Current input before display:", currentInput);
}

function handleSymbol(symbol) {
    switch (symbol) {
        case "AC":
            clearCalculator();
            break;
        case "=":
            calculateResult();
            break;
        case "√x":
            handleSquareRoot();
            break;
        case "x^":
            handleExponent();
            break;
        case "x^2":
            updateCurrentInput(Math.pow(parseFloat(currentInput), 2));
            break;
        case "x^3":
            updateCurrentInput(Math.pow(parseFloat(currentInput), 3));
            break;
        case "x!":
            handleFactorial();
            break;
        case "sin(x)":
            handleTrigonometric(Math.sin);
            break;
        case "cos(x)":
            handleTrigonometric(Math.cos);
            break;
        case "tan(x)":
            handleTrigonometric(Math.tan);
            break;
        case "π":
            updateCurrentInput(Math.PI);
            break;
        case "e":
            updateCurrentInput(Math.E);
            break;
        case "ln":
            handleLog(Math.log);
            break;
        case "log":
            handleLog(Math.log10);
            break;
        case ".":
            handleDecimal();
            break;
        case "←":
            handleBackspace();
            break;
        case "+":
        case "−":
        case "×":
        case "÷":
            handleMath(symbol);
            break;
        case "DEG/RAD":
            toggleAngleUnit();
            break;
        case "+/-":
            toggleSign();
            break;
    }
}

function updateCurrentInput(value) {
    currentInput = formatResult(value);
    hasDecimal = currentInput.includes(".");
}

function clearCalculator() {
    currentInput = "0";
    totalResults = 0;
    hasDecimal = false;
}

function calculateResult() {
    if (chosenOperator === null) {
        return;
    }
    if (chosenOperator === "x^") {
        const exponent = parseFloat(currentInput);
        totalResults = Math.pow(totalResults, exponent);
    } else {
        performArithmetic(parseFloat(currentInput));
    }

    chosenOperator = null;
    currentInput = totalResults.toString();
    hasDecimal = currentInput.includes(".");
}

function applyMathFunction(mathFunc, errorCheck = null) {
    const value = parseFloat(currentInput);
    if (errorCheck && errorCheck(value)) {
        currentInput = "Math ERROR";
        return;
    }
    updateCurrentInput(mathFunc(value));
}

function handleBackspace() {
    currentInput = currentInput.length === 1 ? "0" : currentInput.slice(0, -1);
}

function handleMath(symbol) {
    if (currentInput === "0") {
        return;
    }

    const inCurrentInput = parseFloat(currentInput);
    if (totalResults === 0 && chosenOperator === null) {
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
        currentInput = numberString;
    } else {
        currentInput += numberString;
    }
}

function handleDecimal() {
    if (!hasDecimal) {
        currentInput += ".";
        hasDecimal = true;
    }
}

function handleSquareRoot() {
    applyMathFunction(Math.sqrt, (v) => v < 0);
}

function handleLog(func) {
    applyMathFunction(func, (v) => v <= 0);
}

function handleExponent() {
    if (currentInput === "0") return;

    totalResults = parseFloat(currentInput);
    chosenOperator = "x^";
    currentInput = "0";
    hasDecimal = false;
}

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function handleFactorial() {
    const number = parseInt(currentInput, 10);
    if (Number.isNaN(number) || number < 0 || number > 69) {
        handleError("Math ERROR");
    } else {
        updateCurrentInput(factorial(number));
    }
}

function toggleAngleUnit() {
    isDegreeMode = !isDegreeMode;
    document.querySelector(".mode-display").innerText = isDegreeMode
        ? "DEG"
        : "RAD";
}

function toRadians(degrees) {
    return degrees * (Math.PI / 180);
}

function handleTrigonometric(func) {
    let angle = parseFloat(currentInput);
    if (isDegreeMode) angle = toRadians(angle);

    const result = func(angle);
    updateCurrentInput(result);
}

function toggleSign() {
    if (currentInput !== "0") {
        currentInput = (-parseFloat(currentInput)).toString();
    }
}

function formatResult(result) {
    return Number(parseFloat(result).toFixed(10)).toString();
}

function handleError(message) {
    currentInput = message;
}

function performArithmetic(inCurrentInput) {
    switch (chosenOperator) {
        case "+":
            totalResults += inCurrentInput;
            break;
        case "−":
            totalResults -= inCurrentInput;
            break;
        case "×":
            totalResults *= inCurrentInput;
            break;
        case "÷":
            if (inCurrentInput === 0) {
                return handleError("Math ERROR");
            }
            totalResults /= inCurrentInput;
            break;
    }
}

function init() {
    document
        .querySelector(".calc_buttons")
        .addEventListener("click", function (event) {
            if (event.target.tagName === "BUTTON") {
                buttonClick(event.target.innerText);
            }
        });
}

init();
