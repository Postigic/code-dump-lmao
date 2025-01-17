import pygame
import time
import sys
from difflib import get_close_matches
from core import Core
from graphics import draw_scanlines, draw_terminal_ui, boot_sequence
from utilities import *
from commands import commands
from logger import *


def main():
    clock = pygame.time.Clock()
    core = Core()
    input_text = ""

    # boot_sequence()  # note: COMMENT WHEN DEBUGGING RAAAHHHH I HATE MY LIFE!!!!!!!

    update_interval = 1000
    last_update_time = pygame.time.get_ticks()

    # beep_sound = pygame.mixer.Sound("beep.wav")
    running = True

    pygame.key.set_repeat(500, 50)

    excluded_keys = {pygame.K_RETURN, pygame.K_TAB}
    last_pressed_keys = {}

    while running:
        screen.fill(BLACK)
        draw_scanlines()

        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= update_interval:
            core.update_core()
            last_update_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in excluded_keys:
                    if event.key not in last_pressed_keys or current_time - last_pressed_keys[event.key] > 700:
                        last_pressed_keys[event.key] = current_time
                    else:
                        continue

                if event.key == pygame.K_RETURN:
                    input_text = input_text.lower()

                    parts = input_text.split()
                    command = parts[0] if len(parts) > 0 else None
                    arg = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else float(parts[1]) if len(parts) > 1 and parts[1].replace(".", "", 1).isdigit() else parts[1] if len(parts) > 1 else None  # lmao what

                    if command in commands:
                        if command == "exit":
                            running = False
                        elif command == "clear":
                            clear_logs()
                        else:
                            try:
                                if isinstance(arg, int):
                                    message, color = commands[command]["handler"](core, arg)
                                    log_event(message, color)
                                else:
                                    log_event(f"[ERROR] Expected integer, but got {type(arg).__name__}.", RED)
                            except TypeError:
                                log_event("[ERROR] Invalid argument type.", RED)
                    else:
                        log_event("[ERROR] The term entered is not recognized as a valid command.", RED)
                    core.update_core()
                    time.sleep(0.5)
                    input_text = ""
                elif event.key == pygame.K_TAB:
                    closest_matches = get_close_matches(input_text, commands.keys(), n=1)
                    if closest_matches:
                        input_text = closest_matches[0]
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        draw_terminal_ui(core, input_text, 20)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
