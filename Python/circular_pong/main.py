import pygame
import math
from utils import WIDTH, HEIGHT, CENTER, ARENA_RADIUS
from paddle import Paddle
from ball import Ball

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circular Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
PURPLE = (255, 50, 255)

# paddle_1 = Paddle(angle=math.pi/2, color=RED, keys=(pygame.K_d, pygame.K_a))
paddles = [
    Paddle(angle=math.pi/2, color=RED, is_ai=True),
    Paddle(angle=3*math.pi/2, color=BLUE, is_ai=True),
    # Paddle(angle=3*math.pi/2, color=ORANGE, is_ai=True),
    # Paddle(angle=math.pi, color=YELLOW, is_ai=True),
    # Paddle(angle=0, color=GREEN, is_ai=True),
    # Paddle(angle=math.pi/4, color=PURPLE, is_ai=True),
]

balls = [Ball()]

scores = [0 for _ in paddles]
ball_owners = [paddles[0] for _ in balls]

font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, ball in enumerate(balls):
        ball.update()

        for paddle in paddles:
            paddle.update(ball.pos, ball_owners[i], ball)

        collided = False
        for paddle in paddles:
            if ball.resolve_collision(paddle):
                collided = True
                ball_owners[i] = paddle
                break

        dx = ball.pos[0] - CENTER[0]
        dy = ball.pos[1] - CENTER[1]
        if not collided and math.hypot(dx, dy) + ball.radius >= ARENA_RADIUS:
            owner_index = paddles.index(ball_owners[i])
            for j in range(len(paddles)):
                if j != owner_index:
                    scores[j] += 1
            ball.reset()
            ball_owners[i] = paddles[owner_index]

    WINDOW.fill(BLACK)
    pygame.draw.circle(WINDOW, WHITE, CENTER, ARENA_RADIUS, 2)

    for i, ball in enumerate(balls):
        ball.draw(WINDOW)
        pygame.draw.circle(
            WINDOW,
            ball_owners[i].color,
            (int(ball.pos[0]), int(ball.pos[1])),
            ball.radius + 5,
            3
        )

    for paddle in paddles:
        paddle.draw(WINDOW)

    for i, score in enumerate(scores):
        text = font.render(f"Player {i+1}: {score}", True, paddles[i].color)
        x = 20 if i % 2 == 0 else WIDTH - text.get_width() - 20
        y = 20 + 40 * (i // 2)
        WINDOW.blit(text, (x, y))

    pygame.display.update()

pygame.quit()
