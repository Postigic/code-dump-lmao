import pygame
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi
from song_downloader import download_song_as_mp3
from pathlib import Path


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
    total_length = len(text)
    if total_length <= 1:
        return 0.03
    return duration / (total_length * 5)


def slow_print(text, speed, colour=""):
    for character in text:
        print(colour + character + style["RESET"], end="", flush=True)
        time.sleep(speed)


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_manually_created_transcript(
        ["en-US", "en-GB", "en-AU", "en"])

    return transcript


def print_lyrics(audio_file, transcript, colours, volume=0.65, use_colours=True):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    total_duration = pygame.mixer.Sound(audio_file).get_length()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)

    lyrics = transcript.fetch()
    current_lyric_index = 0

    while current_lyric_index < len(lyrics):
        current_time = pygame.mixer.music.get_pos() / 1000
        current_lyric = lyrics[current_lyric_index]

        if current_time >= current_lyric["start"]:
            colour = random.choice(list(
                colours.values())) if use_colours and current_lyric_index % 3 == 0 else colour
            print_speed = calculate_print_speed(
                current_lyric["text"], current_lyric["duration"])
            slow_print(f"\n{current_lyric['text']}", print_speed, colour)
            current_lyric_index += 1

    time.sleep(max(0, total_duration - current_time))


if __name__ == '__main__':
    current_dir = Path(__file__).parent
    output_path = current_dir / "mp3_files"

    video_id = "uFRPeiAEO0M"

    colour_attributes = {k: v for k, v in style.items() if k != 'RESET'}

    audio_file_path = download_song_as_mp3(video_id, output_path)
    song_transcript = get_transcript(video_id)
    print_lyrics(audio_file_path, song_transcript, colour_attributes)

    pygame.quit()
