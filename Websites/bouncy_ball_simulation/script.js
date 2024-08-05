import Ball from "./ballClass.js";

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const resetButton = document.getElementById("restartButton");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const BALL_COUNT = 10;
const GRAVITY = 0.15;
const BOUNCE = 1.0;
const COEFFICIENT_OF_RESTITUTION = 0.7;

let balls = createBalls();

/**
 * Create an array of Ball instances.
 * @returns {Ball[]} Array of Ball instances.
 */
function createBalls() {
    const ballsArray = [];
    for (let i = 0; i < BALL_COUNT; i++) {
        ballsArray.push(new Ball(canvas.width, canvas.height, GRAVITY, BOUNCE));
    }
    return ballsArray;
}

/**
 * Detect if two balls are colliding.
 * @param {Ball} ball1 - The first ball.
 * @param {Ball} ball2 - The second ball.
 * @returns {boolean} True if the balls are colliding, false otherwise.
 */
function detectCollision(ball1, ball2) {
    const dx = ball1.x - ball2.x;
    const dy = ball1.y - ball2.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    return distance < ball1.radius + ball2.radius;
}

/**
 * Resolve the collision between two balls.
 * @param {Ball} ball1 - The first ball.
 * @param {Ball} ball2 - The second ball.
 */
function resolveCollision(ball1, ball2) {
    const dx = ball1.x - ball2.x;
    const dy = ball1.y - ball2.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const nx = dx / distance;
    const ny = dy / distance;

    const v1n = ball1.vx * nx + ball1.vy * ny;
    const v2n = ball2.vx * nx + ball2.vy * ny;

    const combinedMass = ball1.mass + ball2.mass;

    const v1nNew =
        ((ball1.mass - ball2.mass) * v1n + 2 * ball2.mass * v2n) / combinedMass;
    const v2nNew =
        ((ball2.mass - ball1.mass) * v2n + 2 * ball1.mass * v1n) / combinedMass;

    const velocityOverlap = ball1.radius + ball2.radius - distance;

    ball1.x += velocityOverlap * nx;
    ball1.y += velocityOverlap * ny;
    ball2.x -= velocityOverlap * nx;
    ball2.y -= velocityOverlap * ny;

    ball1.vx += (v1nNew - v1n) * nx;
    ball1.vy += (v1nNew - v1n) * ny;
    ball2.vx += (v2nNew - v2n) * nx;
    ball2.vy += (v2nNew - v2n) * ny;

    ball1.vx *= COEFFICIENT_OF_RESTITUTION;
    ball1.vy *= COEFFICIENT_OF_RESTITUTION;
    ball2.vx *= COEFFICIENT_OF_RESTITUTION;
    ball2.vy *= COEFFICIENT_OF_RESTITUTION;
}

/**
 * Update the positions and velocities of all balls, and resolve collisions.
 */
function update() {
    balls.forEach((ball) => ball.update());

    for (let i = 0; i < balls.length; i++) {
        for (let j = i + 1; j < balls.length; j++) {
            if (detectCollision(balls[i], balls[j])) {
                resolveCollision(balls[i], balls[j]);
            }
        }
    }
}

/**
 * Clear the canvas and draw all balls.
 */
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    balls.forEach((ball) => ball.draw(ctx));
    drawBallCount();
}

/**
 * Main animation loop.
 */
function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

/**
 * Draw the count of balls on the canvas.
 */
function drawBallCount() {
    ctx.fillStyle = "white";
    ctx.font = "20px Noto Sans";
    ctx.fillText(`Balls: ${balls.length}`, 10, 30);
}

/**
 * Restart the simulation with a new set of balls.
 */
function restart() {
    balls = createBalls();
}

// Start the animation loop
loop();

// Attach event listener to the reset button
resetButton.addEventListener("click", restart);
