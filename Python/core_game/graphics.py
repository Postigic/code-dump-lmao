import pygame
import time
from utilities import *


def boot_sequence():
    boot_messages = [
        "Initializing system components...",
        "Loading core modules...",
        "Verifying system integrity...",
        "Connecting to peripherals...",
        "Starting command-line interface...",
        "System Ready. Welcome!"
    ]

    screen.fill(BLACK)
    draw_scanlines()
    y_offset = 20
    char_width = FONT.size(" ")[0]

    for message in boot_messages:
        current_frame = 0
        while current_frame <= len(message):
            screen.fill(BLACK)
            draw_scanlines()

            for i, msg in enumerate(boot_messages[:boot_messages.index(message)]):
                draw_text(screen, msg, 20, 20 + i * 30, GREEN)

            animate_log_event(message, 20, y_offset, current_frame, char_width, CYAN)
            current_frame += 1
            draw_cursor(20 + char_width * current_frame, y_offset)

            pygame.display.flip()
            time.sleep(0.01)

        y_offset += 30
        time.sleep(0.2)


def draw_text(surface, text, x, y, color=WHITE):
    rendered_text = FONT.render(text, True, color)
    surface.blit(rendered_text, (x, y))


def draw_cursor(x, y):
    if pygame.time.get_ticks() // 500 % 2 == 0:
        draw_text(screen, "|", x, y, CYAN)


def draw_scanlines():
    for i in range(0, HEIGHT, 4):
        pygame.draw.line(screen, (20, 20, 20), (0, i), (WIDTH, i))


def animate_log_event(text, x, y, current_frame, char_width, color=WHITE):
    for i in range(min(current_frame, len(text))):
        draw_text(screen, text[i], x + i * char_width, y, color)


def draw_terminal_ui(core, input_text, y_offset):
    status = core.get_status()
    for line in status:
        color = GREEN if "stable" in line else (RED if "WARNING" in line else CYAN)
        draw_text(screen, line, 10, y_offset, color)
        y_offset += 30

    draw_text(screen, "Commands:", 10, y_offset + 30, YELLOW)
    y_offset += 60
    draw_text(screen, "  inc_cooling -- Increase cooling", 10, y_offset)
    draw_text(screen, "  dec_cooling -- Decrease cooling", 10, y_offset + 30)
    draw_text(screen, "  inc_energy  -- Increase energy output", 10, y_offset + 60)
    draw_text(screen, "  dec_energy  -- Decrease energy output", 10, y_offset + 90)
    draw_text(screen, "  exit        -- Exit the control interface", 10, y_offset + 120)

    pygame.draw.rect(screen, GREY, (10, HEIGHT - 70, WIDTH - 20, 40), border_radius=5)
    draw_text(screen, f"> {input_text}", 20, HEIGHT - 61, CYAN)
    draw_cursor(20 + FONT.size(f"> {input_text}")[0], HEIGHT - 62)

    pygame.draw.rect(screen, GREY, (10, HEIGHT - 400, WIDTH - 20, 320), border_radius=5)
    y_offset = HEIGHT - 400
    from logger import log_messages
    for log in log_messages:
        animate_log_event(log["message"], 20, y_offset + 10, log["current_frame"], FONT.size(" ")[0], log["color"])
        log["current_frame"] = min(log["current_frame"] + 2, len(log["message"]))
        y_offset += 30