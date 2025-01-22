import pygame
import time
from utilities import *
from commands import commands


def boot_sequence():
    boot_messages = [
        ("$ init-core --start", WHITE),
        ("[ALERT] Boot sequence initialized...", ORANGE),
        ("$ load-module --core-init /opt/core/boot", WHITE),
        ("[INFO] Loading Core Initialization Module...", CYAN),
        ("$ check-core --status", WHITE),
        ("[DEBUG] Core integrity: PASS", YELLOW),
        ("$ load-network --sync", WHITE),
        ("[INFO] Syncing Core Network...", CYAN),
        ("$ connect-pods --activate all", WHITE),
        ("[INFO] Activating Pod Systems...", CYAN),
        ("$ start-subsystems --all", WHITE),
        ("[DEBUG] Booting up subsystems...", YELLOW),
        ("$ core-status --check --energy", WHITE),
        ("[INFO] Energy systems: Optimal", CYAN),
        ("$ core-diagnostics --scan --deep", WHITE),
        ("[ALERT] Running deep system diagnostics...", ORANGE),
        ("$ memory-check --core", WHITE),
        ("[DEBUG] Core memory: 98% operational", YELLOW),
        ("$ initialize-quantum-link --node-02", WHITE),
        ("[INFO] Establishing Quantum Link...", CYAN),
        ("$ sync-clusters --secure", WHITE),
        ("[INFO] Syncing Core Clusters...", CYAN),
        ("$ activate-neural-net --load", WHITE),
        ("[DEBUG] Loading Neural Network Core...", YELLOW),
        ("$ core-diagnostics --final-check", WHITE),
        ("[INFO] Core diagnostics completed...", CYAN),
        ("$ load-UI --launch", WHITE),
        ("[INFO] Initializing Core UI...", CYAN),
        ("$ verify-system --core-access", WHITE),
        ("[DEBUG] System access verified...", YELLOW),
        ("$ core-status --final-check", WHITE),
        ("[WARN] Good luck.", ORANGE),
        ("[INFO] Core status: ALL SYSTEMS NOMINAL", CYAN),
        ("$ shutdown-protocol --execute", WHITE),
        ("[INFO] System shutting down for final preparation...", CYAN),
        ("$ restart-core --force", WHITE),
        ("[WARN] I have a feeling you'll need it.", ORANGE),
        ("[SUCCESS] Core initialized. Initializing control interface...", CYAN),
    ]

    screen.fill(BLACK)
    draw_scanlines()

    line_height = 30
    padding = 10
    line_height = 30

    start_y = padding
    y_offset = start_y

    for message, color in boot_messages:
        current_frame = 0
        while current_frame <= len(message):
            pygame.event.get()
            screen.fill(BLACK)
            draw_scanlines()

            for i, (msg, col) in enumerate(boot_messages[:boot_messages.index((message, color))]):
                draw_text(screen, msg, 10, start_y + i * line_height, col)

            animate_log_event(message, 10, y_offset, current_frame, FONT.size(" ")[0], color)
            current_frame += 1
            draw_cursor(10 + FONT.size(message[:current_frame])[0], y_offset)

            pygame.display.flip()
            time.sleep(0.01)

        y_offset += line_height
        time.sleep(0.2)


def draw_text(surface, text, x, y, color=WHITE):
    rendered_text = FONT.render(text, True, color)
    surface.blit(rendered_text, (x, y))


def draw_cursor(x, y):
    if pygame.time.get_ticks() // 500 % 2 == 0:
        draw_text(screen, "|", x, y, CYAN)


def draw_scanlines():
    for i in range(0, HEIGHT, 4):
        pygame.draw.line(screen, (20, 20, 20), (0, i), (WIDTH, i))


def animate_log_event(text, x, y, current_frame, char_width, color=WHITE):
    for i in range(min(current_frame, len(text))):
        draw_text(screen, text[i], x + i * char_width, y, color)


def draw_section_header(title, y_offset, color=YELLOW):
    draw_text(screen, f"--- {title} ---", 10, y_offset, color)
    return y_offset + 30


def draw_text_lines(lines, y_offset, line_height=30, color=CYAN):
    for i, line in enumerate(lines):
        draw_text(screen, f"  {line}", 10, y_offset + i * line_height, GREEN if "INFO" in line else (RED if "WARNING" in line or "ERROR" in line else color))
    return y_offset + len(lines) * line_height


def draw_commands(commands, y_offset, line_height=30):
    draw_text(screen, "--- Commands ---", 10, y_offset, YELLOW)
    y_offset += 30
    for display_name, description in commands:
        draw_text(screen, f"  {display_name} : {description}", 10, y_offset)
        y_offset += line_height
    return y_offset


def draw_logs(log_messages, y_offset, line_height=30):
    from logger import log_messages
    pygame.draw.rect(screen, GREY, (10, y_offset, WIDTH - 20, 320), border_radius=5)
    
    for log in log_messages:
        draw_text(screen, log["message"], 20, y_offset + 10, log["color"])
        log["current_frame"] = min(log["current_frame"] + 2, len(log["message"]))
        y_offset += line_height
    return y_offset


def draw_terminal_ui(core, input_text):
    status = core.get_status()

    line_height = 30
    padding = 30

    y_offset = 10

    y_offset = draw_section_header("QTEC Status", y_offset, YELLOW)
    y_offset = draw_text_lines(status, y_offset, line_height)

    energy_quota = core.get_energy_quota()
    y_offset += padding
    y_offset = draw_section_header("Energy Quota", y_offset, YELLOW)
    y_offset = draw_text_lines(energy_quota, y_offset, line_height, PURPLE)

    command_list = [(info["display"], info["description"]) for info in commands.values()]
    y_offset += padding
    y_offset = draw_commands(command_list, y_offset)

    from logger import log_messages
    log_area_top = HEIGHT - 400
    y_offset = draw_logs(log_messages, log_area_top, line_height)

    pygame.draw.rect(screen, GREY, (10, HEIGHT - 70, WIDTH - 20, 40), border_radius=5)
    draw_text(screen, f"> {input_text}", 20, HEIGHT - 61, CYAN)
    draw_cursor(20 + FONT.size(f"> {input_text}")[0], HEIGHT - 62)
