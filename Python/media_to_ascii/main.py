import math
import os
import cv2
import subprocess
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from ascii_processor import frame_to_ascii_image, CHAR_WIDTH, CHAR_HEIGHT

STYLE = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}

TARGET_CELLS = 35000

# higher = finer, lower = coarser
#
# default is 35000, heuristically derived
#
# optimal widths from default target cells:
# 720x720 optimal -> 138 width
# 720x1280 optimal -> 104 width
# 1920x810 optimal -> 213 width
# 1920x1080 optimal -> 184 width
#
# acceptable enough that i can't be bothered to touch it anymore...
#
# my PC crashed once during this heuristic testing so like that's a bad omen or something lol

def optimal_width(frame_width: int, frame_height: int, target_cells: int=TARGET_CELLS) -> int:
    aspect = (frame_height / frame_width) * (CHAR_HEIGHT / CHAR_WIDTH)
    width = math.sqrt(target_cells / aspect)

    return max(40, min(300, round(width)))

def process_frame(frame_tuple: tuple) -> tuple:
    return frame_to_ascii_image(frame_tuple, CHAR_WIDTH, CHAR_HEIGHT)

def compress_video(input_path: Path, output_path: Path, crf: int=23, fps: int=None) -> None:
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-vcodec", "libx264",
        "-crf", str(crf),
        "-preset", "fast"
    ]

    if fps is not None:
        cmd += ["-vf", f"fps={fps}"]
        
    cmd.append(str(output_path))

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{STYLE['GREEN']}🗜️ Saved compressed ASCII video to: {output_path}{STYLE['RESET']}")

