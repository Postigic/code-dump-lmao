import cv2
import time


def frame_to_ascii(frame, width=84):

    aspect_ratio = frame.shape[1] / frame.shape[0]
    height = int(width / aspect_ratio / 2)
    resized_frame = cv2.resize(frame, (width, height))

    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    ascii_chars = "@%#*+=-:. "

    ascii_frame = ""
    for row in gray_frame:
        for pixel in row:
            ascii_frame += ascii_chars[int(pixel /
                                           255 * (len(ascii_chars) - 1))]
        ascii_frame += '\n'

    return ascii_frame


def video_to_ascii(video_path, width=84):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)

    while cap.isOpened():
        start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        ascii_frame = frame_to_ascii(frame, width)

        print(ascii_frame)

        elapsed_time = time.time() - start_time
        remaining_time = max(0, (delay / 1000) - elapsed_time)
        time.sleep(remaining_time)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = r"D:\vs code projects\rabbit_hole_ascii\rabbit_hole.mp4"
    video_to_ascii(video_path)
