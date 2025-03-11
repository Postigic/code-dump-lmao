import pygame
import time
import random
from youtube_transcript_api import YouTubeTranscriptApi, Transcript
from song_downloader import download_song_as_mp3
from settings_manager import *
from input_validation import *
from utils import STYLE
from pathlib import Path


def calculate_print_speed(text: str, duration: float) -> float:
    total_length = len(text)
    speed = duration / (total_length * 5)

    if "," in text:
        speed *= 1.2
    if "." in text or "!" in text or "?" in text:
        speed *= 1.5

    return max(0.01, speed)


def slow_print(text: str, speed: float, colour: str=""):
    for character in text:
        print(colour + character + STYLE["RESET"], end="", flush=True)
        time.sleep(speed)


def get_transcript(video_id: str) -> Transcript:
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        try:
            transcript = transcript_list.find_manually_created_transcript(
                ["en-US", "en-GB", "en-AU", "en"])
            return transcript
        except Exception:
            transcript = transcript_list.find_generated_transcript(
                ["en-US", "en-GB", "en-AU", "en"])
            print(f"⚠️ Using {transcript.language_code} transcript (auto-generated)")
            return transcript
    except Exception as e:
        print(f"❌ No transcript available: {e}")
        return None


def print_lyrics(audio_file: str, transcript: Transcript, colours: dict, use_colours: bool=True, volume: float=0.65) -> None:
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


def main() -> None:
    try:
        current_dir = Path(__file__).parent
        output_path = current_dir / "mp3_files"
        settings_path = current_dir / "settings.json"

        settings = load_settings(settings_path)

        video_id = get_video_id(settings["video_id"])
        coloured_text = get_coloured_text_preference(settings["coloured_text"])
        volume = get_volume(settings["volume"])

        audio_file_path = download_song_as_mp3(video_id, output_path)
        song_transcript = get_transcript(video_id)
        colour_attributes = {k: v for k, v in STYLE.items() if k != "RESET"}

        if song_transcript:
            print_lyrics(audio_file_path, song_transcript,
                        colour_attributes, coloured_text, volume)

        if settings["video_id"] != video_id:
            save_settings(video_id, settings["coloured_text"], settings["volume"], settings_path)

        settings_changed = ((settings['coloured_text'] != coloured_text) or (settings['volume'] != volume))

        if settings_changed:
            save = input("Save these settings for future? (Y/N): ").upper()
            if save == "Y":
                save_settings(video_id, coloured_text, volume, settings_path)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
