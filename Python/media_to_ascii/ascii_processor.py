import cv2
import numpy as np
from PIL import ImageFont
from fontTools.ttLib import TTFont

ASCII_CHARS = r"@@@@@@@@%%##88WWMMBBOOZZ00QQLLCCJJUUYYXXzcvunxrjft/\|(){}[]?-_+~<>i!lI;:,\"^`'."
# UNICODE_CHARS = "齉驫龘✺鬱畫♞☯嘉ꙮ❂⚛✤✹௵目✣♣回⣿☣☸❖田⍟⎈ⵣ☘⡷⠿⌬王⊕◉⠟ᚠ中⊛◎⁙ᛟꘜ※⠋⁂人二丁⸫ᛃ∴∵⋮⠁一⛬丶‧˙·"

CHARS = ASCII_CHARS

# for ASCII
FONT_PATH = r"fonts/consola.ttf"

# for UNICODE
# FONT_PATH = r"fonts/unifont-18.0.01.otf"

FONT = ImageFont.truetype(FONT_PATH, 10) # 10 for ASCII, 16 or 32 for UNICODE
FONT_CMAP = TTFont(FONT_PATH).getBestCmap()

ascent, descent = FONT.getmetrics()
CHAR_WIDTH = round(FONT.getlength("A"))
CHAR_HEIGHT = ascent + descent
CHAR_RATIO = CHAR_HEIGHT / CHAR_WIDTH

def build_glyph_cache(font: ImageFont, ascii_chars: str) -> tuple:
    unique_chars = list(dict.fromkeys(ascii_chars))
    char_to_idx = {c: i for i, c in enumerate(unique_chars)}

    masks = np.zeros((len(unique_chars), CHAR_HEIGHT, CHAR_WIDTH), dtype=np.uint8)

    for i, char in enumerate(unique_chars):
        assert ord(char) in FONT_CMAP, f"{char!r} (U+{ord(char):04X}) isn't in the font"

        mask = font.getmask(char, mode="L")
        arr = np.array(mask, dtype=np.uint8).reshape(mask.size[1], mask.size[0])
        assert arr.any() or char == " ", f"{char!r} rendered blank"
        left, top, _, _ = font.getbbox(char)
        assert top >= 0 and left >= 0, f"{char!r} sticks out above or left of the cell"
        y, x = top, left

        h, w = arr.shape
        if w > CHAR_WIDTH or h > CHAR_HEIGHT:
            scale = min(CHAR_WIDTH / w, CHAR_HEIGHT / h)
            new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
            arr = cv2.resize(arr, (new_w, new_h), interpolation=cv2.INTER_AREA)
            y = min(max(0, top + (h - new_h) // 2), CHAR_HEIGHT - new_h)
            x = 0

        norm = np.zeros((CHAR_HEIGHT, CHAR_WIDTH), dtype=np.uint8)

        h, w = arr.shape
        assert y + h <= CHAR_HEIGHT and x + w <= CHAR_WIDTH, f"{char!r} doesn't fit"

        norm[y:y + h, x:x + w] = arr
        masks[i] = norm

    char_lookup = np.array([char_to_idx[c] for c in ascii_chars], dtype=np.int32)

    return masks, char_lookup

GLYPH_MASKS, CHAR_LOOKUP = build_glyph_cache(FONT, CHARS)

def rgb_to_lightness(r: np.ndarray, g: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (np.maximum(np.maximum(r, g), b).astype(np.int32) + np.minimum(np.minimum(r, g), b).astype(np.int32)) // 2

def frame_to_ascii_image(frame_tuple: tuple, char_width: int, char_height: int) -> tuple:
    assert (char_width, char_height) == (CHAR_WIDTH, CHAR_HEIGHT), f"cell size {char_width}x{char_height} doesn't match glyphs {CHAR_WIDTH}x{CHAR_HEIGHT}"

    frame_index, frame, width = frame_tuple
    aspect = frame.shape[1] / frame.shape[0]
    height = int(width / aspect / CHAR_RATIO)

    small = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    r = small[:, :, 2].astype(np.uint8)
    g = small[:, :, 1].astype(np.uint8)
    b = small[:, :, 0].astype(np.uint8)

    lightness = rgb_to_lightness(r, g, b)
    ascii_idx = ((255 - lightness) * (len(CHARS) - 1) // 255).astype(np.int32)
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

# uniq = list(dict.fromkeys(CHARS))
# masks, _ = build_glyph_cache(FONT, CHARS)
# print("".join(sorted(uniq, key=lambda c: -(masks[uniq.index(c)] > 0).mean())))
