import numpy as np
import pygame.mixer as mixer

SAMPLE_RATE = 44100
MAX_CHANNELS = 64
SUSTAIN = 0.12
VOLUME = 0.08

mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=512)
mixer.set_num_channels(MAX_CHANNELS)

def _freq(val, n):
    lo, hi = np.log2(150), np.log2(800)
    return 2 ** (lo + (hi - lo) * (val / n))

def _envelope(length):
    x = np.linspace(0, 1, length)
    attack, decay, sustain, release = 0.025, 0.1, 0.9, 0.3

    # i don't know what this means okay? don't ask me 🤫
    return np.piecewise(x, 
        [
            x < attack,
            (x >= attack) & (x < attack + decay),
            (x >= attack + decay) & (x < 1.0 - release),
            x >= 1.0 - release
        ], 
        [
            lambda x: x / attack,
            lambda x: 1.0 - (x - attack) / decay * (1.0 - sustain),
            sustain,
            lambda x: sustain / release * (1.0 - x)
        ]
    )

def _loudness_comp(freq):
    ref = 400
    return (ref / freq) ** 0.5

def _make_note(freq, speed):
    duration = max(0.03, SUSTAIN / speed)
    length = int(SAMPLE_RATE * duration)

    t = np.linspace(0, duration, length, False)
    phase = (freq * t) % 1.0
    wave = np.where(phase < 0.5, 4 * phase - 1, 3 - 4 * phase)

    return (wave * _envelope(length) * VOLUME * _loudness_comp(freq) * 32767).astype(np.int16)

def play_tone(freq, speed, muted):
    if muted:
        return
    
    mixer.find_channel(force=True).play(mixer.Sound(_make_note(freq, speed)))

def play_value(val, n, speed, muted):
    play_tone(_freq(val, n), speed, muted)
