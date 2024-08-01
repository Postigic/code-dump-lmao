const cells = document.querySelectorAll(".cell");
const statusInfo = document.querySelector("#statusInfo");
const restartBtn = document.querySelector("#restartBtn");
const enableComputer = document.querySelector("#enableComputer");
const winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

let computerEnabled = false;
let options = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let running = false;

initialiseGame();

function initialiseGame() {
    cells.forEach((cell) => cell.addEventListener("click", cellClicked));
    restartBtn.addEventListener("click", restartGame);
    enableComputer.addEventListener("click", toggleComputer);
    statusInfo.textContent = `${currentPlayer}'s turn`;
    running = true;
}

function toggleComputer() {
    if (!computerEnabled) {
        computerEnabled = true;
        enableComputer.textContent = "Play with Friend";
        restartGame();
    } else {
        computerEnabled = false;
        enableComputer.textContent = "Play with Computer";
        restartGame();
    }
}

function restartGame() {
    currentPlayer = "X";
    options = ["", "", "", "", "", "", "", "", ""];
    statusInfo.textContent = `${currentPlayer}'s turn`;
    cells.forEach((cell) => (cell.textContent = ""));
    running = true;
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
    cell.textContent = currentPlayer;
}

function changePlayer() {
    currentPlayer = currentPlayer == "X" ? "O" : "X";
    statusInfo.textContent = `${currentPlayer}'s turn`;
}

function computerMove() {
    const move = randomMove();
    if (move !== -1) {
        const cell = cells[move];
        const cellIndex = cell.getAttribute("cellIndex");
        updateCell(cell, cellIndex);
    }
}

function randomMove() {
    let availableMoves = [];

    for (let i = 0; i < options.length; i++) {
        if (options[i] === "") {
            availableMoves.push(i);
        }
    }

    if (availableMoves.length === 0) {
        return -1;
    }

    const randomIndex = Math.floor(Math.random() * availableMoves.length);
    return availableMoves[randomIndex];
}

function checkWinner() {
    let roundWon = false;

    for (let i = 0; i < winConditions.length; i++) {
        const condition = winConditions[i];
        const cellA = options[condition[0]];
        const cellB = options[condition[1]];
        const cellC = options[condition[2]];

        if (cellA == "" || cellB == "" || cellC == "") {
            continue;
        }
        if (cellA == cellB && cellB == cellC) {
            roundWon = true;
            break;
        }
    }

    if (roundWon) {
        statusInfo.textContent = `${currentPlayer} wins!`;
        running = false;
    } else if (!options.includes("")) {
        statusInfo.textContent = "Draw!";
        running = false;
    } else {
        changePlayer();
    }
}
