import math

WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
ARENA_RADIUS = 250

def reflect_with_curve(ball_pos: tuple, ball_vel: tuple, reference_angle: float, curve_strength: float = 0.3):
    dx = ball_pos[0] - CENTER[0]
    dy = ball_pos[1] - CENTER[1]
    dist = math.hypot(dx, dy)

    if dist == 0:
        return ball_vel

    ball_angle = math.atan2(dy, dx) % (2 * math.pi)
    offset = ((ball_angle - reference_angle + math.pi) % (2 * math.pi)) - math.pi
    curve = math.sin(offset) * curve_strength

    nx = dx / dist
    ny = dy / dist

    vx, vy = ball_vel
    v_mag = math.hypot(vx, vy)
    if v_mag == 0:
        return ball_vel

    v_norm = [vx / v_mag, vy / v_mag]

    dot = v_norm[0] * nx + v_norm[1] * ny
    rx = v_norm[0] - 2 * dot * nx
    ry = v_norm[1] - 2 * dot * ny

    rx, ry = (
        rx * math.cos(curve) - ry * math.sin(curve),
        rx * math.sin(curve) + ry * math.cos(curve),
    )

    return [rx * v_mag, ry * v_mag]
