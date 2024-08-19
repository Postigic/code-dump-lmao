import pygame
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi
from song_downloader import download_song_as_mp3
from settings_manager import *
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
    speed = duration / (total_length * 5)

    if "," in text:
        speed *= 1.2
    if "." in text or "!" in text or "?" in text:
        speed *= 1.5

    return max(0.01, speed)


def slow_print(text, speed, colour=""):
    for character in text:
        print(colour + character + style["RESET"], end="", flush=True)
        time.sleep(speed)


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    try:
        transcript = transcript_list.find_manually_created_transcript(
            ["en-US", "en-GB", "en-AU", "en"])
        return transcript
    except Exception:
        transcript = transcript_list.find_generated_transcript(
            ["en-US", "en-GB", "en-AU", "en"])
        return transcript


def print_lyrics(audio_file, transcript, colours, use_colours=True, volume=0.65):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    total_duration = pygame.mixer.Sound(audio_file).get_length()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)

    lyrics = transcript.fetch()
    current_lyric_index = 0
    colour = ""

    while current_lyric_index < len(lyrics):
        current_time = pygame.mixer.music.get_pos() / 1000
        current_lyric = lyrics[current_lyric_index]

        if current_time >= current_lyric["start"]:
            colour = random.choice(list(
                colours.values())) if use_colours and current_lyric_index % random.randint(1, 5) == 0 else colour
            print_speed = calculate_print_speed(
                current_lyric["text"], current_lyric["duration"])
            slow_print(f"\n{current_lyric['text']}", print_speed, colour)
            current_lyric_index += 1

    time.sleep(max(0, total_duration - current_time))


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    output_path = current_dir / "mp3_files"
    settings_path = current_dir / "settings.json"

    settings = load_settings(settings_path)

    video_id_input = input(
        f"Enter the YouTube video ID [previous: {settings['video_id']}]: ")
    video_id = video_id_input if video_id_input else settings["video_id"]

    coloured_text_input = input(
        f"Use coloured text? (Y/N) [default: {settings['coloured_text']}]: ")
    coloured_text = coloured_text_input.upper(
    ) == 'Y' if coloured_text_input else settings["coloured_text"]

    volume_input = input(
        f"Volume (0.0 to 1.0) [default: {settings['volume']}]: ")
    volume = float(volume_input) if volume_input else settings["volume"]

    colour_attributes = {k: v for k, v in style.items() if k != "RESET"}

    audio_file_path = download_song_as_mp3(video_id, output_path)
    song_transcript = get_transcript(video_id)

    if song_transcript:
        print_lyrics(audio_file_path, song_transcript,
                     colour_attributes, coloured_text, volume)

    if settings["video_id"] != video_id:
        save_settings(video_id, coloured_text, volume, settings_path)

    if settings["coloured_text"] != coloured_text or settings["volume"] != volume:
        save_settings_input = input(
            f"\n\nDo you want to save the current settings? (Y/N) [Use coloured text: {coloured_text}, Volume: {volume}]: ")
        if save_settings_input.upper() == "Y":
            save_settings(video_id, coloured_text, volume, settings_path)

    pygame.quit()
