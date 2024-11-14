import turtle
import random


# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake body segments
segments = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()

# Golden food
golden_food = turtle.Turtle()
golden_food.shape("circle")
golden_food.color("gold")
golden_food.penup()
golden_food.hideturtle()

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 300)


def setup_border():
    """Create a white border around the game area."""
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.goto(-290, 290)  # Starting at top-left corner
    border.pendown()
    for _ in range(4):
        border.forward(580)
        border.right(90)
    border.penup()
    border.hideturtle()


def setup_legend():
    legend = turtle.Turtle()
    legend.speed(0)
    legend.color("white")
    legend.penup()
    legend.hideturtle()
    legend.goto(-750, -200)  # Positioning the legend on the left side
    legend.write("""
    CONTROLS:
    W - Move Up
    S - Move Down
    A - Move Left
    D - Move Right

    OBJECTS:
    Player: White Square
    Food: Red Circle
    Golden Food: Gold Circle

    SCORING:
    Food: +1 Point
    Golden Food: +3 Points

    GAME MECHANICS:
    Speed increases with each food eaten
    """, align="left", font=("Courier", 14, "normal"))


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


def determine_coords():
    """Generate random coordinates within the game boundaries."""
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    return x, y


def place_food():
    """Place the food at a random location."""
    x, y = determine_coords()
    food.goto(x, y)


def place_golden_food():
    x, y = determine_coords()
    golden_food.goto(x, y)
    golden_food.showturtle()


def add_segments(count=1):
    for _ in range(count):
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(1000, 1000)
        segments.append(new_segment)


def update_score(score, high_score):
    """Update the score display."""
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {
                        high_score}", align="center", font=("Courier", 24, "normal"))
