from game_elements import head, segments


def go_up():
    if len(segments) == 0 or head.direction != "down":
        head.direction = "up"


def go_down():
    if len(segments) == 0 or head.direction != "up":
        head.direction = "down"


def go_left():
    if len(segments) == 0 or head.direction != "right":
        head.direction = "left"


def go_right():
    if len(segments) == 0 or head.direction != "left":
        head.direction = "right"


def bind_keys(screen, enable=True):
    """Bind or unbind the keys to control the snake based on the 'enable' flag."""
    screen.listen()

    if enable:
        screen.onkey(go_up, "w")
        screen.onkey(go_down, "s")
        screen.onkey(go_left, "a")
        screen.onkey(go_right, "d")
    else:
        screen.onkey(None, "w")
        screen.onkey(None, "s")
        screen.onkey(None, "a")
        screen.onkey(None, "d")
