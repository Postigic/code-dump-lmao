import pygame
import math
import random
from utils import CENTER, reflect_with_curve

class Ball:
    def __init__(self, radius=10, speed=4, max_speed=25, color=(255, 255, 255)):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.max_speed = max_speed
        self.grace_frames = 60
        self.reset(speed)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def reset(self, speed=None):
        self.pos = list(CENTER)
        self.vel = [0, 0]
        self.grace_frames = 60
        if speed is not None:
            self.speed = speed

    def update(self):
        if self.grace_frames > 0:
            self.grace_frames -= 1
            if self.grace_frames == 0:
                angle = random.uniform(0, 2 * math.pi)
                self.vel = [self.speed * math.cos(angle), self.speed * math.sin(angle)]
        else:
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]

            speed = math.hypot(self.vel[0], self.vel[1])
            if speed > self.max_speed:
                scale = self.max_speed / speed
                self.vel[0] *= scale
                self.vel[1] *= scale

    def resolve_collision(self, paddle):
        last_pos = self.pos[:]
        next_pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]

        for t in [i / 5 for i in range(6)]:
            interp_x = last_pos[0] + (next_pos[0] - last_pos[0]) * t
            interp_y = last_pos[1] + (next_pos[1] - last_pos[1]) * t
            dx = interp_x - CENTER[0]
            dy = interp_y - CENTER[1]
            dist = math.hypot(dx, dy)
            ball_angle = math.atan2(dy, dx) % (2 * math.pi)

            start_angle = (paddle.angle - paddle.width / 2) % (2 * math.pi)
            end_angle = (paddle.angle + paddle.width / 2) % (2 * math.pi)
            in_arc = (start_angle <= ball_angle <= end_angle) if start_angle < end_angle else (ball_angle >= start_angle or ball_angle <= end_angle)

            if abs(dist - paddle.radius) <= self.radius + 2 and in_arc:
                new_vel = reflect_with_curve((interp_x, interp_y), self.vel, paddle.angle)
                new_speed = math.hypot(*new_vel) * 1.05
                self.vel = [component * (new_speed / math.hypot(*new_vel)) for component in new_vel]

                nx = dx / dist
                ny = dy / dist

                buffer = 2
                target_dist = paddle.radius - self.radius - buffer
                self.pos[0] = CENTER[0] + nx * target_dist
                self.pos[1] = CENTER[1] + ny * target_dist

                return True

        return False
