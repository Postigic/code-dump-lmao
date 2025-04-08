from yt_dlp import YoutubeDL
import os
from utils import STYLE


def download_song_as_mp3(video_id, output_path=""):
    url = f"https://www.youtube.com/watch?v={video_id}"

    with YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info["title"]
        mp3_filename = os.path.join(output_path, f"{title}.mp3")

    if os.path.exists(mp3_filename):
        print(STYLE["CYAN"] + f"⏩ Skipping download, file already exists: {mp3_filename}" + STYLE["RESET"]) # brah this don't work yo
        return mp3_filename

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
        print(STYLE["GREEN"] + f"✅ Downloaded and converted to: {file_path}" + STYLE["RESET"])
        return file_path
