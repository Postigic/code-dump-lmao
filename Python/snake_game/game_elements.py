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

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 300)

# Border setup


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


def place_food():
    """Place the food at a random location."""
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    food.goto(x, y)


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


def update_score(score, high_score):
    """Update the score display."""
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {
                            high_score}", align="center", font=("Courier", 24, "normal"))
