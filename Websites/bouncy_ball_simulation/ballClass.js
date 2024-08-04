class Ball {
    constructor(radius, color, canvasWidth, canvasHeight, gravity, bounce) {
        this.radius = radius;
        this.mass = this.calculateMass();
        this.x = this.getRandomPosition(canvasWidth, radius);
        this.y = this.getRandomPosition(canvasHeight, radius);
        this.vx = Math.random() * 4 - 2;
        this.vy = Math.random() * -4;
        this.color = color;
        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;
        this.gravity = gravity;
        this.bounce = bounce;
    }

    calculateMass() {
        const density = 0.008;
        return density * (4 / 3) * Math.PI * Math.pow(this.radius, 3);
    }

    getRandomPosition(max, radius) {
        return Math.random() * (max - 2 * radius) + radius;
    }

    reset() {
        this.x = this.getRandomPosition(this.canvasWidth, this.radius);
        this.y = this.getRandomPosition(this.canvasHeight, this.radius);
        this.vx = Math.random() * 4 - 2;
        this.vy = Math.random() * -4;
    }

    update() {
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;

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

    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }
}

export default Ball;
