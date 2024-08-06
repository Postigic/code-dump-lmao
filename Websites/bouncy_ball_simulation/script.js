import Ball from "./ballClass.js";
import { BALL_COUNT } from "./constants.js";

const canvas = document.getElementById("canvas");
const ballCountElement = document.getElementById("ballCount");
const resetButton = document.getElementById("restartButton");
const addBallButton = document.getElementById("addBallButton");

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

engine.gravity.y = 0.35;

const mouse = Matter.Mouse.create(canvas);
const mouseConstraint = Matter.MouseConstraint.create(engine, {
    mouse: mouse,
    constraint: {
        stiffness: 0.2,
        render: {
            visible: false,
        },
    },
});
Matter.World.add(engine.world, mouseConstraint);

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

function handleMouseEvents(event) {
    const mousePosition = {
        x: event.clientX,
        y: event.clientY,
    };

    let isOverBall = balls.some((ball) => {
        const distance = Math.sqrt(
            (mousePosition.x - ball.body.position.x) ** 2 +
                (mousePosition.y - ball.body.position.y) ** 2
        );
        return distance < ball.radius;
    });

    canvas.style.cursor = isOverBall ? "pointer" : "default";
}

canvas.addEventListener("click", handleMouseEvents);
canvas.addEventListener("mousemove", handleMouseEvents);

resetButton.addEventListener("click", restart);

addBallButton.addEventListener("click", () => {
    const newBall = new Ball(canvas.width, canvas.height, engine);
    balls.push(newBall);
    updateBallCount();
});

function update() {
    updateBallCount();
}

function loop() {
    Matter.Engine.update(engine);
    update();
    requestAnimationFrame(loop);
}

Matter.Runner.run(engine);
Matter.Render.run(render);

loop();
