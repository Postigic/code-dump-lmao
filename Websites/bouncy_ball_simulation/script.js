import Ball from "./ballClass.js";
import { BALL_COUNT } from "./constants.js";

const canvas = document.getElementById("canvas");
const resetButton = document.getElementById("restartButton");
const ballCountElement = document.getElementById("ballCount");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const engine = Matter.Engine.create();
const render = Matter.Render.create({
    canvas: canvas,
    engine: engine,
    options: {
        width: canvas.width,
        height: canvas.height,
        wireframes: false,
    },
});

engine.gravity.y = 0.45;

let balls = createBalls(engine);
createBoundaries(engine);

function createBalls(engine) {
    return Array.from(
        { length: BALL_COUNT },
        () => new Ball(canvas.width, canvas.height, engine)
    );
}

function createBoundary(x, y, width, height, options = {}) {
    return Matter.Bodies.rectangle(x, y, width, height, {
        isStatic: true,
        ...options,
    });
}

function createBoundaries(engine) {
    const thickness = 500;
    const ground = createBoundary(
        canvas.width / 2,
        canvas.height + thickness / 2,
        canvas.width,
        thickness
    );
    const leftWall = createBoundary(
        -thickness / 2,
        canvas.height / 2,
        thickness,
        canvas.height
    );
    const rightWall = createBoundary(
        canvas.width + thickness / 2,
        canvas.height / 2,
        thickness,
        canvas.height
    );
    const ceiling = createBoundary(
        canvas.width / 2,
        -thickness / 2,
        canvas.width,
        thickness
    );

    Matter.World.add(engine.world, [ground, leftWall, rightWall, ceiling]);
}

function restart() {
    balls.forEach((ball) => Matter.World.remove(engine.world, ball.body));

    balls = createBalls(engine);
    Matter.World.add(engine.world, balls);
    updateBallCount();
}

function updateBallCount() {
    ballCountElement.textContent = `Balls: ${balls.length}`;
}

Matter.Runner.run(engine);
Matter.Render.run(render);

resetButton.addEventListener("click", restart);

function update() {
    updateBallCount();
}

function loop() {
    Matter.Engine.update(engine);
    update();
    requestAnimationFrame(loop);
}

loop();
