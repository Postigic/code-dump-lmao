import cv2
import numpy as np
from PIL import ImageFont

ASCII_CHARS = r"@@@@@@@@%%##88WWMMBBOOZZ00QQLLCCJJUUYYXXzcvunxrjft/\|(){}[]?-_+~<>i!lI;:,\"^`'."

FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 10)
CHAR_WIDTH, CHAR_HEIGHT = FONT.getmask("A").size
CHAR_RATIO = CHAR_HEIGHT / CHAR_WIDTH

def build_glyph_cache(font, ascii_chars):
    unique_chars = list(dict.fromkeys(ascii_chars))
    char_to_idx = {c: i for i, c in enumerate(unique_chars)}

    masks = np.zeros((len(unique_chars), CHAR_HEIGHT, CHAR_WIDTH), dtype=np.uint8)
    for i, char in enumerate(unique_chars):
        mask = font.getmask(char, mode="L")
        arr = np.array(mask, dtype=np.uint8).reshape(mask.size[1], mask.size[0])

        norm = np.zeros((CHAR_HEIGHT, CHAR_WIDTH), dtype=np.uint8)

        h = min(arr.shape[0], CHAR_HEIGHT)
        w = min(arr.shape[1], CHAR_WIDTH)
        
        norm[:h, :w] = arr[:h, :w]
        masks[i] = norm

    char_lookup = np.array([char_to_idx[c] for c in ascii_chars], dtype=np.int32)

    return masks, char_lookup

GLYPH_MASKS, CHAR_LOOKUP = build_glyph_cache(FONT, ASCII_CHARS)

def rgb_to_lightness(r, g, b):
    return (np.maximum(np.maximum(r, g), b).astype(np.int32) + np.minimum(np.minimum(r, g), b).astype(np.int32)) // 2

def frame_to_ascii_image(frame_tuple, char_width, char_height):
    frame_index, frame, width = frame_tuple
    aspect = frame.shape[1] / frame.shape[0]
    height = int(width / aspect * CHAR_RATIO)

    small = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    r = small[:, :, 2].astype(np.uint8)
    g = small[:, :, 1].astype(np.uint8)
    b = small[:, :, 0].astype(np.uint8)

    lightness = rgb_to_lightness(r, g, b)
    ascii_idx = ((255 - lightness) * (len(ASCII_CHARS) - 1) // 255).astype(np.int32)
    glyph_idx = CHAR_LOOKUP[ascii_idx]

    out_h = height * char_height
    out_w = width * char_width
    canvas = np.zeros((out_h, out_w, 3), dtype=np.uint8)

    selected = GLYPH_MASKS[glyph_idx]

    tiled_mask = (selected.transpose(0, 2, 1, 3).reshape(out_h, out_w))

    def tile_channel(ch):
        return (ch[:, :, np.newaxis, np.newaxis] * np.ones((1, 1, char_height, char_width), dtype=np.uint8))

    r_tiled = tile_channel(r).transpose(0, 2, 1, 3).reshape(out_h, out_w)
    g_tiled = tile_channel(g).transpose(0, 2, 1, 3).reshape(out_h, out_w)
    b_tiled = tile_channel(b).transpose(0, 2, 1, 3).reshape(out_h, out_w)

    mask_bool = tiled_mask > 0
    canvas[mask_bool, 0] = r_tiled[mask_bool]
    canvas[mask_bool, 1] = g_tiled[mask_bool]
    canvas[mask_bool, 2] = b_tiled[mask_bool]

    return frame_index, canvas
