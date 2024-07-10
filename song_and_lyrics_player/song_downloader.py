from pytube import YouTube
from pydub import AudioSegment
import os


def download_song_as_mp3(video_id, output_path=''):
    url = f"https://www.youtube.com/watch?v={video_id}"

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    if os.path.exists(new_file):
        print(f"File already exists: {new_file}")
        os.remove(out_file)
        return new_file

    audio = AudioSegment.from_file(out_file)
    audio.export(new_file, format='mp3')

    os.remove(out_file)

    print(f"Downloaded and converted to: {new_file}")
    return new_file
