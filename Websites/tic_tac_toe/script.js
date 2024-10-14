import { easyMode, mediumMode, hardMode } from "./difficultyModes.js";
import { winConditions } from "./constants.js";

const cells = document.querySelectorAll(".cell");
const statusInfo = document.querySelector("#statusInfo");
const difficultyInfo = document.querySelector("#difficultyInfo");
const restartBtn = document.querySelector("#restartBtn");
const enableComputer = document.querySelector("#enableComputer");
const difficultyBtn = document.querySelector("#difficultyBtn");

let computerEnabled = false;
let currentDifficulty = "medium";
let options = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let running = false;

initialiseGame();

function initialiseGame() {
    cells.forEach((cell) => cell.addEventListener("click", cellClicked));
    restartBtn.addEventListener("click", restartGame);
    enableComputer.addEventListener("click", toggleComputer);
    difficultyBtn.addEventListener("click", switchDifficulty);
    statusInfo.textContent = `${currentPlayer}'s turn`;
    difficultyInfo.textContent = `Current Difficulty: ${capitalise(
        currentDifficulty
    )}`;
    running = true;
}

function restartGame() {
    currentPlayer = "X";
    options = ["", "", "", "", "", "", "", "", ""];
    statusInfo.textContent = `${currentPlayer}'s turn`;
    cells.forEach((cell) => {
        cell.textContent = "";
        cell.classList.remove("winner");
    });
    difficultyBtn.disabled = !computerEnabled;
    running = true;
}

function toggleComputer() {
    computerEnabled = !computerEnabled;
    enableComputer.textContent = computerEnabled
        ? "Play with Friend"
        : "Play with Computer";
    difficultyBtn.disabled = !computerEnabled;
    difficultyInfo.style.display = computerEnabled ? "block" : "none";

    restartGame();
}

function switchDifficulty() {
    if (currentDifficulty === "easy") {
        currentDifficulty = "medium";
    } else if (currentDifficulty === "medium") {
        currentDifficulty = "hard";
    } else {
        currentDifficulty = "easy";
    }
    difficultyInfo.textContent = `Current Difficulty: ${capitalise(
        currentDifficulty
    )}`;
}

function cellClicked() {
    const cellIndex = this.getAttribute("cellIndex");

    if (options[cellIndex] != "" || !running) {
        return;
    }

    updateCell(this, cellIndex);
    checkWinner();

    if (running && currentPlayer === "O" && computerEnabled) {
        cells.forEach((cell) => cell.removeEventListener("click", cellClicked));
        setTimeout(() => {
            computerMove();
            checkWinner();
            cells.forEach((cell) =>
                cell.addEventListener("click", cellClicked)
            );
        }, 420);
    }
}

function updateCell(cell, index) {
    options[index] = currentPlayer;

    const span = document.createElement("span");
    span.textContent = currentPlayer;

    if (currentPlayer === "X") {
        span.style.color = "#00c4ff";
    } else {
        span.style.color = "#ff3860";
    }

    cell.innerHTML = "";
    cell.appendChild(span);

    difficultyBtn.disabled = true;

    cell.classList.add("bounce");

    setTimeout(() => {
        cell.classList.remove("bounce");
    }, 600);
}

function changePlayer() {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    statusInfo.textContent = `${currentPlayer}'s turn`;
}

function computerMove() {
    let move;
    if (currentDifficulty === "easy") {
        move = easyMode(options);
    } else if (currentDifficulty === "medium") {
        move = mediumMode(options, currentPlayer);
    } else {
        move = hardMode(options);
    }

    if (move !== -1) {
        const cell = cells[move];
        const cellIndex = cell.getAttribute("cellIndex");
        updateCell(cell, cellIndex);
    }
}

function checkWinner() {
    let roundWon = false;
    let winningCombination = null;

    for (let i = 0; i < winConditions.length; i++) {
        const condition = winConditions[i];
        const cellA = options[condition[0]];
        const cellB = options[condition[1]];
        const cellC = options[condition[2]];

        if (cellA === "" || cellB === "" || cellC === "") {
            continue;
        }

        if (cellA === cellB && cellB === cellC) {
            roundWon = true;
            winningCombination = condition;
            break;
        }
    }

    if (roundWon) {
        statusInfo.textContent = `${currentPlayer} wins!`;
        highlightWinner(winningCombination);
        difficultyBtn.disabled = false;
        running = false;
    } else if (!options.includes("")) {
        statusInfo.textContent = "Draw!";
        setTimeout(restartGame, 1000);
        difficultyBtn.disabled = false;
        running = false;
    } else {
        changePlayer();
    }
}

function highlightWinner(combination) {
    combination.forEach((index) => {
        const cell = cells[index];
        cell.classList.add("winner");
    });
}

function capitalise(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
