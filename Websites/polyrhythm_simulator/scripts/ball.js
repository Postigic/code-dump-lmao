class Ball {
    constructor(track, radius, speed, soundFrequency, hue) {
        this.track = track;
        this.radius = radius;
        this.speed = speed;
        this.soundFrequency = soundFrequency;
        this.hue = hue;
        this.offset = 0;
        this.round = 0;
        this.progress = 0;
        this.center = this.track.getPosition(this.offset);
    }

    draw(ctx) {
        const lightness = 100 - 50 * this.progress;
        const gradient = ctx.createRadialGradient(
            this.center.x,
            this.center.y,
            0,
            this.center.x,
            this.center.y,
            this.radius
        );

        gradient.addColorStop(0, `hsl(${this.hue}, 100%, 80%)`);
        gradient.addColorStop(1, `hsl(${this.hue}, 100%, ${lightness}%)`);

        ctx.beginPath();
        ctx.arc(this.center.x, this.center.y, this.radius, 0, 2 * Math.PI);
        ctx.fillStyle = gradient;
        ctx.shadowBlur = 15;
        ctx.shadowColor = `hsla(${this.hue}, 100%, 50%, 0.7)`;
        ctx.fill();
        ctx.shadowBlur = 0;
        ctx.strokeStyle = "white";
        ctx.stroke();
    }

    move() {
        this.offset += this.speed;
        const res = this.track.getPosition(this.offset);
        this.center = { x: res.x, y: res.y };
        this.progress = res.progress;

        if (res.round !== this.round) {
            this.round = res.round;
            playSound(this.soundFrequency);
        }
    }
}
