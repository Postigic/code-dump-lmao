import pygame
from difflib import get_close_matches
from pathlib import Path
from core import QTEC, HFR
from graphics import draw_scanlines, draw_terminal_ui, boot_sequence
from utilities import *
from logger import *

current_dir = Path(__file__).parent
pygame.mixer.set_num_channels(16)


def input_events_manager(event, input_text, excluded_keys, last_pressed_keys, core):
    current_time = pygame.time.get_ticks()
    if event.type == pygame.QUIT:
        return False, input_text
    elif event.type == pygame.KEYDOWN:
        if event.key in excluded_keys:
            if event.key not in last_pressed_keys or current_time - last_pressed_keys[event.key] > 700:
                last_pressed_keys[event.key] = current_time
            else:
                return True, input_text

        if event.key == pygame.K_RETURN:
            input_text = process_input(core, input_text)
        elif event.key == pygame.K_TAB:
            input_text = handle_tab_completion(core, input_text)
        elif event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        else:
            input_text += event.unicode
    return True, input_text


def process_input(core, input_text):
    input_text = input_text.lower()
    parts = input_text.split()
    command = parts[0] if len(parts) > 0 else None
    arg = parse_argument(parts)

    
    execute_command(core, command, arg)

    return ""

def parse_argument(parts):
    if len(parts) > 1:
        if parts[1].isdigit():
            return int(parts[1])
        elif parts[1].replace(".", "", 1).isdigit():
            return float(parts[1])
        else:
            return parts[1]
    return None


def execute_command(core, command, arg):
    commands = core.commands
    if command in commands:
        try:
            command_info = commands[command]
            message, color = command_info["handler"](arg)
            log_event(message, color)
        except TypeError as e:
            log_event(f"[ERROR] {str(e)}", RED)
        except Exception as e:
            log_event(f"[ERROR] Unexpected error: {str(e)}", RED)
    else:
        log_event("[ERROR] Command not recognized.", RED)


def handle_tab_completion(core, input_text):
    closest_matches = get_close_matches(input_text, core.commands.keys(), n=1)
    if closest_matches:
        return closest_matches[0]
    return input_text


def sound_manager(sound):
    if sound == "comp_amb":
        comp_amb_sound = pygame.mixer.Sound(current_dir / r"sfx\comp_amb.ogg")
        comp_amb_sound.play(loops=-1)
        comp_amb_sound.set_volume(0.1)
    if sound == "fan_amb":
        fan_amb_sound = pygame.mixer.Sound(current_dir / r"sfx\fans_amb.ogg")
        fan_amb_sound.play(loops=-1)
        fan_amb_sound.set_volume(0.2)


def main():
    clock = pygame.time.Clock()
    core = HFR()
    input_text = ""
    last_update_time = pygame.time.get_ticks()
    excluded_keys = {pygame.K_RETURN, pygame.K_TAB}
    last_pressed_keys = {}
    running = True

    pygame.key.set_repeat(500, 50)

    # boot_sequence()  # note: COMMENT WHEN DEBUGGING RAAAHHHH I HATE MY LIFE!!!!!!!

    sound_manager("comp_amb")
    sound_manager("fan_amb")

    while running:
        screen.fill(BLACK)
        draw_scanlines()

        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= 1000:
            core.update_core()
            last_update_time = current_time

        for event in pygame.event.get():
            running, input_text = input_events_manager(event, input_text, excluded_keys, last_pressed_keys, core)
            if not running:
                break

        draw_terminal_ui(core, input_text)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
