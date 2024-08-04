import pygame
import time
import syllapy
import random
from youtube_transcript_api import YouTubeTranscriptApi
from song_downloader import download_song_as_mp3


style = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}


def calculate_print_speed(text, duration):
    total_syllables = sum(syllapy.count(word) for word in text.split())
    if total_syllables <= 1:
        return 0.03

    return duration / (total_syllables * 10)


def slow_print(text, speed, colour=""):
    for character in text:
        print(colour + character + style["RESET"], end="", flush=True)
        time.sleep(speed)


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_transcript(
        ["en-US", "en-GB", "en-AU", "en"])
    return transcript


def print_lyrics(audio_file, transcript, colours, use_colours):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    total_duration = (pygame.mixer.Sound(audio_file)).get_length()
    pygame.mixer.music.play()

    lyrics = transcript.fetch()
    current_lyric_index = 0
    iteration_counter = 0
    running = True

    while running:
        current_lyric = lyrics[current_lyric_index]
        start_time = current_lyric["start"]
        duration = current_lyric["duration"]
        current_time = pygame.mixer.music.get_pos() / 1000

        if iteration_counter % 3 == 0:
            colour = random.choice(
                list(colours.values())) if use_colours else ""

        if current_time >= start_time:
            print_speed = calculate_print_speed(
                current_lyric["text"], duration)
            slow_print(
                f"\n{current_lyric['text']}", print_speed, colour)
            current_lyric_index += 1
            iteration_counter += 1

        if current_lyric_index >= len(lyrics):
            time.sleep((total_duration + 1) - current_time)
            running = False


if __name__ == '__main__':
    output_path = r"D:\vs code projects\song_and_lyrics_player\mp3_files"
    video_id = "F3cXxqgbx9Y"
    coloured_text = True

    colour_attributes = {k: v for k, v in style.items() if k != 'RESET'}

    audio_file_path = download_song_as_mp3(video_id, output_path)
    song_transcript = get_transcript(video_id)
    print_lyrics(audio_file_path, song_transcript,
                 colour_attributes, coloured_text)

    pygame.quit()
