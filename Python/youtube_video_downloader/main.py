import yt_dlp
from pathlib import Path

def download_youtube_video(url, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    current_dir = Path(__file__).parent

    output_dir = current_dir / "downloads"
    output_dir.mkdir(exist_ok=True)

    url = input("Enter YouTube URL: ").strip()
    download_youtube_video(url, output_dir)
    print("✅ Download complete!")
