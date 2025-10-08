import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ASCII_CHARS = r"@@@@@@@@%%##88WWMMBBOOZZ00QQLLCCJJUUYYXXzcvunxrjft/\|(){}[]?-_+~<>i!lI;:,\"^`'."

FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 10)
CHAR_WIDTH, CHAR_HEIGHT = FONT.getmask("A").size
CHAR_RATIO = CHAR_HEIGHT / CHAR_WIDTH

def rgb_to_lightness(r_channel, g_channel, b_channel):
    max_c = np.maximum(np.maximum(r_channel, g_channel), b_channel)
    min_c = np.minimum(np.minimum(r_channel, g_channel), b_channel)
    return (max_c + min_c) / 2

def frame_to_ascii_image(frame_tuple, char_width, char_height):
    frame_index, frame, width = frame_tuple
    aspect = frame.shape[1] / frame.shape[0]
    height = int(width / aspect * CHAR_RATIO)

    small_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    r_channel = small_frame[:, :, 2]
    g_channel = small_frame[:, :, 1]
    b_channel = small_frame[:, :, 0]

    lightness = rgb_to_lightness(r_channel, g_channel, b_channel)
    idx_matrix = (lightness / 255 * (len(ASCII_CHARS) - 1)).astype(np.uint8)

    img = Image.new("RGB", (width * char_width, height * char_height), "black")
    draw = ImageDraw.Draw(img)

    for y in range(height):
        for x in range(width):
            char = ASCII_CHARS[idx_matrix[y, x]]
            color = (
                int(np.clip(round(r_channel[y, x]), 0, 255)),
                int(np.clip(round(g_channel[y, x]), 0, 255)),
                int(np.clip(round(b_channel[y, x]), 0, 255))
            )
            draw.text((x * char_width, y * char_height), char, fill=color, font=FONT)

    return frame_index, np.array(img)
