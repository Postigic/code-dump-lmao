import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
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