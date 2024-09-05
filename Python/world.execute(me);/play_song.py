import pygame
import time
import syllapy
from song_transcript import *
from utils import style


def calculate_print_speed(text, duration):
    total_syllables = sum(syllapy.count(word) for word in text.split())
    if total_syllables <= 1:
        return 0.03

    return duration / (total_syllables * 10)


def slow_print(text, speed, colour):
    for character in text:
        print(colour + character + style.RESET, end="", flush=True)
        time.sleep(speed)


def print_lyrics(audio_file, styles):
    lyrics_to_print = []
    for index, lyric in enumerate(transcript):
        print_speed = calculate_print_speed(lyric["text"], lyric["duration"])
        lyrics_to_print.append(
            (lyric["start"], lyric["text"], styles[index], print_speed))

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    total_duration = (pygame.mixer.Sound(audio_file)).get_length()
    pygame.mixer.music.play()

    current_lyric_index = 0
    running = True

    while running:
        current_lyric = transcript[current_lyric_index]
        start_time = current_lyric["start"]
        current_time = pygame.mixer.music.get_pos() / 1000

        if current_time >= start_time:
            start_time, text, current_style, print_speed = lyrics_to_print[current_lyric_index]
            slow_print(f"\n{text}", print_speed, current_style)
            current_lyric_index += 1
        handle_visuals(current_time)

        if current_lyric_index >= len(transcript):
            time.sleep((total_duration + 1) - current_time)
            running = False

    pygame.quit()


def handle_visuals(current_time):
    if print_statements and print_statements[0][1] <= current_time:
        message = print_statements.popleft()[0]
        print(f"\n{message}", end="", flush=True)

    if functions_to_execute and functions_to_execute[0][1] <= current_time:
        func, _ = functions_to_execute.popleft()
        func()


if __name__ == '__main__':
    audio_file = r"D:\vs code projects\world.execute(me);\world-execute-me.mp3"
    styles = [style.RED] * len(transcript)

    for index, colour in indices_styles.items():
        styles[index] = colour

    print_lyrics(audio_file, styles)