def merge_audio(original_video: Path, ascii_video: Path, output_path: Path) -> None:
    temp_audio = ascii_video.parent / "temp_audio.aac"

    # incantation to extract audio from original video
    subprocess.run([
        "ffmpeg", "-y", 
        "-i", str(original_video),
        "-vn", "-acodec", 
        "copy", str(temp_audio)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # incantation to merge audio with ascii video
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(ascii_video),
        "-i", str(temp_audio),
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        str(output_path)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    temp_audio.unlink(missing_ok=True)
    print(f"{STYLE['GREEN']}🎧 Added audio back to: {output_path}{STYLE['RESET']}")

# handle aspect ratio for width maybe (e.g. landscape 200, portrait 120/150?)
def video_to_ascii(video_path: Path, output_path: Path, width: int=None, max_workers: int=None, batch_size: int=100, skip_compression: bool=False, has_audio: bool=True) -> None:
    start_time = time.time()

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"{STYLE['RED']}❌ Failed to open video: {video_path}{STYLE['RESET']}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if width is None:
        width = optimal_width(frame_width, frame_height)
        orientation = "landscape" if frame_width >= frame_height else "portrait"
        print(f"{STYLE['CYAN']}🎯 Optimal width: {width} (orientation: {orientation} {frame_width}x{frame_height}){STYLE['RESET']}\n")

    first_frame = True
    writer = None
    frame_index = 0
    batch = []

    # i am aware that this is awful, i just don't care yet
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            batch.append((frame_index, frame, width))
            frame_index += 1

            if first_frame and batch:
                h, w, _ = frame_to_ascii_image(batch[0], CHAR_WIDTH, CHAR_HEIGHT)[1].shape
                writer = cv2.VideoWriter(str(output_path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
                first_frame = False

            if len(batch) == batch_size:
                batch_results = list(executor.map(process_frame, batch, chunksize=30))
                batch_results.sort(key=lambda x: x[0])

                for _, ascii_frame in batch_results:
                    writer.write(cv2.cvtColor(ascii_frame, cv2.COLOR_RGB2BGR))

                print(f"{STYLE['YELLOW']}[Progress] {frame_index}/{total_frames} frames ({frame_index / total_frames * 100:.2f}%) {STYLE['RESET']}")
                batch = []

        if batch:
            batch_results = list(executor.map(process_frame, batch, chunksize=30))
            batch_results.sort(key=lambda x: x[0])

            for _, ascii_frame in batch_results:
                writer.write(cv2.cvtColor(ascii_frame, cv2.COLOR_RGB2BGR))

            print(f"{STYLE['YELLOW']}[Progress] {frame_index}/{total_frames} frames ({frame_index / total_frames * 100:.2f}%) {STYLE['RESET']}")

    cap.release()
    writer.release()
    print(f"\n{STYLE['GREEN']}💾 Saved raw ASCII video to: {output_path}{STYLE['RESET']}")

    if not skip_compression:
        compressed_path = output_path.parent / f"{output_path.stem}_compressed.mp4"
        print(f"\n{STYLE['MAGENTA']}🗜️ Compressing video...{STYLE['RESET']}")
        compress_video(output_path, compressed_path, fps=fps)

    if has_audio: # i'm too lazy lol
        final_path = output_path.parent / f"{output_path.stem}_final.mp4"
        print(f"\n{STYLE['MAGENTA']}🎧 Merging audio...{STYLE['RESET']}")
        merge_audio(video_path, compressed_path, final_path)
        print(f"\n{STYLE['GREEN']}✅ Saved final ASCII video to: {final_path}{STYLE['RESET']}")

    elapsed = time.time() - start_time
    m, s = divmod(elapsed, 60)
    h, m = divmod(m, 60)

    print(f"\n{STYLE['CYAN']}⏱ Total time: {int(h)}h {int(m)}m {s:.2f}s{STYLE['RESET']}")

def image_to_ascii(image_path: Path, output_path: Path, width: int=None) -> None:
    image = cv2.imread(str(image_path))
    
    if image is None:
        raise ValueError(f"{STYLE['RED']}❌ Failed to load image: {image_path}{STYLE['RESET']}")
    
    if width is None:
        h, w = image.shape[:2]
        width = optimal_width(w, h)
        orientation = "landscape" if w >= h else "portrait"
        print(f"{STYLE['CYAN']}🎯 Optimal width: {width} (orientation: {orientation} {w}x{h}){STYLE['RESET']}\n")

    _, ascii_image = frame_to_ascii_image((0, image, width), CHAR_WIDTH, CHAR_HEIGHT)
    cv2.imwrite(str(output_path), cv2.cvtColor(ascii_image, cv2.COLOR_RGB2BGR))
    print(f"{STYLE['GREEN']}✅ Saved ASCII image to: {output_path}{STYLE['RESET']}")

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    output_dir = current_dir / "output"
    output_dir.mkdir(exist_ok=True)

    file_path = None
    for ext in ["*.mp4", "*.mov", "*.jpg", "*.png", "*.gif"]:
        file_path = next(current_dir.glob(ext), None)
        if file_path:
            break

    if file_path is None:
        raise FileNotFoundError(f"{STYLE['RED']}❌ No video file found in the directory.{STYLE['RESET']}")

    print(f"{STYLE['CYAN']}{'-'*40}\n🚀 Starting ASCII conversion: {file_path.name}\n{'-'*40}{STYLE['RESET']}")

    if file_path.suffix.lower() in [".mp4", ".mov"]:
        output_path = output_dir / f"{file_path.stem}_ascii.mp4"
        video_to_ascii(file_path, output_path, max_workers=os.cpu_count(), batch_size=2000)
    elif file_path.suffix.lower() == ".gif":
        # i'm lazy, a gif is just an audio-less mp4 right? should work fine... 
        # this is very patchwork though, may or may not improve in the future or something lol
        temp_mp4 = output_dir / f"{file_path.stem}_temp.mp4"
        final_gif = output_dir / f"{file_path.stem}_ascii.gif"

        subprocess.run([
            "ffmpeg", "-y", 
            "-i", str(file_path), 
            str(temp_mp4)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        ascii_mp4 = output_dir / f"{file_path.stem}_ascii.mp4"
        video_to_ascii(temp_mp4, ascii_mp4, max_workers=os.cpu_count(), batch_size=2000, skip_compression=True, has_audio=False)
        temp_mp4.unlink()

        subprocess.run([
            "ffmpeg", "-y", 
            "-i", str(ascii_mp4), 
            str(final_gif)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        output_path = output_dir / f"{file_path.stem}_ascii.png"
        image_to_ascii(file_path, output_path)

    print(f"{STYLE['GREEN']}{'-'*40}\n✅ Finished processing {file_path.name}\n{'-'*40}{STYLE['RESET']}")
