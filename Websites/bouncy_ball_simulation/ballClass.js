import {
    COEFFICIENT_OF_RESTITUTION,
    DEFAULT_DENSITY,
    MIN_RADIUS,
    MAX_RADIUS,
    VELOCITY_RANGE,
} from "./constants.js";

class Ball {
    constructor(canvasWidth, canvasHeight, engine) {
        this.radius = this.getRandomRadius();
        this.x = this.getRandomPosition(canvasWidth, this.radius);
        this.y = this.getRandomPosition(canvasHeight, this.radius);
        this.vx = this.getRandomVelocity();
        this.vy = this.getRandomVelocity(true);
        this.color = this.getRandomColor();

        this.body = Matter.Bodies.circle(this.x, this.y, this.radius, {
            restitution: COEFFICIENT_OF_RESTITUTION,
            density: DEFAULT_DENSITY,
            render: {
                fillStyle: this.color,
            },
        });

        Matter.Body.setVelocity(this.body, {
            x: this.vx,
            y: this.vy,
        });

        Matter.World.add(engine.world, this.body);
    }

    getRandomRadius() {
        return Math.random() * (MAX_RADIUS - MIN_RADIUS) + MIN_RADIUS;
    }

    getRandomPosition(max, radius) {
        return Math.random() * (max - 2 * radius) + radius;
    }

    getRandomVelocity() {
        return Math.random() * VELOCITY_RANGE * 2 - VELOCITY_RANGE;
    }

    getRandomColor() {
        return `hsl(${Math.random() * 360}, 100%, 50%)`;
    }
}

export default Ball;
