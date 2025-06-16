const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSound(frequency = 440, duration = 1, volume = 0.05) {
    const osc = audioCtx.createOscillator();
    const envelope = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc.connect(filter);
    filter.connect(envelope);
    envelope.connect(audioCtx.destination);

    osc.type = settings.oscType;
    osc.frequency.value = frequency;

    filter.type = "lowpass";
    filter.frequency.value = 2000;

    const now = audioCtx.currentTime;
    envelope.gain.setValueAtTime(0, now);
    envelope.gain.linearRampToValueAtTime(volume, now + 0.01);
    envelope.gain.exponentialRampToValueAtTime(0.001, now + duration);

    osc.frequency.setValueAtTime(frequency, audioCtx.currentTime);

    osc.start();
    osc.stop(now + duration);
}
