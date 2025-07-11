import pygame
import time
import difflib
import random
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript
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

def is_similar(a: str, b: str, threshold: float = 0.9) -> bool:
    return difflib.SequenceMatcher(None, a.strip().lower(), b.strip().lower()).ratio() >= threshold

def clean_transcript(lyrics: list) -> list:
    if not lyrics:
        return []

    for line in lyrics:
        line.text = re.sub(r"[\u200B-\u200D\uFEFF]", "", line.text).strip()

    lyrics = [line for line in lyrics if line.text]

    if not lyrics:
        return []
    # countercountermeasure

    cleaned = []
    group = [lyrics[0]]

    for line in lyrics[1:]:
        if is_similar(line.text, group[-1].text):
            group.append(line)
        else:
            longest_line = max(group, key=lambda x: len(x.text))
            longest_line.start = group[0].start
            cleaned.append(longest_line)
            group = [line]

    if group:
        longest_line = max(group, key=lambda x: len(x.text))
        longest_line.start = group[0].start
        cleaned.append(longest_line)

    return cleaned

def get_transcript(video_id: str) -> FetchedTranscript:
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

def print_lyrics(audio_file: str, transcript: FetchedTranscript, colours: dict, use_colours: bool = True, volume: float = 0.65) -> None:
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    total_duration = pygame.mixer.Sound(audio_file).get_length()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)

    lyrics = clean_transcript(transcript.fetch())
    current_lyric_index = 0
    colour_values = list(colours.values())
    colour = random.choice(colour_values) if use_colours else ""
    interval = random.randint(5, 7)
    next_change = interval

    while current_lyric_index < len(lyrics):
        current_time = pygame.mixer.music.get_pos() / 1000
        current_lyric = lyrics[current_lyric_index]

        if current_time >= current_lyric.start:
            if use_colours and current_lyric_index == next_change:
                new_colour = colour
                while new_colour == colour:
                    new_colour = random.choice(colour_values)
                colour = new_colour
                interval = random.randint(5, 7)
                next_change += interval

            print_speed = calculate_print_speed(
                current_lyric.text, current_lyric.duration)
            slow_print(f"\n{current_lyric.text}", print_speed, colour)
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
            save = input("\nSave these settings for future? (Y/N): ").upper()
            if save == "Y":
                save_settings(video_id, coloured_text, volume, settings_path)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
