import turtle
import time
import random
from game_elements import *
from controls import bind_keys
from score_manager import load_high_score, save_high_score

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)
screen.tracer(0)

# Load high score and update initial display
score = 0
high_score = load_high_score()
update_score(score, high_score)

# Setup border and legend, place food, and bind controls
setup_border()
setup_legend()
place_food()
bind_keys(screen)

# Timer for golden food (initially set to spawn after 10-20 seconds)
golden_timer = time.time() + random.randint(10, 20)
# This will track how long the golden food stays on screen
golden_appearance_timer = None
golden_food_visible_duration = 5  # Golden food disappears after 5 seconds

# Variables
speed = 0.1
SPEED_MULTIPLIER = 0.98
SPEED_MIN_THRESHOLD = 0.05  # Minimum speed allowed


def adjust_speed(current_speed, multiplier):
    new_speed = current_speed * multiplier
    return max(new_speed, SPEED_MIN_THRESHOLD)


def reset_game(segments):
    """Reset the game to its initial state."""
    global score, high_score
    head.goto(0, 0)

    # Reset score and segments
    score = 0
    high_score = load_high_score()
    update_score(score, high_score)
    for segment in segments:
        segment.goto(1000, 1000)  # Move off-screen
    segments.clear()

    # Reset speed
    speed = 0.1
    return score, speed


def handle_game_over(screen, segments):
    """Handle game-over logic for collision with walls or snake body."""
    global score, high_score
    time.sleep(1)

    # Save the high score if it exceeds the previous high score
    if score > high_score:
        save_high_score(score)

    # Reset score and speed
    score, speed = reset_game(segments)

    # Disable controls during game over
    bind_keys(screen, False)
    time.sleep(2)  # Give time for game-over effect
    screen.update()

    # Reset direction explicitly to stop movement
    head.direction = "Stop"  # Ensure no movement while game is reset

    # Re-enable controls after game over
    bind_keys(screen, True)

    return score, speed


def move():
    """Move the snake based on the current direction of the head."""
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


def check_food_collision():
    """Check for collision with normal food."""
    global score, speed
    if head.distance(food) < 20:
        place_food()  # Reposition food
        score += 1
        add_segments()  # Add new segment to snake
        speed = adjust_speed(speed, SPEED_MULTIPLIER)  # Increase speed
        update_score(score, high_score)  # Update score display
        return True
    return False


def check_golden_food_collision():
    """Check for collision with golden apple."""
    global score, speed
    if golden_food.isvisible() and head.distance(golden_food) < 20:
        golden_food.hideturtle()  # Remove golden apple
        score += 3  # Golden apple gives 3 points
        add_segments(3)  # Add 3 segments for golden food
        # Faster speed change for golden food
        speed = adjust_speed(speed, (SPEED_MULTIPLIER ** 3))
        update_score(score, high_score)  # Update score display
        return True
    return False


def check_golden_food_timer():
    """Check if it's time to show or hide golden food."""
    global golden_appearance_timer
    if golden_appearance_timer and time.time() > golden_appearance_timer:
        golden_food.hideturtle()  # Hide the golden food
        golden_appearance_timer = None  # Reset the appearance timer

    # Toggle visibility of golden food when it's nearing disappearance
    if golden_appearance_timer and golden_appearance_timer - time.time() < 1:
        if int(time.time() * 10) % 2 == 0:  # Blink effect
            golden_food.showturtle()
        else:
            golden_food.hideturtle()


def spawn_golden_food():
    """Handle golden food spawn logic."""
    global score, golden_timer, golden_appearance_timer
    if score >= 1 and time.time() > golden_timer:
        place_golden_food()  # Place golden food
        golden_appearance_timer = time.time() + golden_food_visible_duration  # Set timer
        golden_timer = time.time() + random.randint(10, 20)  # Schedule next appearance


def move_snake():
    """Move the snake's body segments."""
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()  # Move the head of the snake


# Main game loop
while True:
    screen.update()

    # Check for collisions with food and golden food
    if check_food_collision():
        pass  # Food collision already handled in function

    if check_golden_food_collision():
        golden_appearance_timer = None  # Reset timer if golden food is eaten

    # Handle golden food timer and spawning
    spawn_golden_food()
    check_golden_food_timer()

    # Move snake
    move_snake()

    # Check for collisions with walls or self
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        score, speed = handle_game_over(screen, segments)
    for segment in segments:
        if head.distance(segment) < 20:
            score, speed = handle_game_over(screen, segments)

    time.sleep(speed)
