import { winConditions } from "./constants.js";

export function easyMode(options) {
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

export function mediumMode(options, currentPlayer) {
    console.log(winConditions);
    const winningMove = findWinningMove(currentPlayer, winConditions);
    if (winningMove !== -1) {
        return winningMove;
    }

    const opponent = currentPlayer === "X" ? "O" : "X";
    const blockingMove = findWinningMove(options, opponent, winConditions);
    if (blockingMove !== -1) {
        return blockingMove;
    }

    if (options[4] === "") {
        return 4;
    }

    const corners = [0, 2, 6, 8];
    for (let corner of corners) {
        if (options[corner] === "") {
            return corner;
        }
    }

    const sides = [1, 3, 5, 7];
    for (let side of sides) {
        if (options[side] === "") {
            return side;
        }
    }

    return -1;
}

function findWinningMove(options, player) {
    for (let i = 0; i < winConditions.length; i++) {
        const condition = winConditions[i];
        const [a, b, c] = condition;

        const playerCount = [options[a], options[b], options[c]].filter(
            (option) => option === player
        ).length;
        const emptyCount = [options[a], options[b], options[c]].filter(
            (option) => option === ""
        ).length;

        if (playerCount === 2 && emptyCount === 1) {
            return condition.find((index) => options[index] === "");
        }
    }
    return -1;
}

export function hardMode(options) {
    let bestScore = -Infinity;
    let move = -1;

    for (let i = 0; i < options.length; i++) {
        if (options[i] === "") {
            options[i] = "O";
            let score = minimax(options, winConditions, 0, false);
            options[i] = "";

            if (score > bestScore) {
                bestScore = score;
                move = i;
            }
        }
    }

    return move;
}

function minimax(newOptions, depth, isMaximising) {
    const result = predictWinner(newOptions, winConditions);
    if (result === "X") return -1;
    if (result === "O") return 1;
    if (result === "draw") return 0;

    if (isMaximising) {
        let bestScore = -Infinity;
        for (let i = 0; i < newOptions.length; i++) {
            if (newOptions[i] === "") {
                newOptions[i] = "O";
                let score = minimax(newOptions, depth + 1, false);
                newOptions[i] = "";
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < newOptions.length; i++) {
            if (newOptions[i] === "") {
                newOptions[i] = "X";
                let score = minimax(newOptions, depth + 1, true);
                newOptions[i] = "";
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

function predictWinner(options) {
    for (let i = 0; i < winConditions.length; i++) {
        const [a, b, c] = winConditions[i];

        if (
            options[a] &&
            options[a] === options[b] &&
            options[a] === options[c]
        ) {
            return options[a];
        }
    }
    return options.includes("") ? null : "draw";
}
