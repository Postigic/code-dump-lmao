import pygame
import time
import sys
from core import Core
from graphics import draw_scanlines, draw_terminal_ui, boot_sequence
from utilities import *
from logger import log_event


def main():
    global log_messages
    clock = pygame.time.Clock()
    core = Core()
    input_text = ""

    boot_sequence() # note: COMMENT WHEN DEBUGGING RAAAHHHH I HATE MY LIFE!!!!!!!

    update_interval = 1000
    last_update_time = pygame.time.get_ticks()

    # beep_sound = pygame.mixer.Sound("beep.wav")
    running = True
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
                if event.key == pygame.K_RETURN:
                    input_text = input_text.lower()

                    if input_text == "inc_cooling":
                        log_event("LOGS : Cooling level increased by 10%")
                        core.cooling_level = min(100, core.cooling_level + 10)
                    elif input_text == "dec_cooling":
                        log_event("LOGS : Cooling level decreased by 10%")
                        core.cooling_level = max(0, core.cooling_level - 10)
                    elif input_text == "inc_energy":
                        log_event("LOGS : Energy output increased by 10%")
                        core.energy_output = min(100, core.energy_output + 10)
                    elif input_text == "dec_energy":
                        log_event("LOGS : Energy output decreased by 10%")
                        core.energy_output = max(0, core.energy_output - 10)
                    elif input_text == "exit":
                        running = False
                    else:
                        log_event("ERROR : The term entered is not recognized as a valid command.", RED)
                    core.update_core()
                    time.sleep(0.5)
                    input_text = ""
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
