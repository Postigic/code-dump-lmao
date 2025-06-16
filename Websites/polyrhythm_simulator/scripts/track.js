class Track {
    constructor(center, radius, hue, shape = "semicircle") {
        this.center = center;
        this.radius = radius;
        this.hue = hue;
        this.shape = shape;
        this.period = Math.PI;
    }

    draw(ctx) {
        ctx.beginPath();

        switch (this.shape) {
            case "circle":
                ctx.arc(
                    this.center.x,
                    this.center.y,
                    this.radius,
                    0,
                    2 * Math.PI
                );
                break;
            default:
                ctx.arc(
                    this.center.x,
                    this.center.y,
                    this.radius,
                    0,
                    Math.PI,
                    true
                );
        }

        ctx.strokeStyle = `hsl(${this.hue}, 80%, 60%)`;
        ctx.lineWidth = 2;
        ctx.shadowBlur = 10;
        ctx.shadowColor = `hsla(${this.hue}, 100%, 50%, 0.5)`;
        ctx.stroke();
        ctx.shadowBlur = 0;
    }

    getPosition(offset) {
        let x, y;

        switch (this.shape) {
            case "circle":
                x = this.center.x + this.radius * Math.cos(offset);
                y = this.center.y + this.radius * Math.sin(offset);
                this.period = 2 * Math.PI;
                break;
            default:
                x = this.center.x + this.radius * Math.cos(offset);
                y = this.center.y - this.radius * Math.abs(Math.sin(offset));
        }

        return {
            x,
            y,
            round: Math.floor(offset / this.period),
            progress: (offset % this.period) / this.period,
        };
    }
}
