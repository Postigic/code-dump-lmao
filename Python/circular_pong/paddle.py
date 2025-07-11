import math
import random
import pygame
from utils import CENTER, ARENA_RADIUS, reflect_with_curve

class Paddle:
    def __init__(self, angle: float, color: tuple, keys: tuple = None, is_ai: bool = False):
        self.angle = angle
        self.width = math.radians(30)
        self.radius = ARENA_RADIUS - 10
        self.speed = math.radians(3)
        self.color = color
        self.keys = keys
        self.is_ai = is_ai
        self.mode = "defensive"
        self.mode_timer = 0
        self.aim_offset = 0

    @staticmethod
    def polar_to_cartesian(center, radius, angle):
        return (
            int(center[0] + radius * math.cos(angle)),
            int(center[1] + radius * math.sin(angle))
        )

    def draw(self, surface):
        start_angle = self.angle - self.width / 2
        end_angle = self.angle + self.width / 2
        num_points = 30
        arc_points = [
            self.polar_to_cartesian(CENTER, self.radius, start_angle + i * (end_angle - start_angle) / num_points)
            for i in range(num_points + 1)
        ]
        
        pygame.draw.lines(surface, self.color, False, arc_points, 5)

    def update(self, ball_pos: tuple = None, ball_owner: object = None, ball: object = None):
        if self.is_ai and ball_pos:
            if ball_owner == self:
                return

            if self.mode_timer <= 0:
                self.ai_mode = random.choice(["defensive", "aggressive"])
                self.mode_timer = 300

                if self.ai_mode == "defensive":
                    self.aim_offset = random.uniform(-math.radians(3), math.radians(3))
                elif self.ai_mode == "aggressive":
                    direction = random.choice([-1, 1])
                    self.aim_offset = direction * random.uniform(-math.radians(3), math.radians(3))
            else:
                self.mode_timer -= 1

            px, py = ball.pos
            vx, vy = ball.vel

            dx = px - CENTER[0]
            dy = py - CENTER[1]
            dist = math.hypot(dx, dy)

            approaching = abs(dist - self.radius) <= 30

            if approaching:
                pred_vx, pred_vy = reflect_with_curve((px, py), (vx, vy), self.angle)
                pred_vx, pred_vy = -pred_vx, -pred_vy
            else:
                pred_vx, pred_vy = vx, vy

            a = pred_vx ** 2 + pred_vy ** 2
            b = 2 * (dx * pred_vx + dy * pred_vy)
            c = dx ** 2 + dy ** 2 - ARENA_RADIUS ** 2

            delta = b ** 2 - 4 * a * c

            if a == 0 or delta < 0:
                return
            
            sqrt_delta = math.sqrt(delta)
            t1 = (-b + sqrt_delta) / (2 * a)
            t2 = (-b - sqrt_delta) / (2 * a)

            t = min([time for time in [t1, t2] if time > 0], default=None)
            if t is None:
                return
            
            fx = px + pred_vx * t
            fy = py + pred_vy * t
            intercept_angle = math.atan2(fy - CENTER[1], fx - CENTER[0])

            target_angle = (intercept_angle + self.aim_offset) % (2 * math.pi)
            diff = (target_angle - self.angle + math.pi) % (2 * math.pi) - math.pi

            if abs(diff) > math.radians(3):
                self.angle = (self.angle + self.speed * (1 if diff > 0 else -1)) % (2 * math.pi)
        elif self.keys:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                self.angle -= self.speed
            if keys[self.keys[1]]:
                self.angle += self.speed
