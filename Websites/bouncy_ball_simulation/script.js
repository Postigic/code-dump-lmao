import Ball from "./ballClass.js";

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const gravity = 0.15;
const bounce = 0.95;

// Create ball instances
let balls = createBalls();

function createBalls() {
    return [
        new Ball(5, "red", canvas.width, canvas.height, gravity, bounce),
        new Ball(10, "orange", canvas.width, canvas.height, gravity, bounce),
        new Ball(15, "yellow", canvas.width, canvas.height, gravity, bounce),
        new Ball(20, "green", canvas.width, canvas.height, gravity, bounce),
        new Ball(25, "blue", canvas.width, canvas.height, gravity, bounce),
    ];
}

function detectCollision(ball1, ball2) {
    const dx = ball1.x - ball2.x;
    const dy = ball1.y - ball2.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    return distance < ball1.radius + ball2.radius;
}

function resolveCollision(ball1, ball2) {
    // Calculate normal vector
    const dx = ball1.x - ball2.x;
    const dy = ball1.y - ball2.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const nx = dx / distance;
    const ny = dy / distance;

    // Calculate relative velocity
    const v1n = ball1.vx * nx + ball1.vy * ny;
    const v2n = ball2.vx * nx + ball2.vy * ny;

    // Calculate new velocities
    const combinedMass = ball1.mass + ball2.mass;
    const coefficientOfRestitution = 0.7;

    const v1nNew =
        ((ball1.mass - ball2.mass) * v1n + 2 * ball2.mass * v2n) / combinedMass;
    const v2nNew =
        ((ball2.mass - ball1.mass) * v2n + 2 * ball1.mass * v1n) / combinedMass;

    const velocityOverlap = (ball1.radius + ball2.radius - distance) / 2;

    // Update velocities
    ball1.x += velocityOverlap * nx;
    ball1.y += velocityOverlap * ny;
    ball2.x -= velocityOverlap * nx;
    ball2.y -= velocityOverlap * ny;

    ball1.vx += (v1nNew - v1n) * nx;
    ball1.vy += (v1nNew - v1n) * ny;
    ball2.vx += (v2nNew - v2n) * nx;
    ball2.vy += (v2nNew - v2n) * ny;

    // Apply bounce
    ball1.vx *= coefficientOfRestitution;
    ball1.vy *= coefficientOfRestitution;
    ball2.vx *= coefficientOfRestitution;
    ball2.vy *= coefficientOfRestitution;
}

function update() {
    balls.forEach((ball) => ball.update());

    // Check for ball collisions
    for (let i = 0; i < balls.length; i++) {
        for (let j = i + 1; j < balls.length; j++) {
            if (detectCollision(balls[i], balls[j])) {
                resolveCollision(balls[i], balls[j]);
            }
        }
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    balls.forEach((ball) => ball.draw(ctx));
}

function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

function restart() {
    balls = createBalls();
}

loop();

document.getElementById("restartButton").addEventListener("click", restart);
