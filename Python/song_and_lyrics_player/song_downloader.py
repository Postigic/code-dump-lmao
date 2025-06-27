from yt_dlp import YoutubeDL
import os
from utils import STYLE

def download_song_as_mp3(video_id, output_path=""):
    url = f"https://www.youtube.com/watch?v={video_id}"
    options = {
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)
            if not info:
                raise ValueError("Empty video info received.")
            title = info.get("title", f"{video_id}_fallback")
            mp3_filename = os.path.join(output_path, f"{title}.mp3")
    except Exception as e:
        print(STYLE["RED"] + f"❌ Failed to extract video info: {e}" + STYLE["RESET"])
        raise

    if os.path.exists(mp3_filename):
        print(STYLE["CYAN"] + f"⏩ Skipping download, file already exists: {mp3_filename}" + STYLE["RESET"])
        return mp3_filename

    download_options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    try:
        with YoutubeDL(download_options) as ydl:
            info = ydl.extract_info(url, download=True)
            if not info:
                raise ValueError("Download failed or returned no info.")
            file_path = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
            print(STYLE["GREEN"] + f"✅ Downloaded and converted to: {file_path}" + STYLE["RESET"])
            return file_path
    except Exception as e:
        print(STYLE["RED"] + f"❌ Download error: {e}" + STYLE["RESET"])
        raise
