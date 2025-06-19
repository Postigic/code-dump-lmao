import turtle

def create_hand(color, thickness):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(thickness)
    t.hideturtle()
    return t

def draw_hand(t, length, angle):
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(angle)
    t.pendown()
    t.forward(length)
