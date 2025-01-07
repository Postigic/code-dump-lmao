const canvas = document.getElementById("waveCanvas");
const ctx = canvas.getContext("2d");

const amplitudeInput = document.getElementById("amplitude");
const frequencyInput = document.getElementById("frequency");
const verticalShiftInput = document.getElementById("vertical-shift");
const combineCosineCheckbox = document.getElementById("combineCosine");
// const combineTangentCheckbox = document.getElementById("combineTangent");
// tangent does not work at all this sucks :(

let amplitude = parseFloat(amplitudeInput.value);
let frequency = parseFloat(frequencyInput.value);
let verticalShift = parseFloat(verticalShiftInput.value);
let combineCosine = combineCosineCheckbox.checked;
// let combineTangent = combineTangentCheckbox.checked;

let time = 0;
const speed = 0.01;

amplitudeInput.addEventListener(
    "input",
    () => (amplitude = parseFloat(amplitudeInput.value))
);
frequencyInput.addEventListener(
    "input",
    () => (frequency = parseFloat(frequencyInput.value))
);
verticalShiftInput.addEventListener(
    "input",
    () => (verticalShift = parseFloat(verticalShiftInput.value))
);
combineCosineCheckbox.addEventListener(
    "change",
    () => (combineCosine = combineCosineCheckbox.checked)
);
// combineTangentCheckbox.addEventListener(
//     "change",
//     () => (combineTangent = combineTangentCheckbox.checked)
// );

function calculateWaveValue(x) {
    const t = (x / canvas.width) * (2 * Math.PI);
    let y = amplitude * Math.sin(frequency * t + time) + verticalShift;

    if (combineCosine) {
        y += amplitude * Math.cos(frequency * t + time);
    }

    // if (combineTangent) {
    //     let tangentValue = Math.tan(frequency * t + time);
    //     const maxTangentValue = 10;
    //     tangentValue = Math.min(
    //         Math.max(tangentValue, -maxTangentValue),
    //         maxTangentValue
    //     );
    //     y += amplitude * tangentValue;
    // }

    return y;
}

function drawWave() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.strokeStyle = "#ccc";
    ctx.moveTo(0, canvas.height / 2);
    ctx.lineTo(canvas.width, canvas.height / 2);
    ctx.stroke();

    ctx.beginPath();
    ctx.strokeStyle = "#007bff";
    for (let x = 0; x < canvas.width; x++) {
        const y = calculateWaveValue(x);
        const canvasY = canvas.height / 2 - y;

        if (x === 0) {
            ctx.moveTo(x, canvasY);
        } else {
            ctx.lineTo(x, canvasY);
        }
    }
    ctx.stroke();

    const trackX = 100;
    const trackY = calculateWaveValue(trackX);
    const trackCanvasY = canvas.height / 2 - trackY;

    ctx.beginPath();
    ctx.arc(trackX, trackCanvasY, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "#e64c4c";
    ctx.fill();

    time += speed * frequency;

    requestAnimationFrame(drawWave);
}

drawWave();
