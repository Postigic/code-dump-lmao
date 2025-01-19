import pygame

pygame.init()

display_info = pygame.display.Info()
WIDTH, HEIGHT = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Core Game")

FONT = pygame.font.Font(pygame.font.match_font("Consolas"), 24)
RED = (255, 97, 136)
ORANGE = (252, 152, 103)
YELLOW = (255, 216, 102)
GREEN = (169, 220, 118)
CYAN = (120, 220, 232)
PURPLE = (171, 157, 242)
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GREY = (40, 40, 40)


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))