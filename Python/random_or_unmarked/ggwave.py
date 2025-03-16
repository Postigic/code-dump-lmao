import numpy as np
import sounddevice as sd

sample_rate = 44100
duration = 0.05
min_freq = 250
freq_step = 50

text = "skibidi~ skibidi~ hawk tuah hawk! skibidi king who gives out blumpkins! edging and gooning and learning to munt~ dripping cheese all over my lunch! skibidi~ skibidi~ hawk tuah hawk! skibidi boom or skibidi doom! edging and gooning in ohio square! stinky backshot air! on my grind time drink a prime time! to mog the ohio away! balkan rage time! lower tape fade time! we go rizzing in the sigma's way! griddy on sigma horse! stretch out your meat! griddy around the opps! knee surgery's tomorrow and i feel skibidi! like a skibidi gyatt!"

def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return tone

audio = np.array([], dtype=np.float32)
for char in text:
    freq = min_freq + (ord(char) % 20) * freq_step
    print(f"Char '{char}' -> Frequency {freq} Hz")
    tone = generate_sine_wave(freq, duration, sample_rate)
    audio = np.concatenate((audio, tone))

audio = audio * (0.5 / np.max(np.abs(audio)))

print("▶️ Playing GGWave-like sound...")
sd.play(audio, samplerate=sample_rate)
sd.wait()
print("✅ Done!")
