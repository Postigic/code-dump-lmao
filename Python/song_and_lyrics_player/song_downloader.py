from yt_dlp import YoutubeDL
import os


def download_song_as_mp3(video_id, output_path=''):
    url = f"https://www.youtube.com/watch?v={video_id}"
    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info).replace(
            ".webm", ".mp3").replace(".m4a", ".mp3")
        print(f"Downloaded and converted to: {file_path}")
        return file_path
