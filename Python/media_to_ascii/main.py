import os
import cv2
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from ascii_processor import frame_to_ascii_image, CHAR_WIDTH, CHAR_HEIGHT

def process_frame(frame_tuple):
    return frame_to_ascii_image(frame_tuple, CHAR_WIDTH, CHAR_HEIGHT)

def compress_video(input_path, output_path, crf=23):
    subprocess.run([
        "ffmpeg", "-y", 
        "-i", str(input_path),
        "-vcodec", "libx264", 
        "-crf", str(crf),
        "-preset", "fast", 
        str(output_path)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"⬇️ Saved compressed ASCII video to: {output_path}")

def merge_audio(original_video, ascii_video, output_path):
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
    print(f"🎧 Added audio back to: {output_path}")

def video_to_ascii(video_path, output_path, width=120, max_workers=None, batch_size=100):
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"❌ Failed to open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    first_frame = True
    writer = None

    # i am aware that this is awful, i just don't care yet
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        frame_index = 0
        batch = []

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            batch.append((frame_index, frame, width))
            frame_index += 1

            if first_frame and batch:
                h, w, _ = frame_to_ascii_image(batch[0], CHAR_WIDTH, CHAR_HEIGHT)[1].shape
                writer = cv2.VideoWriter(str(output_path), cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                first_frame = False

            if len(batch) == batch_size:
                batch_results = list(executor.map(process_frame, batch, chunksize=30))
                batch_results.sort(key=lambda x: x[0])

                for _, ascii_frame in batch_results:
                    writer.write(cv2.cvtColor(ascii_frame, cv2.COLOR_RGB2BGR))

                print(f"Processed {frame_index}/{total_frames} frames ({frame_index / total_frames * 100:.2f}%)")
                batch = []

        if batch:
            batch_results = list(executor.map(process_frame, batch, chunksize=30))
            batch_results.sort(key=lambda x: x[0])

            for _, ascii_frame in batch_results:
                writer.write(cv2.cvtColor(ascii_frame, cv2.COLOR_RGB2BGR))

            print(f"Processed {frame_index}/{total_frames} frames (100.00%)")

    cap.release()
    writer.release()
    print(f"💾 Saved raw ASCII video to: {output_path}")

    compressed_path = output_path.parent / f"{output_path.stem}_compressed.mp4"
    compress_video(output_path, compressed_path)

    final_path = output_path.parent / f"{output_path.stem}_final.mp4"
    merge_audio(video_path, compressed_path, final_path)

    print(f"✅ Saved final ASCII video to: {final_path}")

def image_to_ascii(image_path, output_path, width=120):
    image = cv2.imread(str(image_path))
    
    if image is None:
        raise ValueError(f"❌ Failed to load image: {image_path}")

    _, ascii_image = frame_to_ascii_image((0, image, width), CHAR_WIDTH, CHAR_HEIGHT)
    cv2.imwrite(str(output_path), cv2.cvtColor(ascii_image, cv2.COLOR_RGB2BGR))
    print(f"✅ Saved ASCII image to: {output_path}")

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    output_dir = current_dir / "output"
    output_dir.mkdir(exist_ok=True)

    file_path = None
    for ext in ["*.mp4", "*.mov", "*.jpg", "*.png"]:
        file_path = next(current_dir.glob(ext), None)
        if file_path:
            break

    if file_path is None:
        raise FileNotFoundError("No video file found in the directory.")

    if file_path.suffix.lower() in [".mp4", ".mov"]:
        output_path = output_dir / f"{file_path.stem}_ascii.mp4"
        video_to_ascii(file_path, output_path, width=120, max_workers=os.cpu_count(), batch_size=2000)
    else:
        output_path = output_dir / f"{file_path.stem}_ascii.png"
        image_to_ascii(file_path, output_path, width=120)
