const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const tracks = [];
const balls = [];
const pentatonicRatios = [1, 9 / 8, 5 / 4, 3 / 2, 5 / 3];

const trackCenter = { x: canvas.width / 2, y: canvas.height / 2 };

let settings = {
    oscType: "sine",
    baseFreq: 293.66,
    trackShape: "semicircle",
};

const N = 20;
const trackMinRadius = 50;
const trackStep = 30;
const ballRadius = 10;
const ballMinSpeed = 0.005;
const speedStep = -0.0001;

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    trackCenter.x = canvas.width / 2;
    trackCenter.y = canvas.height / 2;
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    tracks.forEach((track) => track.draw(ctx));
    balls.forEach((ball) => ball.move());
    balls.forEach((ball) => ball.draw(ctx));
    requestAnimationFrame(animate);
}

function initTracks() {
    tracks.length = 0;
    balls.length = 0;

    const soundFrequencies = [];

    for (let i = 0; i < N; i++) {
        const octave = Math.floor(i / pentatonicRatios.length) + 4;
        const ratioIndex = i % pentatonicRatios.length;
        const frequency =
            settings.baseFreq *
            Math.pow(2, octave - 4) *
            pentatonicRatios[ratioIndex];
        soundFrequencies.push(parseFloat(frequency.toFixed(2)));
    }

    soundFrequencies.reverse();

    for (let i = 0; i < N; i++) {
        const trackRadius = trackMinRadius + i * trackStep;
        const ballSpeed = ballMinSpeed + i * speedStep;
        const ballSoundFrequency = soundFrequencies[i];
        const hue = (i * 360) / N;

        const track = new Track(
            trackCenter,
            trackRadius,
            hue,
            settings.trackShape
        );
        const ball = new Ball(
            track,
            ballRadius,
            ballSpeed,
            ballSoundFrequency,
            hue,
            settings.oscType
        );

        tracks.push(track);
        balls.push(ball);
    }
}

const baseFreqSlider = document.getElementById("base-freq");
const baseFreqInput = document.getElementById("freq-value");

baseFreqSlider.addEventListener("input", (e) => {
    baseFreqInput.value = e.target.value;
});

baseFreqInput.addEventListener("input", (e) => {
    let val = parseFloat(e.target.value);
    val = Math.max(100, Math.min(500, val));
    baseFreqSlider.value = val;
});

document.getElementById("osc-type").value = settings.oscType;
document.getElementById("track-shape").value = settings.trackShape;

document.getElementById("toggle-settings").addEventListener("click", () => {
    const panel = document.getElementById("settings-panel");
    panel.classList.toggle("visible");
});

document.getElementById("apply-btn").addEventListener("click", () => {
    settings.oscType = document.getElementById("osc-type").value;
    settings.baseFreq = parseFloat(document.getElementById("base-freq").value);
    settings.trackShape = document.getElementById("track-shape").value;

    initTracks();
});

document.getElementById("start-btn").addEventListener("click", () => {
    overlay = document.getElementById("start-overlay");
    overlay.style.opacity = 0;

    setTimeout(() => {
        overlay.style.display = "none";
    }, 500);

    if (audioCtx.state === "suspended") {
        audioCtx.resume();
    }

    initTracks();
    resizeCanvas();
    animate();
});

document.addEventListener("click", (e) => {
    const panel = document.getElementById("settings-panel");
    const toggle = document.getElementById("toggle-settings");

    if (
        panel.classList.contains("visible") &&
        !panel.contains(e.target) &&
        !toggle.contains(e.target)
    ) {
        panel.classList.remove("visible");
    }
});

window.addEventListener("resize", resizeCanvas);
