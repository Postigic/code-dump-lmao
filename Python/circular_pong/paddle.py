import math
import random
import pygame
from ball import Ball
from utils import CENTER, ARENA_RADIUS, reflect_with_curve

class Paddle:
    def __init__(self, angle: float, color: tuple, keys: tuple = None, is_ai: bool = False):
        self.angle = angle
        self.width = math.radians(30)
        self.radius = ARENA_RADIUS - 10
        self.speed = math.radians(5)
        self.color = color
        self.keys = keys
        self.is_ai = is_ai # i should have wrote is_bot but eh
        self.aim_offset = 0

    @staticmethod
    def polar_to_cartesian(center: tuple, radius: float, angle: float) -> tuple:
        return (
            int(center[0] + radius * math.cos(angle)),
            int(center[1] + radius * math.sin(angle))
        )

    def draw(self, surface: pygame.Surface) -> None:
        start_angle = self.angle - self.width / 2
        end_angle = self.angle + self.width / 2
        num_points = 30
        arc_points = [
            self.polar_to_cartesian(CENTER, self.radius, start_angle + i * (end_angle - start_angle) / num_points)
            for i in range(num_points + 1)
        ]
        
        pygame.draw.lines(surface, self.color, False, arc_points, 5)

    def update(self, balls: list, owners: list) -> None:
        if self.is_ai:
            target = self.choose_target(balls, owners)
            if target:
                self.track_ball(target)
        elif self.keys:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                self.angle -= self.speed
            if keys[self.keys[1]]:
                self.angle += self.speed

    def choose_target(self, balls: list, owners: list) -> Ball | None:
        best_time = float("inf")
        best_ball = None

        for ball, owner in zip(balls, owners):
            if owner == self:
                continue

            tti = self.time_to_intercept(ball)
            if tti and tti < best_time:
                best_time, best_ball = tti, ball

        return best_ball
    
    @staticmethod
    def intercept_times(px: float, py: float, vx: float, vy: float, radius: float) -> list[float]:
        dx, dy = px - CENTER[0], py - CENTER[1]

        a = vx**2 + vy**2
        b = 2 * (dx*vx + dy*vy)
        c = dx**2 + dy**2 - radius**2

        delta = b**2 - 4*a*c
        if a == 0 or delta < 0:
            return []

        sqrt_delta = math.sqrt(delta)
        t1 = (-b + sqrt_delta) / (2*a)
        t2 = (-b - sqrt_delta) / (2*a)

        return [t for t in (t1, t2) if t > 0]

    def time_to_intercept(self, ball: Ball) -> float | None:
        times = self.intercept_times(*ball.pos, *ball.vel, ARENA_RADIUS)
        return min(times, default=None)

    def predict_intercept(self, ball: Ball, max_steps=500, dt=1.0) -> float | None:
        sim_pos = ball.pos[:]
        sim_vel = ball.vel[:]

        for _ in range(max_steps):
            sim_pos[0] += sim_vel[0] * dt
            sim_pos[1] += sim_vel[1] * dt

            dx = sim_pos[0] - CENTER[0]
            dy = sim_pos[1] - CENTER[1]
            dist = math.hypot(dx, dy)

            if dist >= self.radius - ball.radius:
                return math.atan2(dy, dx)

        return None

    def track_ball(self, ball: Ball) -> None:
        intercept_angle = self.predict_intercept(ball)
        if intercept_angle is None:
            return

        target_angle = (intercept_angle + self.aim_offset) % (2*math.pi)
        diff = (target_angle - self.angle + math.pi) % (2*math.pi) - math.pi

        if abs(diff) > math.radians(3):
            self.angle = (self.angle + self.speed * (1 if diff > 0 else -1)) % (2*math.pi)
