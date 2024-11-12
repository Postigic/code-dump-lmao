import turtle
import time
from game_elements import head, food, segments, place_food, move, update_score, setup_border
from controls import bind_keys
from score_manager import load_high_score, save_high_score

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Load high score and update initial display
score = 0
high_score = load_high_score()
update_score(score, high_score)

# Setup border, place food, and bind controls
setup_border()
place_food()
bind_keys(screen)

# Main game loop
speed = 0.1
while True:
    screen.update()

    # Check for collision with food
    if head.distance(food) < 20:
        place_food()  # Reposition food
        score += 1

        # Add new segment to snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Update score display
        update_score(score, high_score)

    # Move the snake's segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with walls
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Update high score if needed
        if score > high_score:
            high_score = score
            save_high_score(high_score)

        # Reset score and segments
        score = 0
        update_score(score, high_score)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Check for collision with the snake's own body
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Update high score if needed
            if score > high_score:
                high_score = score
                save_high_score(high_score)

            # Reset score and segments
            score = 0
            update_score(score, high_score)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(speed)
