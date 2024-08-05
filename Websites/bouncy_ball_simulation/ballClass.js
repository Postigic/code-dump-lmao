const DEFAULT_DENSITY = 0.008;
const MIN_RADIUS = 10;
const MAX_RADIUS = 30;
const VELOCITY_RANGE = 4;

class Ball {
    constructor(canvasWidth, canvasHeight, gravity, bounce) {
        this.radius = Math.random() * MAX_RADIUS + MIN_RADIUS;
        this.mass = this.calculateMass();
        this.x = this.getRandomPosition(canvasWidth, this.radius);
        this.y = this.getRandomPosition(canvasHeight, this.radius);
        this.vx = this.getRandomVelocity();
        this.vy = this.getRandomVelocity(true);
        this.color = this.getRandomColor();
        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;
        this.gravity = gravity;
        this.bounce = bounce;
    }

    // Calculate the mass of the ball based on its radius and density
    calculateMass() {
        return DEFAULT_DENSITY * (4 / 3) * Math.PI * Math.pow(this.radius, 3);
    }

    // Generate a random position within the canvas, ensuring the ball is fully visible
    getRandomPosition(max, radius) {
        return Math.random() * (max - 2 * radius) + radius;
    }

    // Generate a random velocity within the specified range
    getRandomVelocity(negative = false) {
        const velocity = Math.random() * VELOCITY_RANGE - VELOCITY_RANGE / 2;
        return negative ? velocity : Math.abs(velocity);
    }

    // Generate a random color in HSL format
    getRandomColor() {
        return `hsl(${Math.random() * 360}, 100%, 50%)`;
    }

    // Reset the ball to a random position and velocity
    reset() {
        this.x = this.getRandomPosition(this.canvasWidth, this.radius);
        this.y = this.getRandomPosition(this.canvasHeight, this.radius);
        this.vx = this.getRandomVelocity();
        this.vy = this.getRandomVelocity(true);
    }

    // Update the ball's position based on its velocity and apply gravity
    update() {
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;

        this.checkCollisionWithBounds();
    }

    // Check for collision with canvas bounds and apply bounce
    checkCollisionWithBounds() {
        // Check for collision with the ground
        if (this.y + this.radius > this.canvasHeight) {
            this.y = this.canvasHeight - this.radius;
            this.vy *= -this.bounce;
        }

        // Check for collision with the top edge
        if (this.y - this.radius < 0) {
            this.y = this.radius;
            this.vy *= -this.bounce;
        }

        // Check for collision with the left edge
        if (this.x - this.radius < 0) {
            this.x = this.radius;
            this.vx *= -this.bounce;
        }

        // Check for collision with the right edge
        if (this.x + this.radius > this.canvasWidth) {
            this.x = this.canvasWidth - this.radius;
            this.vx *= -this.bounce;
        }
    }

    // Draw the ball on the canvas
    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }
}

export default Ball;
